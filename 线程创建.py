import threading
from time import sleep
def download(n):
    images = ['动物1','动物2','动物3','动物4','动物5','动物6']
    for image in images:
        print('正在下载',image)
        sleep(n)
        print('{}下载完成'.format(image))
def listening(n):
    images = ['动物1','动物2','动物3','动物4','动物5','动物6']
    for image in images:
        print('正在收听',image)
        sleep(n)
        print('{}收听完成'.format(image))
if __name__ == '__main__':
    t1 = threading.Thread(target=download,name='aa',args=(1,))
    t2 = threading.Thread(target=listening, name='bb',args=(1,))
    t1.start()
    t2.start()
    n = 1
    while True:
        sleep(1)
        print(n)
        n+=1

