#创建连接池并连接到redis
import redis
import time
pool = redis.ConnectionPool(host = '192.168.109.130',port = 6379,password = '123456',db = 0)
r = redis.Redis(connection_pool=pool)#获得一个连接池对象
def withpipline(r):
    p = r.pipeline()#使用pipline流水线
    for i in range(1000):
        key = 'test1'+str(i)
        value = i+1
        p.set(key,value)
    p.execute()
def withoutpipline(r):
    for i in range(1000):
        key = 'test2'+str(i)
        value = i+1
        r.set(key,value)
if __name__ == '__main__':
    t1 = time.time()
    withoutpipline(r)
    t2 = time.time()
    print('withoutpipline time is %s'%(t2-t1))
    t3 = time.time()
    withpipline(r)
    t4 = time.time()
    print('withpipline time is %s' % (t4 - t3))

