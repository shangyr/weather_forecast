import requests
import time
import json
import re


def load_city():
    with open("city.txt", "r", encoding='utf8') as f:
        city = f.readlines()
    city_list = city[0].replace('\xa0', " ").split(' ')
    return city_list

def run(city):
    try:
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
        if response.text:
            weather_data = json.loads(re.findall("window.tplData = (.*?);</script>",response.text)[0])
            print(weather_data)

    except Exception:
        pass
city_list = load_city()
print(f"-----------------------------当前正在采集{len(city_list)}个城市天气预报---------------------------------------")
print("程序开始计时")
start = time.time()
for city in city_list:
    run(city)

end = time.time()
timeee = end - start
cast_time = end - start
print(f"采集{len(city_list)}个城市的天气预报共耗时：{end - start}s")
print("-------------------------------------------------------程序结束-----------------------------------------------------")