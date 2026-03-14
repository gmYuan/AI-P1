"""
# 示例1: 基本元组解封装
# 定义一个包含四个元素的元组
my_tuple = (1, 2, 3, 4)

# 将元组的四个元素分别赋值给变量 a, b, c, d
a, b, c, d = my_tuple

# 打印解封装后的变量值
print(f"元组: {my_tuple}")
print(f"解封装后: a={a}, b={b}, c={c}, d={d}")

# 示例2: 不同类型数据的解封装
# 定义一个包含不同类型数据的元组
mixed_tuple = ("Alice", 25, 165.5, True)

# 将元组的元素分别赋值给不同类型的变量
name, age, height, is_student = mixed_tuple

# 打印解封装后的变量值
print(f"\n混合类型元组: {mixed_tuple}")
print(f"姓名: {name}, 类型: {type(name)}")
print(f"年龄: {age}, 类型: {type(age)}")
print(f"身高: {height}, 类型: {type(height)}")
print(f"是否学生: {is_student}, 类型: {type(is_student)}")

# 示例3: 嵌套元组解封装
# 定义一个嵌套元组
nested_tuple = ((1, 2), (3, 4), (5, 6))

# 解封装嵌套元组
(first_pair, second_pair, third_pair) = nested_tuple

# 进一步解封装每个子元组
a, b = first_pair
c, d = second_pair
e, f = third_pair

# 打印解封装后的值
print(f"\n嵌套元组: {nested_tuple}")
print(f"第一对: {first_pair} -> a={a}, b={b}")
print(f"第二对: {second_pair} -> c={c}, d={d}")
print(f"第三对: {third_pair} -> e={e}, f={f}")

# 示例4: 部分解封装
# 定义一个较长的元组
long_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# 只解封装前三个元素
first, second, third = long_tuple[:3]

# 打印部分解封装的结果
print(f"\n长元组: {long_tuple}")
print(f"前三个元素: first={first}, second={second}, third={third}")



# 示例1: 坐标处理
# 定义一个函数，返回坐标点
def get_coordinates():
    # 函数返回一个包含两个元素的元组
    return 37.7749, -122.4194


# 调用函数并解封装返回值
latitude, longitude = get_coordinates()

# 打印解封装后的坐标值
print(f"坐标解封装:")
print(f"纬度: {latitude}")
print(f"经度: {longitude}")


# 示例2: 颜色处理
# 定义一个函数，返回RGB颜色值
def get_rgb_color():
    # 函数返回RGB颜色值
    return (255, 128, 64)


# 调用函数并解封装返回值
red, green, blue = get_rgb_color()

# 打印解封装后的颜色值
print(f"\n颜色解封装:")
print(f"红色: {red}")
print(f"绿色: {green}")
print(f"蓝色: {blue}")


# 示例3: 文件信息处理
# 定义一个函数，返回文件信息
def get_file_info():
    # 函数返回文件信息
    return ("document.txt", 1024, "2024-01-01")


# 调用函数并解封装返回值
filename, size, date = get_file_info()

# 打印解封装后的文件信息
print(f"\n文件信息解封装:")
print(f"文件名: {filename}")
print(f"大小: {size} 字节")
print(f"日期: {date}")


# 示例4: 用户信息处理
# 定义一个函数，返回用户信息
def get_user_info():
    # 函数返回用户信息
    return ("Alice", "alice@example.com", 25, "Engineer")


# 调用函数并解封装返回值
name, email, age, job = get_user_info()

# 打印解封装后的用户信息
print(f"\n用户信息解封装:")
print(f"姓名: {name}")
print(f"邮箱: {email}")
print(f"年龄: {age}")
print(f"职业: {job}")


# 示例5: 数学计算
# 定义一个函数，返回计算结果
def calculate_stats(numbers):
    # 计算统计信息
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    maximum = max(numbers) if numbers else 0
    minimum = min(numbers) if numbers else 0
    return (total, count, average, maximum, minimum)


# 测试统计计算
test_numbers = [1, 2, 3, 4, 5]
total, count, average, maximum, minimum = calculate_stats(test_numbers)

# 打印解封装后的统计信息
print(f"\n统计信息解封装:")
print(f"总数: {total}")
print(f"个数: {count}")
print(f"平均值: {average:.2f}")
print(f"最大值: {maximum}")
print(f"最小值: {minimum}")


# 示例1: 基本循环解封装
# 定义一个包含学生信息的列表
students = [("Alice", 28), ("Bob", 25), ("Charlie", 30)]

# 在循环中解封装每个元组
print("学生信息:")
for name, age in students:
    # 打印每个学生的姓名和年龄
    print(f"{name} is {age} years old.")

# 示例2: 坐标点处理
# 定义一个包含坐标点的列表
coordinates = [(0, 0), (1, 1), (2, 4), (3, 9)]

# 在循环中解封装坐标点
print(f"\n坐标点:")
for x, y in coordinates:
    # 打印每个坐标点
    print(f"点 ({x}, {y})")

# 示例3: 字典项解封装
# 定义一个字典
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
#  scores.items() Object.entries

# 在循环中解封装字典项
print(f"\n成绩:")
for name, score in scores.items():
    # 打印每个学生的成绩
    print(f"{name}: {score}")

# 示例4: 嵌套结构解封装
# 定义一个包含嵌套结构的列表
nested_data = [((1, 2), (3, 4)), ((5, 6), (7, 8))]

# 在循环中解封装嵌套结构
print(f"\n嵌套结构:")
for (a, b), (c, d) in nested_data:
    # 打印每个嵌套结构
    print(f"第一组: ({a}, {b}), 第二组: ({c}, {d})")

# 示例5: 使用enumerate解封装
# 定义一个列表
items = ["apple", "banana", "cherry"]

# 使用enumerate解封装索引和值
print(f"\n带索引的项:")
for index, item in enumerate(items):
    # 打印索引和项
    print(f"{index}: {item}")

# 示例6: 使用zip解封装
# 定义两个列表
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# 使用zip解封装两个列表
print(f"\n姓名和年龄:")
for name, age in zip(names, ages):
    # 打印姓名和年龄
    print(f"{name}: {age}")

# 示例7: 使用zip解封装多个列表
# 定义三个列表
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

# 使用zip解封装三个列表
print(f"\n姓名、年龄和城市:")
for name, age, city in zip(names, ages, cities):
    # 打印姓名、年龄和城市
    print(f"{name}, {age} years old, from {city}")
"""

# 示例1: 基本扩展解封装
# 定义一个包含五个元素的元组
data = (1, 2, 3, 4, 5)

# 使用星号进行扩展解封装
# 将第一个值 1 赋给 a
# 将最后一个值 5 赋给 c
# 将中间所有剩余的值 (2, 3, 4) 收集到一个列表并赋给 middle
a, *middle, c = data

# 打印解封装后的值
print(f"原始数据: {data}")
print(f"a: {a}, middle: {middle}, c: {c}")

# 示例2: 星号在开头
# 定义一个包含三个元素的元组
data = (1, 2, 3)

# 使用星号在开头进行扩展解封装
# 将最后一个值 3 赋给 z
# 将前面所有剩余的值 (1, 2) 收集到一个列表并赋给 x
*x, z = data

# 打印解封装后的值
print(f"\n*x, z = {data}")
print(f"x: {x}, z: {z}")

# 示例3: 星号在中间
# 定义一个包含三个元素的元组
data = (1, 2, 3)

# 使用星号在中间进行扩展解封装
# 将第一个值 1 赋给 a
# 将最后一个值 3 赋给 c
# 将中间所有剩余的值 (2) 收集到一个列表并赋给 b
a, *b, c = data

# 打印解封装后的值
print(f"\na, *b, c = {data}")
print(f"a: {a}, b: {b}, c: {c}")

# 示例4: 星号在结尾
# 定义一个包含四个元素的元组
data = (1, 2, 3, 4)

# 使用星号在结尾进行扩展解封装
# 将第一个值 1 赋给 x
# 将后面所有剩余的值 (2, 3, 4) 收集到一个列表并赋给 y
x, *y = data

# 打印解封装后的值
print(f"\nx, *y = {data}")
print(f"x: {x}, y: {y}")

# 示例5: 多个星号（Python 3.5+）
# 定义两个列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 使用星号解封装合并列表
merged = [*list1, *list2]  # js [...list1,...list2]

# 打印合并后的列表
print(f"\n合并列表: {merged}")

# 示例6: 星号解封装字典（Python 3.5+）
# 定义两个字典
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# 使用星号解封装合并字典
merged_dict = {**dict1, **dict2}

# 打印合并后的字典
print(f"合并字典: {merged_dict}")


# 示例1: 基本变量交换
# 定义两个变量
x, y = 5, 10

# 打印交换前的值
print(f"交换前: x={x}, y={y}")

# 使用元组解封装交换变量值
x, y = y, x

# 打印交换后的值
print(f"交换后: x={x}, y={y}")

# 示例2: 交换多个变量
# 定义三个变量
a, b, c = 1, 2, 3

# 打印交换前的值
print(f"\n交换前: a={a}, b={b}, c={c}")

# 交换三个变量的值（循环交换）
a, b, c = b, c, a

# 打印交换后的值
print(f"交换后: a={a}, b={b}, c={c}")

# 示例3: 交换字符串变量
# 定义两个字符串变量
str1 = "Hello"
str2 = "World"

# 打印交换前的值
print(f"\n交换前: str1='{str1}', str2='{str2}'")

# 交换字符串变量的值
str1, str2 = str2, str1

# 打印交换后的值
print(f"交换后: str1='{str1}', str2='{str2}'")

# 示例4: 交换列表变量
# 定义两个列表变量
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 打印交换前的值
print(f"\n交换前: list1={list1}, list2={list2}")

# 交换列表变量的值
list1, list2 = list2, list1

# 打印交换后的值
print(f"交换后: list1={list1}, list2={list2}")

# 示例5: 交换字典变量
# 定义两个字典变量
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# 打印交换前的值
print(f"\n交换前: dict1={dict1}, dict2={dict2}")

# 交换字典变量的值
dict1, dict2 = dict2, dict1

# 打印交换后的值
print(f"交换后: dict1={dict1}, dict2={dict2}")
