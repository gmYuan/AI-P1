"""
# 如何判断是函数类型
def my_function():
    pass


class MyClass:
    def method(self):
        pass

    def __call__(self, *args, **kwds):
        return "MyClass"


str = "123"
myClass = MyClass()
# .1 如果callable返回True,它就是可以当函数调用
print(callable(my_function), my_function())
print(callable(myClass), myClass())
print(callable(str))

## 2.types
import types

lambdaFn = lambda x: x
print(isinstance(my_function, types.FunctionType))
print(isinstance(lambdaFn, types.LambdaType))

import inspect

print(inspect.isfunction(my_function))
posisition = 0
# 这是文件内容
file_content = "123\n456\n789\n"
posisition = 5
first_line = file_content[0:5]
reminder_content = file_content[5]


# 类是怎么判断来着的
print(inspect.isclass(MyClass))
print(inspect.isclass(my_function))
print(inspect.isclass(int))
print(inspect.isclass("hello"))

print(isinstance(MyClass, type))
print(isinstance(my_function, type))
print(isinstance(int, type))
print(isinstance("hello", type))

# \n对应换行符，在len就是一个
str = "abc\n"
print(len(str))
print(str.encode("utf-8"))
print(len(str.encode("utf-8")))
str = "abc中"
print(len(str))  # 算的是字符的数量，可不是字节的数量
print(str.encode("utf-8"))  # 得到的字节串
print(len(str.encode("utf-8")))
# 是不是统计字符的时候 /n算一个，但是readline的时候 指针 \n算2个是的
# 那python怎么获取字节数 先转字节串，再取字节串的长度
# 那种大文件上传，把分片存到一个临时目录中，最后合并读取还是要在内存合并吧？还是会超吧？
# 1.获取所有的分片 1 2 3 4 5 append逐步添加



import copy

l1 = [1, 2, 3]
l2 = l1.copy()
print(l2)
# 元组没有copy方法， dict set list 有copy方法
t1 = (1, 2, 3)
# t2 = t1.copy()
t3 = copy.copy(t1)  # t1和 t3内存地址是一样的
t4 = t1[:]
print(id(t1))
print(id(t3))
print(id(t4))  # 切片拷贝也是一样的

t5 = (1, 2, [3, 4])
print(t5)
t5[2][0] = 100
print(t5)

list1 = [1, 2, 3]
list2 = list1[:]
print(id(list1))
print(id(list2))

dict1 = {"a": 1, "b": 2}
print(dict1)


class Person:
    def __init__(self):
        self.name = "张三"
        self.age = 30


person = Person()
# 判断person上有没有__dict__
print(hasattr(person, "__dict__"))
print(getattr(person, "__dict__"))
# print(setattr(person.__dict__, "name", "value"))
setattr(person, "name", "123")
print(person.__dict__)
for attr, value in person.__dict__.items():
    print(attr, value)




class Person:
    def __init__(self):
        pass


p = Person()
cls = type(p)
print(cls)

p2 = Person.__new__(Person)
print(p2)


class Person:
    def __init__(self):
        self.age = 30


cls = type(Person())
result = cls.__new__(cls)
print(result.age)
result2 = cls()
print(result2.age)




class Node:
    def __init__(self):
        pass

    def add_friend(self, friend):
        self.friend = friend


node1 = Node()
node2 = Node()
node1.add_friend(node2)
node2.add_friend(node1)

list1 = []
list2 = []
list1[0] = list2
list2[0] = list1



class Node:
    def __init__(self, a):
        self.a = a


node1 = Node(1)
print(hasattr(node1, "a"))
print(node1.a)

dict1 = {"a": 1}
# AttributeError: 'dict' object has no attribute 'a'
# print(dict1.a)
print(hasattr(dict1, "a"))
# 字典的取值用方括号或者 get
print(dict1["a"])
print(dict1.get("a"))
# 类的实例也就是对象的取值用.或者 getattr
print(node1.a)
# print(node1["a"])#TypeError: 'Node' object is not subscriptable
print(node1.__dict__["a"])
print(getattr(node1, "a"))

# tuple1 = (1, 2, 3)
# print(hasattr(tuple1, 1))
"""

numbers = ["a", "b", "c"]
dict1 = {item: item for item in numbers}
print(dict1)


# s = "['a', 1, 'b', 2, 'c', 3]"
# lst = eval(s)

lst = ["a", 1, "b", 2, "c", 3]
dct = {}
for i in range(0, len(lst), 2):
    dct[lst[i]] = lst[i + 1]
print(dct)


message = "用户 {} 登录成功 {} "
args = ("Alice", "2")
print(message.format(*args))


def wrapper(*args, **kwargs):
    pass


def register():
    print("register")


wrapper.register = register

wrapper.register()
