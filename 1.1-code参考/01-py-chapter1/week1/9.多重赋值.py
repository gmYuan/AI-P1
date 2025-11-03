"""
# 这是最常用的多重赋值方式
a, b, c = 1, 2, 3

# 打印变量的值以验证赋值结果
print(f"变量 a 的值: {a}")
print(f"变量 b 的值: {b}")
print(f"变量 c 的值: {c}")

# 示例2: 不同类型的数据赋值
# 可以同时为不同类型的变量赋值
name, age, height = "Alice", 25, 165.5

# 打印不同类型变量的值
print(f"\n姓名: {name}, 类型: {type(name)}")
print(f"年龄: {age}, 类型: {type(age)}")
print(f"身高: {height}, 类型: {type(height)}")

# 示例3: 更多变量的赋值
# 可以同时为更多变量赋值
x, y, z, w = 10, 20, 30, 40

# 打印更多变量的值
print(f"\n变量 x: {x}, y: {y}, z: {z}, w: {w}")

# 示例4: 混合数据类型
# 可以混合使用不同的数据类型
data = ("Python", 3.9, True, [1, 2, 3])
language, version, is_active, features = data

# 打印混合数据类型变量的值
print(f"\n语言: {language}")
print(f"版本: {version}")
print(f"是否激活: {is_active}")
print(f"特性: {features}")




# 示例1: 将变量 x, y, z 都赋值为 0
# 使用链式赋值语法
x = y = z = 0

# 打印变量的值以验证赋值结果
print(f"变量 x 的值: {x}")
print(f"变量 y 的值: {y}")
print(f"变量 z 的值: {z}")

# 示例2: 字符串相同值赋值
# 为多个字符串变量赋相同的值
first_name = last_name = middle_name = ""

# 打印字符串变量的值
print(f"\n名字: '{first_name}'")
print(f"姓氏: '{last_name}'")
print(f"中间名: '{middle_name}'")

# 示例3: 列表相同值赋值（注意：这是引用赋值）
# 为多个变量赋相同的列表值
list1 = list2 = list3 = []

# 向其中一个列表添加元素
list1.append(1)

# 打印所有列表的值（它们都指向同一个对象）
print(f"\nlist1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print(f"list1 is list2: {list1 is list2}")

# 示例4: 避免引用问题的正确做法
# 如果需要独立的列表，应该分别创建
list_a = []
list_b = []
list_c = []

# 向其中一个列表添加元素
list_a.append(1)

# 打印独立列表的值
print(f"\nlist_a: {list_a}")
print(f"list_b: {list_b}")
print(f"list_c: {list_c}")
print(f"list_a is list_b: {list_a is list_b}")



# 示例1: 从元组解包
# 定义一个元组，包含三个值
tuple_values = (4, 5, 6)

# 将元组中的值按顺序解包赋给变量 a, b, c
a, b, c = tuple_values

# 打印解包后的变量值
print(f"从元组解包: a={a}, b={b}, c={c}")

# 示例2: 从列表解包
# 定义一个列表，包含三个值
list_values = [7, 8, 9]

# 将列表中的值按顺序解包赋给变量 x, y, z
x, y, z = list_values

# 打印解包后的变量值
print(f"从列表解包: x={x}, y={y}, z={z}")

# 示例3: 从字符串解包
# 定义一个字符串
string_value = "ABC"

# 将字符串中的字符按顺序解包赋给变量
char1, char2, char3 = string_value

# 打印解包后的字符
print(f"从字符串解包: {char1}, {char2}, {char3}")

# 示例4: 从集合解包（注意：集合是无序的） js set
# 定义一个集合
set_values = {1, 2, 3}

# 将集合中的值解包赋给变量（顺序可能不同）
val1, val2, val3 = set_values

# 打印解包后的值
print(f"从集合解包: {val1}, {val2}, {val3}")

# 示例5: 从字典解包（解包的是键）
# 定义一个字典
dict_values = {"a": 1, "b": 2, "c": 3}

# 将字典中的键解包赋给变量
key1, key2, key3 = dict_values

# 打印解包后的键
print(f"从字典解包键: {key1}, {key2}, {key3}")


# 示例1: 嵌套元组解包
# 定义一个嵌套元组
nested_tuple = ((1, 2), (3, 4), (5, 6))

# 解包嵌套元组
(a, b), (c, d), (e, f) = nested_tuple

# 打印解包后的值
print(f"嵌套元组解包: a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")

# 示例2: 混合数据结构解包
# 定义一个包含不同数据类型的元组
mixed_data = ("Alice", (25, 165.5), ["Python", "Java"])

# 解包混合数据结构
name, (age, height), languages = mixed_data

# 打印解包后的值
print(f"\n姓名: {name}")
print(f"年龄: {age}, 身高: {height}")
print(f"编程语言: {languages}")

# 示例3: 部分解包
# 定义一个较长的元组
long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 只解包前三个值
first, second, third = long_tuple[:3] # [start:end:step]

# 打印部分解包的值
print(f"\n部分解包: first={first}, second={second}, third={third}")

# 示例4: 使用切片解包
# 定义一个列表
data_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 解包特定位置的值
start, *middle, end = data_list

# 打印解包后的值
print(f"\n开始: {start}")
print(f"中间: {middle}")
print(f"结束: {end}")


# 示例1: 交换两个变量的值
# 假设变量 a 的初始值为 10
a = 10
# 假设变量 b 的初始值为 20
b = 20

# 打印交换前的值
print(f"交换前: a={a}, b={b}")

# 将 b 的值赋给 a，同时将 a 的值赋给 b，实现交换
a, b = b, a

# 打印交换后的值
print(f"交换后: a={a}, b={b}")

# 示例2: 交换多个变量的值
# 定义三个变量
x, y, z = 1, 2, 3

# 打印交换前的值
print(f"\n交换前: x={x}, y={y}, z={z}")

# 交换三个变量的值（循环交换）
x, y, z = y, z, x

# 打印交换后的值
print(f"交换后: x={x}, y={y}, z={z}")

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


# 示例1: 使用临时变量交换（传统方法）
# 定义两个变量
a = 100
b = 200

# 打印交换前的值
print(f"交换前: a={a}, b={b}")

# 使用临时变量进行交换
temp = a  # 将 a 的值保存到临时变量
a = b  # 将 b 的值赋给 a
b = temp  # 将临时变量的值赋给 b

# 打印交换后的值
print(f"使用临时变量交换后: a={a}, b={b}")

# 示例2: 使用多重赋值交换（Python方法）
# 重新定义变量
a = 100
b = 200

# 打印交换前的值
print(f"\n交换前: a={a}, b={b}")

# 使用多重赋值进行交换
a, b = b, a

# 打印交换后的值
print(f"使用多重赋值交换后: a={a}, b={b}")


# 示例1: 用星号处理多余变量
# 将第一个值 1 赋给 a
# 将最后一个值 5 赋给 c
# 将中间所有剩余的值 (2, 3, 4) 收集到一个列表并赋给 b
a, *b, c = 1, 2, 3, 4, 5

# 打印解包后的值
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# 示例2: 星号在开头
# 将最后一个值 3 赋给 z
# 将前面所有剩余的值 (1, 2) 收集到一个列表并赋给 x
*x, z = 1, 2, 3

# 打印解包后的值
print(f"\n*x, z = 1, 2, 3")
print(f"x = {x}")
print(f"z = {z}")

# 示例3: 星号在中间
# 将第一个值 1 赋给 a
# 将最后一个值 3 赋给 c
# 将中间所有剩余的值 (2) 收集到一个列表并赋给 b
a, *b, c = 1, 2, 3

# 打印解包后的值
print(f"\na, *b, c = 1, 2, 3")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# 示例4: 星号在结尾
# 将第一个值 1 赋给 x
# 将后面所有剩余的值 (2, 3, 4) 收集到一个列表并赋给 y
x, *y = 1, 2, 3, 4

# 打印解包后的值
print(f"\nx, *y = 1, 2, 3, 4")
print(f"x = {x}")
print(f"y = {y}")

# 示例5: 多个星号（Python 3.5+）
# 定义两个列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 使用星号解包合并列表
merged = [*list1, *list2]

# 打印合并后的列表
print(f"\n合并列表: {merged}")

# 示例6: 星号解包字典（Python 3.5+）
# 定义两个字典
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# 使用星号解包合并字典
merged_dict = {**dict1, **dict2}

# 打印合并后的字典
print(f"合并字典: {merged_dict}")




# 示例1: 处理可变数量的参数
# 定义一个函数，接受可变数量的参数
# 1.位置参数 2 关键字参数
def process_data(*args):
    print(args)
    # 处理可变数量的参数
    if len(args) == 0:  # ()
        return "没有参数"
    elif len(args) == 1:  # (42,)
        return f"单个参数: {args[0]}"
    else:  # (1, 2, 3, 4, 5)
        return f"多个参数: {args}"


# 测试函数
print(f"无参数: {process_data()}")
print(f"单个参数: {process_data(42)}")
print(f"多个参数: {process_data(1, 2, 3, 4, 5)}")


# 示例2: 解包函数参数
# 定义一个函数，接受多个参数
def calculate_sum(a, b, c):
    # 计算三个数的和
    return a + b + c


# 定义一个包含三个值的元组
values = (10, 20, 30)

# 使用星号解包传递参数
result = calculate_sum(*values)

# 打印计算结果
print(f"\n计算结果: {result}")


# 示例3: 解包字典参数
# 定义一个函数，接受关键字参数
def create_person(name, age, city):
    # 创建人员信息
    return f"姓名: {name}, 年龄: {age}, 城市: {city}"


# 定义一个包含关键字参数的字典
person_data = {"name": "Alice", "age": 25, "city": "New York"}

# 使用星号解包传递关键字参数
# create_person({"name": "Alice", "age": 25, "city": "New York"})
# person_info = create_person(person_data)
# create_person(name="Alice",age=25,city= "New York")
person_info = create_person(**person_data)
# 打印人员信息
print(f"\n人员信息: {person_info}")


# 示例4: 混合解包
# 定义一个函数，接受位置参数和关键字参数
# 定义函数的时候顺序是定死的，只能是先是定义位置参数，再定义关键字参数
# 一旦出现一个关键字参数，后面不能再出现位置参数
def mixed_function(a, b, c, name="xxxxx", age=0):
    # 混合参数函数
    return f"位置参数: {a}, {b}, {c}, 关键字参数: {name}, {age}"


# 定义位置参数和关键字参数
positional_args = (1, 2, 3)
keyword_args = {"name": "Bob", "age": 30}

# 使用星号解包传递混合参数
# result = mixed_function(*positional_args, **keyword_args)
result = mixed_function(3, 2, 1, age=30)
# 打印结果
print(f"\n混合参数结果: {result}")

# 示例5: 解包嵌套结构
# 定义一个嵌套结构
nested_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 解包嵌套结构
first_row, *remaining_rows = nested_data

# 打印解包结果
print(f"\n第一行: {first_row}")
print(f"剩余行: {remaining_rows}")

# 进一步解包剩余行
second_row, third_row = remaining_rows
print(f"第二行: {second_row}")
print(f"第三行: {third_row}")



# 示例1: 函数返回多个值
# 定义一个函数，它返回两个坐标值
def get_coordinates():
    # 函数返回一个元组 (10, 20)
    return 10, 20


# 调用 get_coordinates 函数
# 并使用解包将返回的两个值分别赋给变量 x 和 y
x, y = get_coordinates()

# 打印解包后的坐标值
print(f"坐标: x={x}, y={y}")


# 示例2: 函数返回三个值
# 定义一个函数，返回三个值
def get_rgb_color():
    # 函数返回RGB颜色值
    return 255, 128, 64


# 调用函数并解包返回值
red, green, blue = get_rgb_color()

# 打印RGB颜色值
print(f"\nRGB颜色: R={red}, G={green}, B={blue}")


# 示例3: 函数返回列表和元组
# 定义一个函数，返回列表和元组
def get_data():
    # 函数返回列表和元组
    return [1, 2, 3], (4, 5, 6)


# 调用函数并解包返回值
numbers_list, numbers_tuple = get_data()

# 打印解包后的数据
print(f"\n列表: {numbers_list}")
print(f"元组: {numbers_tuple}")


# 示例4: 函数返回字典和字符串
# 定义一个函数，返回字典和字符串
def get_user_info():
    # 函数返回用户信息
    user_dict = {"name": "Alice", "age": 25}
    user_string = "Active User"
    return user_dict, user_string


# 调用函数并解包返回值
user_data, status = get_user_info()

# 打印解包后的用户信息
print(f"\n用户数据: {user_data}")
print(f"用户状态: {status}")


# 示例5: 函数返回可变数量的值
# 定义一个函数，根据参数返回不同数量的值
def get_values(count):
    # 根据计数返回不同数量的值
    if count == 1:
        return 42
    elif count == 2:
        return 10, 20
    elif count == 3:
        return 1, 2, 3
    else:
        return tuple(range(count))


# 测试不同数量的返回值
print(f"\n单个值: {get_values(1)}")
print(f"两个值: {get_values(2)}")
print(f"三个值: {get_values(3)}")
print(f"多个值: {get_values(5)}")

# 解包多个值
a, b, c, d, e = get_values(5)
print(f"解包五个值: a={a}, b={b}, c={c}, d={d}, e={e}")
"""

import typing


def add(a: int, b: int) -> int:
    return a + b
