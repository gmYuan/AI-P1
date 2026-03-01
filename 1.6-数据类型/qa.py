
"""
# 1.6-1 函数定义在下面，上面能调用吗- 不能
fn1()

def fn1():
    print("fn1")
"""


"""------------------------------------------------------------------------
# 1.6-2 py 里边的类型推断怎么做， process_student_data 参数类型推断怎么做

# 后面会讲：
# 类型定义 类型
# pydantic
"""


"""------------------------------------------------------------------------
# 1.6-3 field not in student_info 是什么意思 在tuple里面没有？

# 就是判断 在字典里 有没这个属性，有没有这个key ==> 属性存在判断
student_info = {"a": 1, "b": 2}

if "a" in student_info:
    print("a exist")

if not "c" in student_info:
    print("c not exist")
"""


"""------------------------------------------------------------------------
# 1.6-4 python有转换数字失败，然后NaN的概念吗: 没有，会直接报错

try:
    res = int("aaa111")
    print(res)
except (ValueError, TypeError) as error:
    print(error)   # invalid literal for int() with base 10: 'aaa111'

"""


"""------------------------------------------------------------------------
# 1.6-5 python字典能和js一样解构和key同名简写么
# answer:  可以的，后续介绍


# 那互相调用的2个函数怎么写呢

def f2():
    print("f2")
    f1()

def f1():
    print("f1")
    f2()

f2()  # answer: 会死循环

"""


"""------------------------------------------------------------------------
# 1.6-6 展开运算符/ 解包(字典的解构赋值)

student_info = {"a": 1, "b": 2}

def demo(key):
    print(student_info[key])

demo("a")


# ans: 在 py 里，实现方法一般是通过 for 循环

student_info = {"name": 1, "age": 2}

for item in student_info.items():
    print(item)

for key in student_info.keys():
    print(key)

for value in student_info.values():
    print(value)


# ans: 这种写法可以拿到字典的 key
(a, b) = student_info
print(a, b, student_info[a], student_info[b])



obj1 = {"a": 1}
obj2 = {"b": 2}

# ans: 对象的 展开/解包
obj3 = { **obj1, **obj2 }
print(obj3)


# ans: 列表的 展开/解包
arr1 = [1, 2]
arr2 = [3, 4]
arr3 = [*arr1, *arr2]
print(arr3)


# ans: 元组的 展开/解包
arr4 = (1, 2)
arr5 = (3, 4)
arr6 = (*arr1, *arr2)
print(arr6)


students = [{"name": "1", "age": 18}, {"name": "2", "age": 28}]
"""


"""------------------------------------------------------------------------
# 1.6-7 列表生成式（列表推导式）


# ans1: 可以用来 快速创建一个新列表
# [s["score"] for s in students_with_grades]


# ans2: 等价于 下面的写法：
arr = []
for student in students:
    arr.append(student["name"])
print(arr)

# 即
print([student["name"] for student in students])


# fn(位置参数，关键字参数)
"""


"""------------------------------------------------------------------------
# 1.6-8 对象val的 后备值
 
grade_counts = {}
score = grade_counts.get("score", 100)
print(score)
print(grade_counts)
"""


"""------------------------------------------------------------------------
# 1.6-10 变量的 后备值

grade_counts = None
grade = grade_counts or 100
print(grade)
"""



"""------------------------------------------------------------------------
# 1.6-9 grade_counts.items() + join使用

grade_counts = {"A": 10, "B": 20}

print(grade_counts.items())  # (A, 10), (B, 20)

print([f"{grade}:{count}人" for grade, count in grade_counts.items()])

print(", ".join([f"{grade}:{count}人" for grade, count in grade_counts.items()]))

# pyton js 连接的方法不一样 join

arr4 = ["1", "2", "3"]
print(",".join(arr4))
"""


"""------------------------------------------------------------------------
# 1.6-9.2 类似于 JS 的 map效果

# let arr8 = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
# let result = arr8.map(item=>item.a+item.b)
# console.log(result)

arr5 = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
result = [item["a"] + item["b"] for item in arr5]
print(result)
"""



"""------------------------------------------------------------------------
# 1.6-11 sort

arr5 = [{"a": 1, "b": 2}, {"a": 2, "b": 1}]
# arr6 = sorted(arr5, key=lambda x: x["b"], reverse=True)
# print(arr5)
# print(arr6)

# 如果没有 key，直接用 sort排序字典
# 会报错  '<' not supported between instances of 'dict' and 'dict'


# 另一种写法：
def sort(item):
    return item["b"]

arr6 = sorted(arr5, key=sort, reverse=True)
print(arr5)
print(arr6)
"""



"""------------------------------------------------------------------------
# 1.6-12 enumerate

arr1 = ["A", "B", "C"]
for index, item in enumerate(arr1, 10):
    print(index, item)
    
"""


"""------------------------------------------------------------------------
# 1.6-13 类似于 JS 的 filter效果

# [s["name"] for s in students_with_grades if age>20]

arr = []
for student in students:
    if student["age"] > 20:
        arr.append(student["name"])
print(arr)
"""


"""------------------------------------------------------------------------
# 1.6-14 for循环，如果返回值和判断条件都比较复杂，可以写方法吗- 可以

students = [{"name": "1", "age": 18}, {"name": "2", "age": 28}]

def filter(item):
    # 经过非常复杂的计算和判断
    return True

def getValue(item):
    # 经过非常复杂的计算和判断
    return item

# for循环，如果返回值和判断条件都比较复杂，可以写方法吗
arr2 = [getValue(s) for s in students if filter(s)]
"""


"""------------------------------------------------------------------------
# 1.6-15 可迭代对象 迭代协议 迭代器；  生成器函数 生成器对象
# 后面会详细讲

students = [{"name": "1", "age": 18}, {"name": "2", "age": 28}]
arr1 = [1 for s in students]

print(list(arr1))

print(sum([1 for s in students]))

print(1 for s in students)
"""


students = [{"name": "1", "age": 18}, {"name": "2", "age": 28}]
arr1 = [1 for s in students]
# print(list(arr1))
print(sum([1 for s in students]))
print(1 for s in students)



"""------------------------------------------------------------------------
# 1.6-16 enumerate
"""

arr1 = ["A", "B", "C"]
for index, item in enumerate(arr1, 10):
    print(index, item)