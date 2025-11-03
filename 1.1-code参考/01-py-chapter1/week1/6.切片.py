"""
instructions = [("LOAD_CONST", 10, 20, 30, 40, 50)]
# * 类似于ts里的其它参数 rest参数    (a,b,*rest)
for op, *args in instructions:
    print(op, args)


#  要想创建一个空元组，有两种方式
t1 = ()
print(t1, type(t1))
# tuple指的元组构建函数类
t2 = tuple()
print(t2, type(t2))


t3 = (5,)
print(t3)
print((6,))

# tuple相当于包装类吗
# tuple 是一个类型
# str int float tuple list dict set
t5 = "hello"
t5 = str("hello")

t6 = (1, 2)
# 相当于对应的类型的实例创建器 或者叫工厂函数
t7 = tuple([1, 2])
print(t7)
t8 = tuple("hello")
print(t8)

t9 = int("100")
print(t9, type(t9))

#


v1 = {"name": "zhangsan"}
print(v1["name"])
print(v1.get("age", 100))
# AttributeError: 'dict' object has no attribute 'age'
# print(v1.age)


class Person:
    def __init__(self, a):
        self.a = a


p1 = Person(100)
print(p1.a)

# rasie throw
# python没有块级作用域

a = 1
if a == 1:
    b = 2
print(b)

# js 类方法(属性) 实例方法(属性)
# python 类方法(属性) 静态方法(属性) 实例方法(属性)


# id() 函数：返回对象的“身份标识”（即内存地址）。
a = 1
print(id(a))
b = 1
print(id(b))

c = []
d = []
print(id(c))
print(id(d))


def hello():
    e = 1
    print(e)
    print(c)

    def world():
        f = 1
        print(f)
        print(e)
        print(c)

    world()


hello()


g = []
print(not g)
print(g.pop())

# jjs里面 空数组是true py中 空list是false？

# 第二次运行内存地址还是原来的？不会重新执行创建过程吗

# glocal nolocal

"""

v1 = 1
print("1", v1)


def fn1():
    v1 = 2
    print("2", v1)

    def fn2():
        # nonlocal v1  # 此处要使用外层作用域内的v1
        global v1  # 此处引用的是全局作用域的v1
        v1 = 3
        print("3", v1)

    fn2()
    print("4", v1)


fn1()
print("5", v1)
