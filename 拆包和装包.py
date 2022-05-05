a = (1,2,3)
print(*a)#这里时拆包的过程
b,*c = a#这里时一个连续的过程，拆包->装包，a元组会自动进行拆包的动作，然后进行装包把2，3以列表的形式装进变量c里面
print(c)
e,f,g,*h = a#这里在进行装包的操作时，由于h接收到的数据为空，所以h返回一个空列表
print(h)
d = dict([('name','zh'),('age',18),('height',180)])#把列表转换成字典
print(d)
print(type(d))
def dict_test(**kwargs):
    print(kwargs)
dict_test(name = 'zh',age = 19)

def demo(*args,**kwargs):
    print(args)
    print(kwargs)
num = (1,2,3)
dict_test_l = {'name':'小明','age':18}
demo(num,dict_test_l)#这个是不拆包传参，相当于两个元素都传给了args
demo(*num,**dict_test_l)#这个是拆包传参,这样第一个是元组类型传给args,第二个是字典类型，传给kwargs,**dict_test_l拆包后相当于变成了name = 小明,age = 18




