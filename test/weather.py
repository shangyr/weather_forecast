import requests
import redis
import time
import datetime
import json
import re


def load_city():
    with open("../city.txt", "r", encoding='utf8') as f:
        city = f.readlines()
    city_list = city[0].replace('\xa0', " ").split(' ')
    return city_list

def run(city,pool):
    r = redis.Redis(connection_pool=pool)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.9101 SLBChan/115 SLBVPV/64-bit",
        "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://weathernew.pae.baidu.com/weathernew/pc"
    params = {
        "query": city + '天气',
        "srcid": "4982",
        "forecast": "long_day_forecast"
    }
    response = requests.get(url, headers=headers,params=params)
    # print(city)
    # print(response.text)
    if response.text:
        weather_data = json.loads(re.findall("window.tplData = (.*?);</script>",response.text)[0])
        print(weather_data)
        current_date = str(datetime.date.today())
        key = city + current_date
        #存入 5数据库
        r.set(key,json.dumps(weather_data))
        # print(r.get(key))
    else:
        print("ip限制，或网络故障")
#加载配置
with open("../config.json", "r", encoding="utf8") as f:
    config = json.load(f)
redis_address = config['redis_address']
redis_port = config['redis_port']
#数据库5作为单爬虫数据存储
pool = redis.ConnectionPool(host=redis_address, port=redis_port, db=5, max_connections=10)
city_list = load_city()
print(f"-----------------------------当前为单线程爬虫，采集{len(city_list)}个县城天气预报---------------------------------------")
print("程序开始计时")
start = time.time()
for city in city_list:
    #开始采集太难起
    run(city,pool)
    #防止速度过快被封，最后计算时间，需要 (总时间 - 5 * len(city_list)) !!!!!
    time.sleep(5)
#结束时间
end = time.time()
timeee = end - start
print(timeee)
cast_time = end - start - 5 * len(city_list)
print(f"采集{len(city_list)}个县城天气预报共耗时：{end - start}")
print("-------------------------------------------------------程序结束-----------------------------------------------------")