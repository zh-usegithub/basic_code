class Person():
    def __init__(self,name):
        self.name = name
    def feed_pet(self,pet):
        if isinstance(pet,Pet):
            print('{}喜欢养{},昵称是:{}'.format(self.name,pet.role,pet.nikename))
        else:
            print('不是宠物不能养')
class Pet:
    role = 'Pet'
    def __init__(self,nikename,age):
        self.nikename = nikename
        self.age = age
    def show(self):
        print('昵称是{},年龄是{}'.format(self.nikename,self.age))
class Cat(Pet):
    role = '猫'
    def catch_mouse(self):
        print('猫捕食物')
class Dog(Pet):
    role = '狗'
    def watch_house(self):
        print('看家高手')
class Tiger():
    def show(self):
        print('老虎不能养哦')
cat = Cat('小猫',1)
dog = Dog('小狗',2)
tiger = Tiger()
person = Person('小王')
person.feed_pet(cat)
person.feed_pet(dog)
person.feed_pet(tiger)



