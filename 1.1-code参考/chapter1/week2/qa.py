"""
str1 = "abcde"
str2 = "bcd"
str3 = str1[1:4]
print(str1, id(str1))
print(str2, id(str2))
print(str3, id(str3))
str4 = "bcd"
print(str4, id(str4))
print(str2 is str4)


# print("abc".split(""))  # ValueError: empty separator
# 是没有办法将abc改为[a,b,c]的 只能通过list来生成
print(list("abc"))


# 1100如果右移3位  会怎么样
# 1
print(0b1100 >> 4 == 0b1100 >> 5)
# 感觉r+，w+，a+是一样的作用？
# w 清空原来内容写入
# a 在原来内容的尾部追加写入
# 这是操作权限，可不是操作顺序


# with open("test.txt", "r+") as file:
#    file.write()
#    file.read()
#
#    file.read()
#    file.write()
# set_mode 通过  mode | fllag实现能懂。另外清除切换包含三个操作 位迅运算 不太理解。
READ = 0b0001  # 1
WRITE = 0b0010  # 2
APPEND = 0b0100  # 4
mode = 0b0000
# + READ
mode |= READ  # 0b0001
mode |= 0b0010  # 0b0011
print(mode)
# ~READ 0b1110
mode &= ~READ  #  0b0010
print(mode)


b = bytes([65])
print(b)


items = ["apple", "banana", "cherry", "date", "elderberry"]
# 使用切片[::-1]创建反向列表 ['elderberry', 'date', 'cherry', 'banana', 'apple']
reversed_items = items[::-1]
print(reversed_items)
# 遍历反向列表
for i, item in enumerate(reversed_items):
    # 计算原始索引
    original_index = len(items) - 1 - i
    # 打印原始索引和值
    print(f"原始索引 {original_index}: {item}")


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers1 = numbers[-8:-2]
print(numbers1)  # [3, 4, 5, 6, 7, 8]
numbers2 = numbers[-2:-8:-1]
print(numbers2)  # [9, 8, 7, 6, 5, 4]
# 我刚才试了a = num[-2:-8:] 是空的。说明不支持从右到左的正向
numbers3 = numbers[
    -2:-8:1
]  # start=8  end=3 |  startIndex=8,endIndex=3 1   index需要大于等于8，小于3
print(numbers3)
numbers4 = numbers[
    -2:-8:-1
]  # start=8  end=3 |  startIndex=8,endIndex=3 1   index需要大于等于8，小于3
print(numbers4)


l1 = [1, 2]
l2 = [3, 4]
l3 = l1 + l2

print(l3)

import logging


arr6 = ["a", "b", "c"]
print(arr6[-1])


key = "Alice"
print(f"{key}")
print(f"{{}}")
print(f"{{{key}}}")


# fstring 如何 转义
key = "Alice"
# 转义花括号
print(f"我的名字是 {{key}} ")
# 单个括号转义
print(f"我的名字是 {{ {key} }} ")
print(f"我的名字是 {key} ")
print(f"{{")
print(f"}}")
# 输出: {

print(f"我的名字是 {key} ")


# +和extend的区别是不是，+只能是相同的数据类型，extend只要是迭代器的都可以合并？
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = (4, 5, 6)
list4 = {4, 5, 6}
list5 = "hello"
# list1.extend(list2)
# print(list1)
list1 += list5
print(list1)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:8])
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers)  # <filter object at 0x0000021D6A4659C0>
print(list(even_numbers)[3:8])


# 使用列表推导式和enumerate()查找所有位置
#    positions = [index for index, value in enumerate(lst) if value == target]
list = [1, 2, 3]
list2 = [item * 2 for item in list if item > 1]
print(list2)


# 定义一个字符串列表
words = ["hello", "world", "python", "programming"]

# 使用map()将字符串转换为大写
upper_words = map(str.upper, words)

# 使用enumerate()遍历转换后的结果
for index, word in enumerate(upper_words, start=1):
    # 打印序号和大写单词
    print(f"单词{index}: {word}")


lst = list(upper_words)
print(lst)
print(len(lst))
# 这个lst 为啥成[]了




words = ["hello", "world", "python", "programming"]
del words
print(words)
"""

my_list_pop_no_index = [10, 20, 30]
# last_element = my_list_pop_no_index.pop()
# print(last_element)
# print(my_list_pop_no_index)

last_element = my_list_pop_no_index.pop(1)
print(last_element)
print(my_list_pop_no_index)

item = "hello"
# item = 1
# item = 1.1
if isinstance(item, (int, float)):
    print(type(item))  # <class 'float'>
else:
    print(type(item))
