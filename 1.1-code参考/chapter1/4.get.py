"""
class Person:
    # 定义构造函数
    def __init__(self, name, age):
        # 初始化name属性
        self.name = name
        self.age = age


# 创建Person实例
person = Person("Alice", 25)
# {'name': 'Alice', 'age': 25}
print(person.__dict__)
# 普通属性：存/取时直连实例字典（instance.__dict__）。 实例字典指的是每个对象自身的属性存储空间
print(person.name)
person.age = 35
print(person.age)
# 描述符属性：存/取会间接调用该属性的特殊方法（由类级描述符对象代理）。
# __get__(self, instance, owner=None)  # 读取属性时执行
# __set__(self, instance, value)       # 设置属性时执行
# __delete__(self, instance)           # 删除属性时执行
# 同时有 __get__ & __set__ ：数据描述符(Data Descriptor)（如 property, @property装饰器）
# 只有 __get__ ：非数据描述符(Non-data Descriptor)（如普通函数、类方法、静态方法）



# 这是一个数据描述符类
class DataDescriptor:
    def __init__(self, initial_value=None):
        self._value = initial_value

    def __get__(self, instance, owner):
        print(f"Getting value:{self._value}")
        return self._value

    def __set__(self, instance, value):
        print(f"Setting value to :{value}")
        self._value = value


class MyClass:
    attr = DataDescriptor("初始值")
    age = 25


obj = MyClass()
# 访问attr属性，触发__get__方法，会输出
print(obj.attr)
obj.attr = "新的值"



# 只有 __get__ ：非数据描述符(Non-data Descriptor)
class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "只读虚拟值"


class MyClass:
    nd = NonDataDescriptor()


obj = MyClass()
print(obj.nd)



# 属性查找优先级
# 1. 数据描述符（定义了 __set__）
# 2. 实例字典（instance.__dict__）
# 非数据描述符（仅有 __get__）
# 类字典/父类字典
# __getattr__
class DataDescriptor:
    def __init__(self, initial_value=None):
        self._value = initial_value

    def __get__(self, instance, owner):
        print(f"Getting value:{self._value}")
        return self._value

    def __set__(self, instance, value):
        print(f"Setting value to :{value}")
        self._value = value


class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "非数据描述符"


class Parent:
    parent_attr = "父类字典上的属性"


class MyClass(Parent):
    attr = DataDescriptor("数据描述符")
    attr1 = "实例字典"
    attr2 = NonDataDescriptor()

    # 定义属性访问方法
    # 这是一个魔术方法，当访问对象中不存在属性的时候会调用
    def __getattr__(self, name):
        # 当访问不存在的属性时调用
        print(f"访问不存在的属性: {name}")
        # 返回默认值
        return None


obj = MyClass()
print(obj.attr)
print(obj.attr1)
print(obj.attr2)
print(obj.parent_attr)
print(obj.noattr)



class DemoObj:
    def __init__(self, v):
        self._v = v

    # 使用@property装饰器，将v方法变成属性
    # @property其实就是一个非数据描述符
    @property
    def v(self):
        print(f"触发property __get__")
        return self._v


d = DemoObj(60)
print(d.v)


import types


class Animal:
    pass


def say_hi(self):
    return f"Hi! I am {self.name}"


def get_age(self):
    return f"Hi! I am {self.age} years old"


duck = Animal()
duck.name = "鸭鸭"
duck.age = 60
# TypeError: say_hi() missing 1 required positional argument: 'self'
# duck.say_hi = say_hi
# duck.get_age = get_age
# duck.say_hi = types.MethodType(say_hi, duck)
# types.MethodType(f,obj) 等价于 f.__get__(obj,type(obj))
# __get__的使用就是让say_hi的第一个参数永远绑定为duck
duck.say_hi = say_hi.__get__(duck, Animal)
print(duck.say_hi())


# 动态给类/实例添加方法对比 如果是类名赋值Animal.say_hi = say_hi就不用传了吧
import types


class Cat:
    pass


def meow(self):
    return f"{self.name} 喵喵..."


cat1, cat2 = Cat(), Cat()
cat1.name, cat2.name = "小白", "小黑"
# 如果给实例添加属性的话，只针对当前的实例生效，其它的实例不受影响
# cat1.speak = types.MethodType(meow, cat1)
cat1.speak = meow.__get__(cat1)
# cat2.speak = types.MethodType(meow, cat2)
# 如果给类添加方法属性的话，会针对所有的实例生效，而且可以自动绑定各自的实例
# Cat.speak = meow
print(cat1.speak())
# print(cat2.speak())
# 在python 有实例属性 类属性 静态属性


# Python的所有函数本身都是非数据描述符，都有一个 __get__ 方法，这让“函数作为类属性”时，
# 能在读取时自动变成“绑定方法”。


def intro(self, age):
    return f"我是{self.name},今年{age}"


class P:
    pass


p = P()
p.name = "张三"
p.intro = intro


# p.intro()
# class Function:
#    def __get__(self, instance, owner):
#        return "非数据描述符"

# import types


def MethodType(func, instance):
    def boundFunc(*args, **kwargs):
        return func(instance, *args, **kwargs)

    return boundFunc


# Python的所有函数本身都是非数据描述符，都有一个 __get__ 方法
def __get__(self, instance):
    if instance is None:
        return self
    return MethodType(self, instance)


intro.__get__ = __get__
# p.intro = intro.__get__(p)
p.intro = intro.__get__(intro, p)
print(p.intro(25))



class Cat:
    pass


def meow(self):
    return f"{self.name} 喵喵..."


cat1, cat2 = Cat(), Cat()
cat1.name, cat2.name = "小白", "小黑"
# Python中在执行下面这个行代码的时候会进行自动包
Cat.speak = meow
# 在通过实例调用类上的方法的时候会进行自动转换再执行
print(cat1.speak())
# function.__get__ 是最核心的自动装配机制：让函数+实例→绑定方法。
print(cat1.speak.__get__(cat1)())
# types.MethodType 提供了自己“动态装配”的能力。
print(cat2.speak.__get__(cat2)())
# 内部执行步骤
# 1.由于函数实现了__get__方法，后续通过实例访问的话会触发描述符协议



# __slots__是一个类变量，用于显示声明类允许的属性
class SlotClass:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = SlotClass("Bob", 25)
print(hasattr(obj, "__dict__"))
# AttributeError: 'SlotClass' object has no attribute 'home' and no __dict__ for setting new attributes
obj.home = "北京"
"""
