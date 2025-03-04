from flask import Flask,request, jsonify,make_response
from flask_cors import CORS
import requests
import json
import redis
app = Flask(__name__)

def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)
#设置跨域访问
CORS(app, supports_credentials=True)
def get_city():
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://www.baidu.com",
        "Referer": "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=15007414_dg&wd=ip&oq=ip&rsv_pq=f2418f200a1a97bb&rsv_t=defdh%2BVR%2BsLrLaYz1v8uiPq30h6y6fZ4ov4Ga2%2FeDENH7rM4og8LW1kqDMWkl2Nhbfs&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.9101 SLBChan/115 SLBVPV/64-bit",
        "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://qifu-api.baidubce.com/ip/local/geo/v1/district"
    params = {
        "": ""
    }
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text)
    if data['code'] == 'Success':
        district = data['data']['district']
        print(json.loads(response.text))
        return district
#获取当前城市
@app.route("/getCity")
def getcity():
    city = get_city()
    print(city)
    return city

def parse_redis_data(redis_data):
    if redis_data:
        return json.loads(redis_data.decode("utf8"))
#查询单词爬虫消耗时间
@app.route("/getDistributedTime")
def getDistributedTime():
    r = redis.Redis(host=config['redis_address'], port=config['redis_port'], db=11, max_connections=10)
    #获取机器各个任务的时间 machineId应该动态加载
    #机器一
    reqTime1 = float(parse_redis_data(r.get("machine1reqTime")))
    parseTime1 = float(parse_redis_data(r.get("machine1parseTime")))
    saveTime1 = float(parse_redis_data(r.get("machine1saveTime")))
    # print(reqTime1)
    # print(parseTime1)
    # print(saveTime1)
    m1_max = max(reqTime1,parseTime1,saveTime1)
    #比较各个任务最长时间为改机器花费时间
    # 机器二
    reqTime2 = float(parse_redis_data(r.get("machine2reqTime")))
    parseTime2 = float(parse_redis_data(r.get("machine2parseTime")))
    saveTime2 = float(parse_redis_data(r.get("machine2saveTime")))
    # print(reqTime2)
    # print(parseTime2)
    # print(saveTime2)
    m2_max = max(reqTime2,parseTime2,saveTime2)
    print(m1_max)
    print(m2_max)
    DistributedTime = max(m1_max,m2_max)
    print(DistributedTime)
    return str(DistributedTime)

#查询单词爬虫消耗时间
@app.route("/getSimpleTime")
def getSimpleTime():
    r = redis.Redis(host=config['redis_address'], port=config['redis_port'], db=5, max_connections=10)
    simpleTime = parse_redis_data(r.get("simpleTime"))
    print(simpleTime)
    return str(simpleTime)

#注册接口
@app.route("/register",methods=['POST'])
def register():
    data_list = request.json
    # print(data_list)
    usernamee = data_list['username']
    passworde = data_list['password']
    if not usernamee or not isinstance(usernamee,str):
        print("用户名为空")
        return "用户名为空"
    if not passworde or not isinstance(passworde,str):
        print("000")
        return "密码为空"
    print(usernamee)
    print(passworde)
    return "ok"
#根据城市查询天气
@app.route("/query_weather",methods=['POST'])
def query_weather():
    r = redis.Redis(host=config['redis_address'], port=6379, db=10, charset="utf-8", decode_responses=True)
    data_list = request.json
    # print(data_list)
    city = data_list['city']
    date = data_list['date']
    print(date)
    if not city or not isinstance(city,str):
        print("城市为空")
        return "城市为空"
    result = r.get(city+date)
    print(result)
    if result:
        return result
    else:
        return ""

if __name__ == '__main__':
    with open("config.json","r",encoding="utf8") as f:
        config = json.load(f)
    # 跨域支持
    app.run(host = '0.0.0.0' ,port = 5000, debug = 'True')