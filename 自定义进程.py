from multiprocessing import Process
class myprocess(Process):
    #下面重写父类的init方法，并在里面调用父类的init方法
    def __init__(self,name):
        super(myprocess, self).__init__()
        self.name = name
    #重写run方法
    def run(self):
        n = 1
        while True:
            print('{}-----自定义进程,n = {}'.format(self.name,n))#这里的name是继承的Process类里面的进程名，所以直接使用
            n+=1
if __name__ == '__main__':
    p1  = myprocess('小明')
    p2 = myprocess('小红')
    p1.start()
    p2.start()

