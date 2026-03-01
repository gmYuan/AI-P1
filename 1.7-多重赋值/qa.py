

"""
# -------------------------------------------------------------------------------
# 1.7-4.2 高级 *星号解包 ==> 函数的 位置参数 和 关键字参数1

def mixed_function(a, b, c, name, age):
    # 混合参数函数
    return f"位置参数: {a}, {b}, {c}, 关键字参数: {name}, {age}"

arr = [1, 2, 3]
obj = {"name": "4", "age": 5}
# 相当于 print(mixed_function(a=1, b=2, c=3, name="4", age=5))
print(mixed_function(*arr, **obj))


# 1.7-4.2 高级 *星号解包 ==> 函数的 位置参数 和 关键字参数2

def mixed_function(a, b, c, name="xxxxx", age=0):
    # 混合参数函数
    return f"位置参数: {a}, {b}, {c}, 关键字参数: {name}, {age}"


result = mixed_function(2, c=1, b=3, age=30)
print(result)
"""



"""
# -------------------------------------------------------------------------------
# 1.7-x todo




"""



print(int(True))
print(int(False))

print(bool(1))
print(bool(0))


t = (1, 1)
# list set dict 都不能作为字典的key或者字典的属性
l = []  # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d = {l: 1}


# 一般来说创建空的容器类实例都有两种方式
l1 = []
l2 = list()
t1 = ()
t2 = tuple()
# s1 = {}
s2 = set()
d1 = {}
d2 = dict()


my_list = [1, 2, 2, 3, 3, 4]
unique_set = set(my_list)
print(unique_set)  # {1, 2, 3, 4}

# unique_set.remove(5)
unique_set.discard(5)
import re


int_c = 5
int_d = 6
print(id(int_c))
print(id(int_d))
print(f"int_c is int_d: {int_c is int_d}")


print("ab" * 10)
# 所以通常只在比较None、True、False等单例对象时使用is】 ,True False为什么用is呢
print(id(None))
print(id(None))
print(id(True))
print(id(True))
print(id(False))
print(id(False))


str = "10"
print(int(str, 2))
print(int(str, 8))
print(int(str, 10))
print(int(str, 16))

print(255 % 16)
print(255 / 16)  # 15.9375
print(255 // 16)  # 15


print(type("hello"))  # <class 'str'>



char = "中"
print(ord(char))
print(char.encode("utf-8"))

char_unicode = 255  # FF
print(f"U+{char_unicode:04X}")


print(len("中"))

char = "中"
print(len(char))
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 6-7: ordinal not in range(128)
# 如果遇到不识别无法编码的字符就替换成?
print("Hello 世界".encode("ascii", errors="replace"))



class Person:
    def __str__(self):
        return f"学生"


p = Person()
# <__main__.Person object at 0x0000020D4C074590>
print(p)


from collections import namedtuple

# 定义一个Person具名元组类，包含4个字段：name, age, city, job
Person = namedtuple("Person", ["name", "age", "city", "job"])
person = Person("Alice", 25, "New York", "Engineer")
#'Person' object does not support item assignment
# person[0] = "Bob"
# AttributeError: can't set attribute
# person.age = 35
new_person = person._replace(age=35, name="Bob")
print(new_person)
print(person)





text_with_whitespace = "apple   orange\tbanana\ncherry"
space_split = text_with_whitespace.split(" ")
print("指定空格分割:", space_split)

# 3个连续空格，第一个视为分割符，没了，
# 第二个是被分割的保留了，
# 那为啥第三个为什么没有被视为分隔符，而是被保留了，

text_with_whitespace = "apple,,,orange\tbanana\ncherry"
space_split = text_with_whitespace.split(",")
print("指定,分割:", space_split)

print(",".join("a,b,c".split(",")))


print(",a,,,b".split(","))  # ['', 'a', '', '', 'b']

"""