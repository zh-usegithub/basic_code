import redis
from time import sleep
"""乐观锁的作用是当事务在执行期间，加上了乐观锁的键对应值发生了变化，事务操作会失败，具体例子可在python操作watch.py文件中理解"""
pool = redis.ConnectionPool(host = '192.168.109.130',db = 0,port = 6379,password = '123456')
r = redis.Redis(connection_pool=pool)
with r.pipeline(transaction=True) as pipe:
    pipe.watch('num')#给redis的键num加上乐观锁
    pipe.multi()#创建流水线
    sleep(10)#等待10秒，在此期间用其他方式操作redis改变num的值，在这里我在此期间直接操作虚拟机上的redis的num的值改变，打印的value报错redis.exceptions.WatchError: Watched variable changed.
    pipe.incr('num')
    pipe.incr('num')
    value = pipe.execute()#把流水线上的redis命令发送给redis执行，并把执行的结果以列表的形式返回给value
    print(value)