"""


# 定义一个“动物”类
class Animal:
    # 构造方法，初始化属性
    def __init__(self, name, sound):
        self.name = name  # 实例属性：名字
        self.sound = sound  # 实例属性：叫声

    # 实例方法：让动物发出叫声
    def make_sound(self):
        print(f"{self.name} says: {self.sound}")


# 创建对象（实例化）
cat = Animal("Cat", "Meow")
dog = Animal("Dog", "Woof")
# 调用对象方法
cat.make_sound()  # 输出: Cat says: Meow
dog.make_sound()  # 输出: Dog says: Woof



class Student:
    school = "清华大学"  # 类变量，所有实例共享

    def __init__(self, name):
        self.name = name  # 实例变量，每个实例独有


s1 = Student("小明")
s2 = Student("小红")

print(s1.school)  # 输出: 清华大学
print(s2.school)  # 输出: 清华大学
print(s1.name)  # 输出: 小明
print(s2.name)  # 输出: 小红

Student.school = "北京大学"  # 修改类变量，所有实例受影响
print(s1.school)  # 输出: 北京大学
print(s2.school)  # 输出: 北京大学



# 非数据描述符，都有一个 __get__ 方法
class my_classmethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, objtype=None):
        def wrapper(*args, **kwargs):
            return self.func(objtype, *args, **kwargs)

        return wrapper


# 但是类是什么时候传进去的呀 objtype owner


class my_staticmethod:
    def __init__(self, func):
        self.func = func

    def __get__(self):
        return self.func


class Example:
    # 类变量
    count = 0

    def __init__(self, name):
        self.name = name
        Example.count += 1

    # 1.实例方法(可以访问实例属性和方法)
    def show_name(self):
        print(f"我的名字叫{self.name}")

    # 2.类方法 可以访问类属性，不能访问实例属性
    @my_classmethod
    def how_many(cls):
        print(f"已经创建了{cls.count}个Example实例")

    # 3.静态方法，与类/实例无关
    @staticmethod
    def say_hi():
        print(f"你好，这是一条对对象和类无关的问候")


# 类方法和静态方法只是有没有参数的区别吗
# 从语法层面来说类方法和静态方法的区别在于是否有cls参数
# 从使用的角度来说区别在于类方法依赖类，静态方法不依赖当前类

e1 = Example("小明")
e2 = Example("小红")
e1.show_name()
e2.show_name()
Example.how_many()
e1.how_many()
Example.say_hi()
e1.say_hi()
# 实例可以访问实例方法  类方法 和静态方法



# 定义一个名为 Person 的类
class Person:
    # 构造方法：初始化姓名与年龄，并派生邮箱
    def __init__(self, name, age):
        # 保存姓名
        self.name = name
        # 保存年龄
        self.age = age
        # 派生出邮箱字段
        self.email = f"{name.lower()}@example.com"

    # 定义自我介绍实例方法
    def introduce(self):
        # 打印姓名与年龄
        print(f"大家好，我叫{self.name}，今年{self.age}岁。")
        # 打印邮箱
        print(f"我的邮箱是：{self.email}")

    # 定义生日方法，年龄 +1
    def have_birthday(self):
        # 年龄自增
        self.age += 1
        # 打印生日祝贺
        print(f"生日快乐！{self.name}现在已经{self.age}岁了。")


# 创建两个对象并调用方法
p1 = Person("张伟", 30)
p2 = Person("王芳", 25)
p1.introduce()
p2.introduce()
p1.have_birthday()
p1.introduce()



class Demo:
    def __new__(cls, *args, **kwargs):
        print(cls)  # <class '__main__.Demo'>
        print(f"执行__new__创建实例对象")
        print(super())  # <super: <class 'Demo'>, <Demo object>>
        instance = super().__new__(cls)
        print(instance)  # <__main__.Demo object at 0x000001CE61B14590>
        print(f"执行__new__,实例已经创建,返回实例")
        return instance

    def __init__(self, x):
        print(f"执行__init__初始化实例")
        self.x = x


demo = Demo(5)
print(f"实例属性x={demo.x}")



class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):  # cls=Singleton
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("正在创建唯一的实例对象")
        else:
            print("直接返回已经存在的实例对象")
        return cls._instance

    def __init__(self, value):  # self=instance 实例
        self.value = value


s1 = Singleton(1)
print(s1.value)
s2 = Singleton(2)
print(s1.value, s2.value)
print(s1 is s2)



# 修改类变量会影响所有实例，
# 但如果通过实例.变量赋新值，只会给该实例新建同名实例变量，不影响类变量
class Dog:
    species = "家犬"  # 类变量，所有狗都属于家犬
    total = 0  # 记录已创建的狗的总数

    def __init__(self, name, age):
        self.name = name  # 实例变量，狗的名字
        self.age = age  # 实例变量，狗的年龄
        Dog.total += 1  # 每创建一个实例，总数加一


dog1 = Dog("旺财", 2)
dog2 = Dog("小黑", 5)
Dog.species = "犬"
print(dog1.species)
dog1.species = "大狗"
print(dog1.species)
print(dog2.species)



class Person:
    def __init__(self, name):
        self._name = name  # 受保护属性


p = Person("张三")
print(p._name)  # 仍能访问，但不推荐


class Secret:
    def __init__(self, secret):
        self.__secret = secret  # 私有属性


s = Secret("abc123")
# AttributeError: 'Secret' object has no attribute '__secret'
# print(s.__secret)  # AttributeError
print(s._Secret__secret)  # 可通过类名访问，但不推荐（仅限特殊情况）



# 非数据描述符
class MyProperty:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.getter(obj)


## 数据描述符
class MyPropertyWithSetter:
    def __init__(self, getter):
        self._getter = getter
        self._setter = None

    def __get__(self, obj, objtype):
        return self._getter(obj)

    def __set__(self, obj, value):
        self._setter(obj, value)

    def setter(self, setter_func):
        self._setter = setter_func
        return self


# 定义一个名为Student的类
class Student:
    # 初始化方法，接收年龄作为参数
    def __init__(self, age):
        # 定义一个私有属性__age并初始化为None
        self.__age = None
        # 通过age的setter方法进行验证并赋值
        self.age = age  # 调用setter校验

    # 定义age属性的getter方法，用于获取年龄
    # @property属性方法装饰器
    # @propety功能，本来就是通过描述符协议实现
    @MyPropertyWithSetter
    def age(self):
        # 返回私有属性__age的值
        return self.__age

    # 定义age属性的setter方法，用于设置年龄
    @age.setter
    def age(self, value):
        # 判断年龄是否在0到150之间
        if 0 < value < 150:
            # 如果合法，设置私有属性__age的值
            self.__age = value
        else:
            # 如果不合法，抛出异常
            raise ValueError("年龄必须在0~150之间")


# 创建一个Student对象，年龄为18
stu = Student(18)
# 打印学生的年龄，结果为18
print(stu.age)  # 18
# 修改学生的年龄为20，合法
stu.age = 20  # 合法
print(stu.age)
# 尝试将学生年龄设置为-1，抛出ValueError异常
# stu.age = -1  # ValueError




# 定义一个父类（Animal）
class Animal:
    def __init__(self, name):
        self.name = name

    # 父类方法
    def speak(self):
        print(f"{self.name} 发出叫声")


# 定义一个子类（Dog），继承于 Animal
class Dog(Animal):
    # 可添加自己的构造方法
    def __init__(self, name, breed):
        # 调用父类构造方法
        super().__init__(name)
        self.breed = breed

    # 重写父类的 speak 方法
    def speak(self):
        print(f"{self.name} 汪汪叫，我是{self.breed}")


# 创建子类对象并演示
d = Dog("小黑", "哈士奇")
d.speak()  # 输出：小黑 汪汪叫，我是哈士奇



class Animal:
    def speak(self):
        print("动物发出叫声")


class Cat(Animal):
    def speak(self):
        super().speak()  # 调用父类的 speak()
        print("猫：喵喵~")


cat = Cat()
cat.speak()
# 输出：
# 动物发出叫声
# 猫：喵喵~
# 派生类就是子类的意思


print(isinstance(cat, Cat))  # True
print(isinstance(cat, Animal))  # True
print(issubclass(Cat, Animal))  # True



## 数据描述符
class MyPropertyWithSetter:
    def __init__(self, getter):
        self._getter = getter
        self._setter = None

    def __get__(self, obj, objtype):
        return self._getter(obj)

    def __set__(self, obj, value):
        self._setter(obj, value)

    def setter(self, setter_func):
        self._setter = setter_func
        return self


# 定义一个名为Student的类
class Student:
    # 初始化方法，接收年龄作为参数
    def __init__(self, age):
        # 定义一个私有属性__age并初始化为None
        self.__age = None
        # 通过age的setter方法进行验证并赋值
        self.age = age  # 调用setter校验

    # 定义age属性的getter方法，用于获取年龄
    # @property属性方法装饰器
    # @propety功能，本来就是通过描述符协议实现
    @MyPropertyWithSetter
    def age(self):
        # 返回私有属性__age的值
        return self.__age

    # 定义age属性的setter方法，用于设置年龄
    @age.setter
    def age(self, value):
        # 判断年龄是否在0到150之间
        if 0 < value < 150:
            # 如果合法，设置私有属性__age的值
            self.__age = value
        else:
            # 如果不合法，抛出异常
            raise ValueError("年龄必须在0~150之间")


# 创建一个Student对象，年龄为18
stu = Student(18)
# 打印学生的年龄，结果为18
print(stu.age)  # 18
# 修改学生的年龄为20，合法
stu.age = 20  # 合法
print(stu.age)
# 尝试将学生年龄设置为-1，抛出ValueError异常
# stu.age = -1  # ValueError
"""


class A:
    def do(self):
        print("A")


class B(A):
    def do(self):
        print("B")
        super().do()


class C(A):
    def do(self):
        print("C")
        super().do()


class D(B, C):
    def do(self):
        print("D")
        super().do()


d = D()
d.do()
# 输出顺序如下，体现了 MRO 的查找路径：
# D
# B
# C
# A
print(D.__mro__, D.mro())
print(B.__mro__, B.mro())
print(C.__mro__, C.mro())
print(A.__mro__, A.mro())
