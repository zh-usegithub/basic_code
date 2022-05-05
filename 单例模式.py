class person():
    __addrspace = None
    def __new__(cls):
        if cls.__addrspace is None:
            cls.__addrspace = object.__new__(cls)#创建一个空间并赋值给私有类属性__addrspace
            return cls.__addrspace#返回创建对象的地址空间
        else:
            return cls.__addrspace
s1 = person()
s2 = person()
print(s1,s2)#打印出来的两个对象的地址空间是一样的