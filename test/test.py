import requests
import uuid
import json

r = redis.Redis(host='localhost', port=6379, db=0)

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