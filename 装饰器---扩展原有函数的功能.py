# 下面创建一个装饰器用于校验在传参的时候限制于height小于190
def check_personinfo(func):
    print('123')

    def warp(name, age, height, *args, **kwargs):
        print(type(height))
        if int(height) > 190:
            print('height is bigger,please check !')
            return
        return func(name, age, height)

    return warp  # 这里是返回函数，相当于把当前的函数的地址空间赋值给另一个函数名变量引用


@check_personinfo
def person(name, age, height):
    print('name is {},age is {},height is {}'.format(name, age, height))


person('zh', '19', 195)
