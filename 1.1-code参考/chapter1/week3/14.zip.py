"""
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
result = list(zip(list1, list2))
print(result)
# 输出: [(1, 'a'), (2, 'b'), (3, 'c')]


for item1, item2 in zip(list1, list2):
    print(f"{item1} -> {item2}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))
print(transposed)


# zip() 函数的工作原理可以这样理解：
# 接收多个可迭代对象作为参数
# 同时迭代这些可迭代对象，每次取每个对象的第i个元素
# 将这些元素组合成一个元组返回
# 当最短的可迭代对象耗尽时，停止迭代


def zipFn(*iterables):
    # 获取最短的可迭代对象的长度
    min_length = min(len(iterable) for iterable in iterables)
    result = []
    for i in range(min_length):  # 0 1 2
        tuple_elements = []
        for iterable in iterables:
            tuple_elements.append(iterable[i])
        result.append(tuple(tuple_elements))
    return result


list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
result = list(zip(list1, list2))
print(result)


# 基本拆包操作
# 定义一个包含元组的列表，模拟zip后的结果
zipped = [(1, "a"), (2, "b"), (3, "c")]

# 使用*操作符对zipped列表进行解包，然后使用zip函数将其反向解压
list1, list2 = zip(*zipped)
print(f"原始压缩数据: {zipped}")
# 打印原始压缩数据
print(f"解压后的第一个元组: {list1}")
# 打印解压后的第一个元组
# 预期输出: (1, 2, 3)
print(f"解压后的第二个元组: {list2}")
# 打印解压后的第二个元组
# 预期输出: ('a', 'b', 'c')

# 三个列表的拆包
zipped_three = [(1, "a", 1.1), (2, "b", 2.2), (3, "c", 3.3)]
# 定义包含三个元素的元组列表
list1, list2, list3 = zip(*zipped_three)
# 解压三个列表
print(f"\n三个列表的拆包:")
# 打印三个列表的拆包标题
print(f"解压后的第一个元组: {list1}")
# 打印解压后的第一个元组
print(f"解压后的第二个元组: {list2}")
# 打印解压后的第二个元组
print(f"解压后的第三个元组: {list3}")
# 打印解压后的第三个元组

# 实际应用：转置矩阵
print("\n实际应用：转置矩阵")
# 打印实际应用标题
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 定义一个3x3矩阵
print(f"原始矩阵: {matrix}")
# 打印原始矩阵
transposed = list(zip(*matrix))
# 使用zip函数转置矩阵
print(f"转置后矩阵: {transposed}")
# 打印转置后的矩阵
# 预期输出: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# 将转置结果转换回列表格式
transposed_lists = [list(row) for row in transposed]
# 将元组转换为列表
print(f"转置后列表格式: {transposed_lists}")
# 打印转置后的列表格式


from itertools import zip_longest

# 定义不同长度的列表
list1 = [1, 2, 3, 4, 5]
# 定义第一个列表（较长）
list2 = ["a", "b"]
# 定义第二个列表（较短）
list3 = [1.1, 2.2, 3.3]
# 定义第三个列表（中等长度）

# 使用普通zip函数
print("1. 使用普通zip函数:")
# 打印使用普通zip函数标题
result_normal = zip(list1, list2, list3)
# 使用普通zip函数压缩列表
print(f"普通zip结果: {list(result_normal)}")
# 将迭代器转换为列表并打印
# 预期输出: [(1, 'a', 1.1), (2, 'b', 2.2)]

# 使用zip_longest函数
print("\n2. 使用zip_longest函数:")
# 打印使用zip_longest函数标题
result_longest = zip_longest(list1, list2, list3, fillvalue=None)
# 使用zip_longest函数压缩列表，使用'x'作为填充值
print(f"zip_longest结果: {list(result_longest)}")
# 将迭代器转换为列表并打印
# 预期输出: [(1, 'a', 1.1), (2, 'b', 2.2), (3, 'x', 3.3), (4, 'x', 'x'), (5, 'x', 'x')]

# 使用不同的填充值
print("\n3. 使用不同的填充值:")
# 打印使用不同的填充值标题
result_custom = zip_longest(list1, list2, list3, fillvalue=0)
# 使用0作为填充值
print(f"使用0作为填充值: {list(result_custom)}")
# 将迭代器转换为列表并打印

# 使用None作为填充值（默认）
result_none = zip_longest(list1, list2, list3)
# 使用None作为填充值（默认）
print(f"使用None作为填充值: {list(result_none)}")
# 将迭代器转换为列表并打印

# 实际应用：处理CSV文件的不同列数
print("\n4. 实际应用：处理CSV文件的不同列数")
# 打印实际应用标题
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "25"],
    ["Bob", "30", "New York", "Engineer"],
    ["Charlie", "35", "London"],
]
# 定义CSV数据（不同行有不同列数）

# 使用zip_longest处理CSV数据
processed_data = list(zip_longest(*csv_data, fillvalue=""))
# 使用zip_longest处理CSV数据
print("处理后的CSV数据:")
# 打印处理后的CSV数据标题
for row in processed_data:
    # 遍历处理后的数据
    print(f"  {row}")
    # 打印每一行




# 将zip后的数据解包回原始的可迭代对象 相当于zip(*zipped_data)
def zip_unpack(zipped_data):
    if not zipped_data:
        return ()
    return tuple(zip(*zipped_data))


data = [(1, "a", 10), (2, "b", 20), (3, "c", 30)]
unpacked = zip_unpack(data)
print(data)
print(unpacked)
print(list(zip(*unpacked)))
"""


def zipFn(*iterables):
    # 获取最短的可迭代对象的长度
    min_length = min(len(iterable) for iterable in iterables)
    result = []
    for i in range(min_length):  # 0 1 2
        tuple_elements = []
        for iterable in iterables:
            tuple_elements.append(iterable[i])
        result.append(tuple(tuple_elements))
    return result


list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
print(list1)
print(list2)
result = list(zip(list1, list2))
print(result)
result = list(zip(*result))
for item in result:
    print(item)
