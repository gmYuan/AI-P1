"""
# 定义一个原始字符串
original_string = "hello"
# 使用字符串切片[::-1]反转字符串
# [::-1]表示从开始到结束，步长为-1（反向）
reversed_string = original_string[::-1]
# 打印反转后的字符串
print(reversed_string)
# 输出: olleh

# 验证原始字符串未被修改
print(f"原始字符串: {original_string}")
# 输出: 原始字符串: hello

# 定义一个原始字符串
original_string = "hello"
# 使用reversed()函数获取反向迭代器
# reversed()返回一个反向迭代器
reversed_iterator = reversed(original_string)
# 使用join()方法将迭代器中的字符连接成字符串
reversed_string = "".join(reversed_iterator)
# 打印反转后的字符串
print(reversed_string)
# 输出: olleh
# olleh
# 一步完成反转
reversed_string_one_step = "".join(reversed(original_string))
print(f"一步反转: {reversed_string_one_step}")
# 输出: 一步反转: olleh


# 使用不同的连接符
reversed_with_dash = "-".join(reversed(original_string))
print(f"用连字符连接: {reversed_with_dash}")
# 输出: 用连字符连接: o-l-l-e-h


original_string = "hello"
reversed_string = reversed(original_string)
# 迭代器是一次性的，取完就没有了，不有再用了
# python中的迭代器和js中用法和概念基本相同
# for item in reversed_string:
#    print(item)

print("".join(reversed_string))


def gen():
    print("before 1")
    yield 1
    print("before 2")
    yield 2
    print("before 3")
    yield 3


it = gen()
# print(next(it))
ls = list(it)
print(ls)
# print(next(it))
# print(next(it))
# for item in it:
#    print(item)
# 列表 list 元组 tuple 集合set 甚至是字符串都是特殊的迭代器

# <reversed object at 0x10acb6230>,type=<class 'reversed'>，还以为返回的会是list类型，怎么还有reversed类型呢
# python reversed map filter reduce 有很多方法返回的都是是迭代器，而非列表
# 文档里面说it是生成器，特殊的迭代器
# 生成器是通过生成器函数执行得到的，它是一种特殊的迭代器
# 张三是一个人
# 张三=生成器
# 人= 迭代器
# 迭代器我们可以认为它是一个规范，也可以说是一个接口，它有各种不同的类型的实现
# 可迭代对象就相当于一本书
# 迭代器就相当一个翻页器，可以把书一页一页的向后翻
# 可迭代对象像一个快递驿站 迭代器像一个快递员，负责把驿站的快递送到家里，送一件就少一件

# 特殊的迭代器，就是特殊在可以多次使用吗？  不是的，特殊在每个迭代器都不一样
# 迭代器类似于一个接口，有不同的实现


# 定义一个原始字符串
original_string = "hello"
# 初始化空字符串用于存储反转结果
reversed_string = ""
# 遍历原始字符串中的每个字符
for char in original_string:
    # 将当前字符添加到反转字符串的开头
    reversed_string = char + reversed_string
# 打印反转后的字符串
print(reversed_string)
# 输出: olleh


# 使用列表收集字符然后反转
def reverse_with_list(text):
    # 将字符串转换为字符列表
    char_list = list(text)
    # 反转列表
    char_list.reverse()
    # 将列表转换回字符串
    return "".join(char_list)


# 测试列表反转方法
test_string = "Python"
reversed_with_list = reverse_with_list(test_string)
print(f"列表反转: {reversed_with_list}")
# 输出: 列表反转: nohtyP



# 定义递归反转函数
def reverse_string(s):
    # 基本情况：如果字符串为空，直接返回
    if len(s) == 0:
        return s
    else:
        # 递归情况：反转除第一个字符外的子字符串，然后加上第一个字符
        return reverse_string(s[1:]) + s[0]


# 测试递归反转函数
original_string = "hello"
# 调用递归函数反转字符串
reversed_string = reverse_string(original_string)
# 打印反转后的字符串
print(reversed_string)
# 输出: olleh
"""


# 带尾递归优化的递归函数
def reverse_string_tail(s, result=""):
    # 如果输入字符串为空，返回结果
    if len(s) == 0:
        return result
    else:
        # 尾递归：将第一个字符添加到结果的开头
        return reverse_string_tail(s[1:], s[0] + result)


# 测试尾递归反转函数
test_string = "Python"
reversed_tail = reverse_string_tail(test_string)
print(f"尾递归反转: {reversed_tail}")
# 输出: 尾递归反转: nohtyP

#
