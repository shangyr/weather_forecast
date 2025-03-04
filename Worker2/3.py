import redis
r = redis.Redis(host='192.168.1.30', port=6379, db=11)
# 要存储的float对象
float_value = 3.14159
print(r.get('machine2req'))
# # 将float对象转换为字符串并存储
r.set('float_key', str(float_value))