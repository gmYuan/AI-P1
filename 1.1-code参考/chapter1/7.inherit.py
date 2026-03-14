"""


# 定义第一个父类 Parent1
class Parent1:
    # 构造函数，用于初始化 Parent1 实例
    def __init__(self):
        # 设置 Parent1 的属性
        self.value1 = "Parent1"

    # 定义 Parent1 类的一个方法 method1
    def method1(self):
        # 打印 Parent1 method1
        print("Parent1 method1")

    # 定义一个通用方法，用于演示方法冲突
    def common_method(self):
        # 打印 Parent1 common_method
        print("Parent1 common_method")


# 定义第二个父类 Parent2
class Parent2:
    # 构造函数，用于初始化 Parent2 实例
    def __init__(self):
        # 设置 Parent2 的属性
        self.value2 = "Parent2"

    # 定义 Parent2 类的一个方法 method2
    def method2(self):
        # 打印 Parent2 method2
        print("Parent2 method2")

    # 定义一个通用方法，用于演示方法冲突
    def common_method(self):
        # 打印 Parent2 common_method
        print("Parent2 common_method")


# 定义子类 Child，它同时继承 Parent1 和 Parent2
class Child(Parent1, Parent2):
    # 构造函数，用于初始化 Child 实例
    def __init__(self):
        # 分别调用父类构造函数
        Parent1.__init__(self)
        Parent2.__init__(self)
        # 设置 Child 的属性
        self.value3 = "Child"

    # 定义 Child 类的一个方法 method3
    def method3(self):
        # 打印 Child method3
        print("Child method3")


# 创建 Child 类的实例
child = Child()
# 调用从 Parent1 继承的 method1 方法
child.method1()
# 调用从 Parent2 继承的 method2 方法
child.method2()
# 调用 Child 自己的 method3 方法
child.method3()
# 访问从 Parent1 继承的属性
print(f"Parent1 属性: {child.value1}")
# 访问从 Parent2 继承的属性
print(f"Parent2 属性: {child.value2}")
# 访问 Child 本身的属性
print(f"Child 属性: {child.value3}")



class Parent1:
    def method(self):
        print("Parent1 method")


class Parent2:
    def method(self):
        print("Parent2 method")


class Child(Parent1, Parent2):
    def method(self):
        print("Child method")


for i, cls in enumerate(Child.__mro__):
    print(f"{i}: {cls.__name__}")
child = Child()
child.method()
print(Child.mro())



class A:
    def __init__(self):
        self.value = "A"

    def method(self):
        print("A method")


class B(A):
    def __init__(self):
        super().__init__()
        self.value = "B"

    def method(self):
        print("B method")


class C(A):
    def __init__(self):
        super().__init__()
        self.value = "C"

    def method(self):
        print("C method")


class D(B, C):
    def __init__(self):
        super().__init__()
        self.value = "D"

    def method(self):
        print("D method")


for i, cls in enumerate(D.__mro__):
    print(f"{i}: {cls.__name__}")




# 菱形继承问题示例
class Object:
    pass


class A(Object):
    def method(self):
        return "A的方法"


class B(Object):
    def method(self):
        return "B的方法"


class C(A, B):
    pass


class D(B, A):
    pass


# TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
class E(C, D):
    pass
"""



