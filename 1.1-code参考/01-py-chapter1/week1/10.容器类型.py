"""
# 创建列表
# 创建一个包含不同类型元素的列表
my_list = [1, 2, 3, "hello", True, 3.14]
print(my_list)
# 访问元素
# 通过索引访问第一个元素
first_element = my_list[0]
print(first_element)
# 通过负索引访问最后一个元素
last_element = my_list[-1]
print(last_element)
# 切片操作
# 获取索引1到3的元素（不包含索引3）
slice_result = my_list[1:3]  # js slice(1,3)
print(slice_result)
# 添加元素
# 在列表末尾添加元素
my_list.append("world")  # js push()
print(my_list)
# 在指定位置插入元素
my_list.insert(1, "inserted")
print(my_list)
# 删除元素
# 删除指定值的元素
my_list.remove("hello")  # ValueError: list.remove(x): x not in list
print(my_list)
# 删除指定索引的元素并返回
popped_element = my_list.pop(1)
print(popped_element)
my_list = [5, 1, 3, 2, 4]
# 对列表进行排序
my_list.sort()
print(my_list)
# 反转列表
my_list.reverse()  # js arr.reverse()
print(my_list)
# 获取列表长度
length = len(my_list)
print(length)


# 创建元组
# 创建一个包含不同类型元素的元组
my_tuple = (1, 2, 3, "hello", True)
print(my_tuple)  # (1, 2, 3, 'hello', True)
# 单个元素的元组需要加逗号
# 注意：单个元素的元组必须在元素后加逗号
single_tuple = (42,)  # (42,)
print(single_tuple)
# 访问元素
# 通过索引访问元素
first_element = my_tuple[0]
print(first_element)  # 1
# 通过负索引访问元素
last_element = my_tuple[-1]
print(last_element)  # True
# 切片操作
# 获取索引1到3的元素
slice_result = my_tuple[1:3]
print(slice_result)  # (2, 3)
# 元组解包
# 将元组中的元素分别赋值给变量
a, b, c = my_tuple[:3]
print(a, b, c)  # 1 2 3
# 元组作为字典的键
# 创建以元组为键的字典
coordinates = {(0, 0): "origin", (1, 1): "diagonal"}
print(coordinates)  # {(0, 0): 'origin', (1, 1): 'diagonal'}

# 查找元素索引
index = my_tuple.index("hello")
print(index)  # 3
# 统计元素出现次数
# 常用方法
print("my_tuple", my_tuple)
count = my_tuple.count(1)
print(count)  # 2
# 获取元组长度
length = len(my_tuple)
print(length)  # 5

# 创建集合 就相当于JS中的set HashSet
# 创建一个包含不同元素的集合
my_set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

# 空集合必须使用set()，不能用{}
# 因为{}表示空字典
empty_set = set()
print(empty_set)  # set()
# 从列表创建集合（去重）
# 将列表转换为集合以去除重复元素
my_list = [1, 2, 2, 3, 3, 4]
unique_set = set(my_list)
print(unique_set)  # {1, 2, 3, 4}
# 添加元素
# 向集合中添加单个元素
my_set.add(6)  # list append  js push   , add js add
print(my_set)  # {1, 2, 3, 4, 5, 6}
# 向集合中添加多个元素
my_set.update([7, 8, 9])
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 删除元素
# 删除指定元素（如果不存在会报错）
my_set.remove(5)
print(my_set)  # {1, 2, 3, 4, 6, 7, 8, 9}
# 删除指定元素（如果不存在不会报错）
my_set.discard(10)
print(my_set)  # {1, 2, 3, 4, 6, 7, 8, 9}
# 随机删除并返回一个元素
popped_element = my_set.pop()
print(popped_element)  # 1
# 集合运算
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 并集
# 两个集合的所有元素
union_result = set1 | set2
print(union_result)  # {1, 2, 3, 4, 5, 6}
# 交集
# 两个集合的共同元素
intersection_result = set1 & set2
print(intersection_result)  # {3, 4}
# 差集
# 在set1中但不在set2中的元素
difference_result = set1 - set2
print(difference_result)  # {1, 2}
# 对称差集
# 两个集合中不同时存在的元素
symmetric_difference = set1 ^ set2
print(symmetric_difference)  # {1, 2, 5, 6}
# 成员测试
# 检查元素是否在集合中
is_member = 3 in my_set
print(is_member)  # True
# 常用方法
# 清空集合
my_set.clear()
print(my_set)  # set()
# 获取集合长度
length = len(my_set)
print(length)  # 0


# 创建字典
# 创建一个包含不同类型键值对的字典
my_dict = {"name": "张三", "age": 25, "city": "北京", "hobbies": ["读书", "游泳"]}

# 空字典
# 创建一个空字典
empty_dict = {}

# 访问元素
# 通过键访问值
name = my_dict["name"]
# name1 = my_dict["name1"]
# 使用get方法访问（如果键不存在返回None）
age = my_dict.get("age")

# 使用get方法设置默认值
salary = my_dict.get("salary", 0)

# 添加/修改元素
# 添加新的键值对
my_dict["salary"] = 8000

# 修改现有键的值
my_dict["age"] = 26

# 删除元素
# 删除指定键值对
del my_dict["city"]

# 删除并返回指定键的值
popped_value = my_dict.pop("age")

# 删除并返回最后一个键值对
last_item = my_dict.popitem()
print(last_item)
# 遍历字典
# 遍历所有键
for key in my_dict.keys():
    print(f"键: {key}")

# 遍历所有值
for value in my_dict.values():
    print(f"值: {value}")

# 遍历所有键值对
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 常用方法
# 检查键是否存在
has_key = "name" in my_dict
print(has_key)

# 获取所有键
keys = my_dict.keys()

# 获取所有值
values = my_dict.values()

# 获取所有键值对
items = my_dict.items()

# 清空字典
my_dict.clear()

# 复制字典
new_dict = my_dict.copy()

# 获取字典长度
length = len(my_dict)


my_dict = {"1": "张三", "5": 25, "3": "北京"}
print(my_dict.keys())
my_dict["2"] = 2
last_item = my_dict.popitem()
print(last_item)
print(my_dict.keys())
my_dict["0"] = 0
print(my_dict.keys())
last_item = my_dict.popitem()
print(last_item)
"""

# 创建字符串
# 创建不同类型的字符串
single_quote = "单引号字符串"
double_quote = "双引号字符串"
triple_quote = """三引号字符串
可以跨多行"""

# 字符串连接
# 使用+号连接字符串
name = "张三"
greeting = "你好, " + name + "!"

# 使用join方法连接字符串列表
words = ["Hello", "World", "Python"]
joined = " ".join(words)
print(joined)  # Hello World Python
# 字符串分割
# 使用split方法分割字符串
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'orange']
# 字符串查找和替换
# 查找子字符串位置
text = "Hello World"
position = text.find("World")
print(position)  # 6
# 替换字符串
new_text = text.replace("World", "Python")
print(new_text)  # Hello Python
# 字符串格式化
name = "张三"
age = 25

# 使用f-string格式化
formatted1 = f"姓名: {name}, 年龄: {age}"  # 模板字符串
print(formatted1)  # 姓名: 张三, 年龄: 25
# 使用format方法格式化
formatted2 = "姓名: {}, 年龄: {}".format(name, age)
print(formatted2)  # 姓名: 张三, 年龄: 25
# 字符串大小写转换
text = "Hello World"
# 转换为小写
lower_text = text.lower()
print(lower_text)  # hello world

# 转换为大写
upper_text = text.upper()
print(upper_text)  # HELLO WORLD
# 首字母大写
title_text = text.title()
print(title_text)  # Hello World
# 字符串检查
# 检查是否为数字
is_digit = "123".isdigit()
print(is_digit)  # True
# 检查是否为字母
is_alpha = "hello".isalpha()
print(is_alpha)  # True
# 检查是否以指定字符串开头
starts_with = text.startswith("Hello")
print(starts_with)  # True
# 检查是否以指定字符串结尾
ends_with = text.endswith("World")
print(ends_with)  # True
# 字符串切片
# 获取前5个字符
first_five = text[:5]
print(first_five)  # Hello
# 获取后5个字符
last_five = text[-5:]
print(last_five)  # World
# 每隔一个字符取一个
every_other = text[::2]
print(every_other)  # HloWrd
# 反转字符串
reversed_text = text[::-1]
