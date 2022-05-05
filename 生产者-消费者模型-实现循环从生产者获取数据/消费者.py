import redis
import json
redsis_client = redis.Redis(host='192.168.109.130',port=6379,db=0,password='123456')
while True:
    task = redsis_client.brpop('pyl2',10)#每10秒中访问一次数据库是否有新的值
    if task:
        print(task,'消费成功')
        json_obj = json.loads(task[1])
    else:
        print('---no task---')
