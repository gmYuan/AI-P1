"""
class Cat:
    pass


def meow(self):
    return f"{self.name} 喵喵..."


Cat.speak = meow
cat1 = Cat()
cat1.name = "小白"
print(cat1.speak())


__age = 18


class MyPropertyWithSetter:
    def __init__(self, getter):
        # _getter是真正用来读取__age的方法 getAge
        self._getter = getter  # 都是被 装饰的函数
        # _setter是用来真正给__age赋值的方法 setAge
        self._setter = None  # 都是被 装饰的函数

    # 这是我们描述符协议规定的魔术方法，当取值的时候就会走__get__
    def __get__(self, obj, objtype):
        return self._getter(obj)

    # 这是我们描述符协议规定的魔术方法，当赋值的时候就会走__get__
    def __set__(self, obj, value):
        self._setter(obj, value)

    # 这是一个装饰器，是用来给 self._setter赋值为setAge方法的
    def setter(self, setter_func):
        self._setter = setter_func
        return self


# @MyPropertyWithSetter
def getAge(self):
    # 返回私有属性__age的值
    return __age


myPropertyWithSetter = MyPropertyWithSetter(getAge)

# <__main__.MyPropertyWithSetter object at 0x0000024ACA3C4590>
print(myPropertyWithSetter)


# @age.setter
def setAge(self, value):
    global __age
    __age = value


myPropertyWithSetter = myPropertyWithSetter.setter(setAge)
print(myPropertyWithSetter)


class Person:
    myage = myPropertyWithSetter


person = Person()

print(person.myage)
# 类级别访问不会触发描述符：`Person.myage = 29` 会直接覆盖描述符
person.myage = 29
print(person.myage)


# A object

# bases_mros=[]
#result=[A,object]

# bases_mros = [[A], [object,A]]
# A

# result = [A, object]
"""


class Person:
    def __call__(self, *args, **kwargs):
        print("实现了这个魔术方法，这个类的实例就可以当方法来调用")


person = Person()
# TypeError: 'Person' object is not callable
person()
