import redis
r = redis.Redis(host='192.168.1.30', port=6379, db=11)
# r = redis.Redis(host='192.168.1.30', port=6379, db=5)
import json

# 要存储的float对象
float_value = 3.14159
timm = r.get('machine2req')

# r.set("simpleTime",str(11))
# simpleTime = r.get("simpleTime")
# print(str(simpleTime))
print(json.loads(timm.decode("utf8")))
# # 将float对象转换为字符串并存储
# r.set('float_key', str(float_value))