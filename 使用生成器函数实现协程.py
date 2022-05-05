def run():
    for i in range(10):
        print('跑步{}公里'.format(i))
        yield
def sing():
    for i in range(10):
        print('唱第{}首歌曲'.format(i))
        yield
if __name__ == '__main__':

    a = run()
    b = sing()

    while True:
        try:
            next(a)
            next(b)
        except:
            break
