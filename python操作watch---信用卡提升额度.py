"""场景：两个人同时操作一个人的行用卡额度
1.解决办法是watch这个账户，如果在一个人修改这个账户的额度的期间（还未修改完成），另一人也在修改这个账户的额度（并且修改成功），那么此次事务操作失败"""
import redis
from time import sleep
#创建连接池并连接到redis，以后在连接redis的时候尽量使用redis的连接池进行连接数据库的操作，这样可以减轻与redis重复建连的压力
pool = redis.ConnectionPool(host = '192.168.109.130',db = 0,port = 6379,password = '123456')
r = redis.Redis(connection_pool=pool)#从池子里面拿一个连接

def double_account(user_id):
    key = 'account_%s'%(user_id)
    with r.pipeline(transaction=True) as pipe:
        #一般在使用watch的时候需要使用while循环直到事务提交成功
        while True:
            try:#这里使用try的原因是在while循环体里面如果发生了错误会立刻退出循环，为了不终止循环可以使用捕获异常的方式
                pipe.watch(key)#流水线上的点命令是暂时不发送出去（直到pipe.execute），但是这个watch命令有点特殊，使用这个命令会立刻发送给redis进行执行
                print('slep is start')
                sleep(10)#在sleep期间直接去redis数据库修改这个账户的额度
                print('slep is end')
                value = int(r.get(key))#使用r连接直接把redis中的这个账户的值取出来
                value *= 2#值翻倍
                pipe.multi()#开启事务
                pipe.set(key,value)
                pipe.execute()
                break#如果事务操作成功则退出循环
            except redis.WatchError:#抓取WatchError操作
                print('---key changed,try agin---')
                continue#结束本次循环进行下一次循环
    return int(r.get(key))

if __name__ == '__main__':
    #首先需要在redis 数据库中开户，初始化account_zh账户的额度为500
    print(double_account('zh'))






