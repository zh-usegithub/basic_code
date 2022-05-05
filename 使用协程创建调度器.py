#有一个corn调度器，每一秒拉起一个job,要求这些job并发爬取网页
import asyncio
import random


async def cron_job(url):
    n = random.randint(1,3)
    await asyncio.sleep(n)
    print('下载结束',url)

async def cron_scheduler():
    page = 1
    while True:
        url = '{}/{}'.format('https://www.baidu.com',page)
        job = cron_job(url)#创建一个协程对象
        asyncio.create_task(job)#注册到事件循环
        await asyncio.sleep(0)#主动让出调度权到线程，让程序跳出这个循环有时间去执行协程任务
        page = page+1
if __name__ == '__main__':
    asyncio.run(cron_scheduler())
"""对于上面的代码在while循环中，我们不断拉起job，创建协程，并把它注册注册到事件循环中，
需要注意的是我们把协程对象注册到事件循环中后不会立即执行协程，当前是处于while True循环里面
我们需要使用await asyncio.sleep(0)做一个异步等待操作，让出调度权执行协程，并等待协程的返回，
如果不使用await asyncio.sleep(0)程序只会拉起协程任务，把他注册进事件循环中但是不会执行，因为程序处于
一个while的循环中没有时间去执行协程,相比于下面的协程代码：
async def a():
    while True:
        print('task-----1')
        await asyncio.sleep(0)

async def b():
    while True:
        print('task------2')
        await asyncio.sleep(0)
async def c():
    while True:
        print('task-----3')
        await asyncio.sleep(0)
if __name__ == '__main__':
    t1 = a()
    t2 = b()
    t3 = c()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(t1,t2,t3))
我们是把创建协程对象和注册事件循环分开编写的，协程任务是提前创建好的，只需要拉起这些任务即可，但是调度器协程是创建任务和拉起协程同时在一个while中，
所以需要await asyncio.sleep(0)让出调度权去执行协程
"""


