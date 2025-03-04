import requests
import uuid
import json
import redis
pool = redis.ConnectionPool(host='192.168.1.30', port=6379, db=7,max_connections=10)
r = redis.Redis(host='192.168.1.30', port=6379, db=7)
retrieved_array_str = r.rpop('machine2')
print(retrieved_array_str)
print(retrieved_array_str.decode("utf8"))
task_list = json.loads(retrieved_array_str.decode("utf8"))
print(task_list)
# resp = requests.post(url=url,data=data)
# print(resp.status_code)
# with open("config.json", 'r', encoding='utf8') as f:
#     config = json.load(f)
# print(config)
# print(type(config))
#
# with open("city.txt","r",encoding='utf8') as f:
#     city = f.readlines()
# print(city[0].replace('\xa0'," "))
# city_list = city[0].replace('\xa0'," ").split(' ')
# print(len(city_list))
#
# with open('machineIds.json', 'r', encoding='utf8') as f:
#     machineIds = json.load(f)
# print(machineIds)