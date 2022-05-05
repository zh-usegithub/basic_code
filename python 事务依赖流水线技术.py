import redis
pool = redis.ConnectionPool(host = '192.168.109.130',port = 6379,db = 0,password = '123456')#创建一个连接池
r = redis.Redis(connection_pool=pool)#创建一个连接池对象
with r.pipeline(transaction=True) as pipe:
    pipe.multi()#创建流水线
    pipe.incr('num')
    pipe.incr('num')
    value = pipe.execute()#把流水线上的redis命令发送给redis执行，并把执行的结果以列表的形式返回给value
    print(value)





