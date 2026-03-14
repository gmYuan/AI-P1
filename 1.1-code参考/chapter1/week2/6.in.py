"""
# 示例1: 字符串中的字符检查
# 检查字符 'a' 是否在字符串 'banana' 中
print(f"'a' in 'banana': {'a' in 'banana'}")  # 输出: True

# 示例2: 列表中的元素检查
# 检查数字 1 是否在列表 [1, 2, 3] 中
print(f"1 in [1, 2, 3]: {1 in [1, 2, 3]}")  # 输出: True

# 示例3: 元组中的元素检查
# 检查数字 2 是否在元组 (1, 2, 3) 中
print(f"2 in (1, 2, 3): {2 in (1, 2, 3)}")  # 输出: True

# 示例4: 集合中的元素检查
# 检查数字 3 是否在集合 {1, 2, 3, 4, 5} 中
print(f"3 in {{1, 2, 3, 4, 5}}: {3 in {1, 2, 3, 4, 5}}")  # 输出: True


# 示例1: 字符串中的字符检查
# 检查字符 'a' 是否不在字符串 'banana' 中
print(f"'a' not in 'banana': {'a' not in 'banana'}")  # 输出: False

# 示例2: 列表中的元素检查
# 检查数字 1 是否不在列表 [1, 2, 3] 中
print(f"1 not in [1, 2, 3]: {1 not in [1, 2, 3]}")  # 输出: False

# 示例3: 元组中的元素检查
# 检查数字 2 是否不在元组 (1, 2, 3) 中
print(f"2 not in (1, 2, 3): {2 not in (1, 2, 3)}")  # 输出: False

# 示例4: 集合中的元素检查
# 检查数字 3 是否不在集合 {1, 2, 3, 4, 5} 中
print(f"3 not in {{1, 2, 3, 4, 5}}: {3 not in {1, 2, 3, 4, 5}}")  # 输出: False


# 定义一个字典
d = {"a": 1, "b": 2, "c": 3}
print(f"字典 d: {d}")

# 示例1: 检查键是否存在
# 检查键 'a' 是否在字典 d 中
print(d.keys())  # [a,b,c]
print(f"'a' in d: {'a' in d}")  # 输出: True
print(f"'a' in d: {'a' in d.keys()}")  # 输出: True
# 示例2: 检查值是否在字典的值中
# 要检查值是否在字典的值中，需要使用 d.values()
print(d.values())  # [1,2,3]
print(f"1 in d.values(): {1 in d.values()}")  # 输出: True

# 示例3: 检查键值对是否存在
# 检查键值对 ('a', 1) 是否在字典 d 的 items() 中
print(d.items())  # [(a,1),(b,2),(c,3)]
print(f"('a', 1) in d.items(): {('a', 1) in d.items()}")  # 输出: True


# 定义一个集合
s = {1, 2, 3, 4, 5}
print(f"集合 s: {s}")

# 示例1: 检查元素是否存在
# 检查数字 3 是否在集合 s 中
print(f"3 in s: {3 in s}")  # 输出: True

# 示例2: 检查元素是否不存在
# 检查数字 4 是否不在集合 s 中
print(f"4 not in s: {4 not in s}")  # 输出: False
"""


# 定义一个名为 MyClass 的类
class MyClass:
    # 类的初始化方法，接收一个数据列表
    def __init__(self, data):
        # 将传入的数据存储为实例属性
        self.data = data

    # 定义 __contains__ 魔法方法，使其支持 in 和 not in 运算符
    def __contains__(self, item):
        # 检查 item 是否存在于实例的 data 属性中
        return item in self.data

    # 定义字符串表示方法
    def __str__1(self):
        return f"MyClass __str__"

    # 定义字符串表示方法
    def __repr__1(self):
        return f"MyClass __repr__"


# 创建 MyClass 的一个实例，并传入列表 [1, 2, 3]
obj = MyClass([1, 2, 3])
print(f"自定义对象 obj: {obj}")

print(str(obj))
print(obj)
print(repr(obj))  # <__main__.MyClass object at 0x00000232B77C4590>
print(dir(obj))
# 检查数字 2 是否在 obj 对象中 (通过 __contains__ 方法实现)
print(f"2 in obj: {2 in obj}")  # 输出: True
print(f"2 in obj: {obj.__contains__(2)}")

# 检查数字 4 是否不在 obj 对象中 (通过 __contains__ 方法实现)
print(f"4 not in obj: {4 not in obj}")  # 输出: True
print(f"4 not in obj: {not obj.__contains__(4)}")
# __repr__ 和__str__什么区别 用的地方不一样


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 此方法的返回值是给用户看的，返回是一些更适合用户观看的信息
        return f"{self.name} is {self.age} years old"

    def __repr__(
        self,
    ):  # 此方法的返回值是给程序员调试的时候看到,更多是返回内部的属性的状态，给程序员看的
        return f"Person('{self.name}', {self.age})"


p = Person("Alice", 30)

print(str(p))  # 输出: Alice is 30 years old
print(repr(p))  # 输出: Person('Alice', 30)
