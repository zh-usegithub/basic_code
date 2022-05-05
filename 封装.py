class person():
    def __init__(self,name,age,height):
        self.name = name
        self.__age = age#这里私有化age属性
        self.height = height
    def run(self):
        print(self.name,'正在跑步')
    #向外部暴露公有的get方法
    @property
    def age(self):
        return self.__age
    #向外界暴露公有的set方法，这个set方法必须需要先定义公有的get方法才能使用
    @age.setter
    def age(self,age_num):
        self.__age = age_num
    #以下重写的魔术方法在打印类对象的时候会自动调用
    def __str__(self):
        return '{}的年龄是{},身高是{}'.format(self.name,self.__age,self.height)
person= person('小王',18,179)
print(person)#打印类对象自动调用魔术方法__str__
person.age=20#调用公有的set方法修改年龄的值，这里使用了等号赋值，就会默认调用经过@age.setter修饰的age方法即类似set_age的功能
print(person)
print('修改后的年龄是',person.age)#调用公有的get方法获取年龄的值
person.run()#调用类方法
