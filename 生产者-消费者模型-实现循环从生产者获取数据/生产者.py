import redis
import json
redsis_client = redis.Redis(host='192.168.109.130',port=6379,password='123456',db=0)
json_obj = {'task':'send_email','email_body':'aaa','from':'bbb','to':'zh'}
json_str = json.dumps(json_obj)
redsis_client.lpush('pyl2',json_str)