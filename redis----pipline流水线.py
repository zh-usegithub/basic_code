import redis
pool = redis.ConnectionPool(host = '192.168.109.130',db = 0,port = 6379,password = '123456')#创建一个redis连接池
r = redis.Redis(connection_pool=pool)#从池子里面拿一个redis连接
pipe = r.pipeline()#使用redis连接建立一个redis操作流水线
pipe.set('num',1)
pipe.incr('num')
pipe.incrby('num',100)
pipe.execute()#提交流水线的命令给redis执行

