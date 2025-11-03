# 函数定义在下面，上面能调用吗
# fn1()

"""
def fn1():
    print("fn1")


# py 里边的类型推断怎么做， process_student_data 参数类型推断怎么做
# 类型定义 类型
# pydantic
# field not in student_info 是什么意思 在tuple里面没有？
# 就是判断在字典是有没这个属性，有没有这个key
student_info = {"a": 1, "b": 2}
if "a" in student_info:
    print("a exist")

if not "c" in student_info:
    print("c not exist")

# python有转换数字失败，然后NaN的概念吗
try:
    res = int("aaa111")
    print(res)
except (ValueError, TypeError) as error:
    # invalid literal for int() with base 10: 'aaa111'
    print(error)

# python字典能和js一样解构和key同名简写么

# 那互相调用的2个函数怎么写呢



def f2():
    print("f2")
    f1()


def f1():
    print("f1")
    f2()


f2()


student_info = {"a": 1, "b": 2}


def demo(key):
    print(student_info[key])


demo("a")

student_info = {"name": 1, "age": 2}

for item in student_info.items():
    print(item)

for key in student_info.keys():
    print(key)
for value in student_info.values():
    print(value)


(a, b) = student_info
print(a, b, student_info[a], student_info[b])


obj1 = {"a": 1}
obj2 = {"b": 2}
# 解包
obj3 = {**obj1, **obj2}
print(obj3)


arr1 = [1, 2]
arr2 = [3, 4]
arr3 = [*arr1, *arr2]
print(arr3)


arr4 = (1, 2)
arr5 = (3, 4)
arr6 = (*arr1, *arr2)
print(arr6)


students = [{"name": "1", "age": 18}, {"name": "2", "age": 28}]

# [s["score"] for s in students_with_grades]
arr = []
for student in students:
    arr.append(student["name"])
print(arr)


print([student["name"] for student in students])
# fn(位置参数，关键字参数)


grade_counts = {}
score = grade_counts.get("score", 100)
print(score)
print(grade_counts)



grade_counts = {"A": 10, "B": 20}
print(grade_counts.items())
print(", ".join([f"{grade}:{count}人" for grade, count in grade_counts.items()]))

# pyton js 连接的方法不一样 join

arr4 = ["1", "2", "3"]
print(",".join(arr4))


grade_counts = None
grade = grade_counts or 100
print(grade)


#'<' not supported between instances of 'dict' and 'dict'
arr5 = [{"a": 1, "b": 2}, {"a": 2, "b": 1}]
# lambda 1<2


def sort(item):
    return item["b"]


# arr6 = sorted(arr5, key=lambda x: x["b"], reverse=True)
arr6 = sorted(arr5, key=sort, reverse=True)
print(arr5)
print(arr6)
let arr8 = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
let result = arr8.map(item=>item.a+item.b)
console.log(result)

arr5 = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
result = [item["a"] + item["b"] for item in arr5]
print(result)


arr1 = ["A", "B", "C"]
for index, item in enumerate(arr1, 10):
    print(index, item)
# [s["score"] for s in students_with_grades if age>20]
arr = []
for student in students:
    if student["age"] > 20:
        arr.append(student["name"])
print(arr)


students = [{"name": "1", "age": 18}, {"name": "2", "age": 28}]


def filter(item):
    # 经过非常复杂的计算和判断
    return True


def getValue(item):
    # 经过非常复杂的计算和判断
    return item


# for循环，如果返回值和判断条件都比较复杂，可以写方法吗
arr2 = [getValue(s) for s in students if filter(s)]


students = [{"name": "1", "age": 18}, {"name": "2", "age": 28}]
arr1 = [1 for s in students]
print(list(arr1))
print(sum([1 for s in students]))
print(1 for s in students)
# 可迭代对象 迭代协议 迭代器 生成器函数 生成器对象


arr1 = ["A", "B", "C"]
for index, item in enumerate(arr1, 10):
    print(index, item)



def mixed_function(a, b, c, name, age):
    # 混合参数函数
    return f"位置参数: {a}, {b}, {c}, 关键字参数: {name}, {age}"


arr = [1, 2, 3]
obj = {"name": "4", "age": 5}
# print(mixed_function(a=1, b=2, c=3, name="4", age=5))
print(mixed_function(*arr, **obj))
print(mixed_function(1, 2, 3, name="4", age=5))




def mixed_function(a, b, c, name="xxxxx", age=0):
    # 混合参数函数
    return f"位置参数: {a}, {b}, {c}, 关键字参数: {name}, {age}"


result = mixed_function(2, c=1, b=3, age=30)
print(result)



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
"""


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
