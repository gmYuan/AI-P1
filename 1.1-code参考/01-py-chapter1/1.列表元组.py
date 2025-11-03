"""
# 列表的创建方式
# 使用方括号创建空列表
empty_list = []
print(f"空列表: {empty_list}, 类型: {type(empty_list)}")

# 使用方括号创建包含元素的列表
numbers_list = [1, 2, 3, 4, 5]
print(f"数字列表: {numbers_list}, 类型: {type(numbers_list)}")

# 使用list()构造函数创建列表
string_list = list("hello")
print(f"字符串列表: {string_list}, 类型: {type(string_list)}")

# 元组的创建方式
# 使用圆括号创建空元组
empty_tuple = ()
print(f"空元组: {empty_tuple}, 类型: {type(empty_tuple)}")

# 使用圆括号创建包含元素的元组
numbers_tuple = (1, 2, 3, 4, 5)
print(f"数字元组: {numbers_tuple}, 类型: {type(numbers_tuple)}")

# 创建单元素元组需要逗号
single_tuple = (42,)  # 注意这里的逗号
print(f"单元素元组: {single_tuple}, 类型: {type(single_tuple)}")

# 没有逗号的话会被认为是括号表达式
not_tuple = 42
print(f"不是元组: {not_tuple}, 类型: {type(not_tuple)}")

# 使用tuple()构造函数创建元组
string_tuple = tuple("world")
print(f"字符串元组: {string_tuple}, 类型: {type(string_tuple)}")


# 列表和元组都支持索引和切片操作
# 创建测试数据
fruits_list = ["苹果", "香蕉", "橙子", "葡萄", "草莓"]
colors_tuple = ("红色", "绿色", "蓝色", "黄色", "紫色")

print("=== 索引操作 ===")
# 访问第一个元素（索引0）
print(f"列表第一个元素: {fruits_list[0]}")
print(f"元组第一个元素: {colors_tuple[0]}")

# 访问最后一个元素（索引-1）
print(f"列表最后一个元素: {fruits_list[-1]}")
print(f"元组最后一个元素: {colors_tuple[-1]}")

# 访问中间元素
print(f"列表第三个元素: {fruits_list[2]}")
print(f"元组第三个元素: {colors_tuple[2]}")

print("\n=== 切片操作 ===")
# 获取前三个元素
print(f"列表前三个元素: {fruits_list[:3]}")
print(f"元组前三个元素: {colors_tuple[:3]}")

# 获取中间三个元素
print(f"列表中间三个元素: {fruits_list[1:4]}")
print(f"元组中间三个元素: {colors_tuple[1:4]}")

# 获取最后三个元素
print(f"列表最后三个元素: {fruits_list[-3:]}")
print(f"元组最后三个元素: {colors_tuple[-3:]}")

# 步长切片
print(f"列表每隔一个元素: {fruits_list[::2]}")
print(f"元组每隔一个元素: {colors_tuple[::2]}")


# 创建初始列表
my_list = [1, 2, 3]
print(f"初始列表: {my_list}")

# 修改元素
my_list[0] = 10
print(f"修改第一个元素后: {my_list}")

# 添加元素
my_list.append(4)
print(f"添加元素后: {my_list}")

# 插入元素
my_list.insert(1, 5)
print(f"插入元素后: {my_list}")

# 删除元素
my_list.remove(2)
print(f"删除元素2后: {my_list}")

# 删除指定位置的元素
del my_list[0]
print(f"删除第一个元素后: {my_list}")

# 排序
my_list.sort()
print(f"排序后: {my_list}")

# 反转
my_list.reverse()
print(f"反转后: {my_list}")

# 清空列表
my_list.clear()
print(f"清空后: {my_list}")


# 创建初始元组
my_tuple = (1, 2, 3)
print(f"初始元组: {my_tuple}")

# 尝试修改元素（这会引发错误）
try:
    my_tuple[0] = 10
    print(f"修改第一个元素后: {my_tuple}")
except TypeError as e:
    print(f"修改元组元素时出错: {e}")  #'tuple' object does not support item assignment

# 尝试添加元素（这会引发错误）
try:
    my_tuple.append(4)
    print(f"添加元素后: {my_tuple}")
except AttributeError as e:
    print(f"添加元组元素时出错: {e}")  #'tuple' object has no attribute 'append'

# 尝试删除元素（这会引发错误）
try:
    del my_tuple[0]
    print(f"删除第一个元素后: {my_tuple}")
except TypeError as e:
    print(f"删除元组元素时出错: {e}")  #'tuple' object doesn't support item deletion

# 元组支持的操作
print(f"元组长度: {len(my_tuple)}")
print(f"元组中元素2的索引: {my_tuple.index(2)}")
print(f"元组中元素3的个数: {my_tuple.count(3)}")

# 元组可以重新赋值（创建新元组）
my_tuple = (4, 5, 6)
print(f"重新赋值后的元组: {my_tuple}")


# 列表转元组
original_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(original_list)
print(f"原始列表: {original_list}, 类型: {type(original_list)}")
print(f"转换后元组: {converted_tuple}, 类型: {type(converted_tuple)}")

# 元组转列表
original_tuple = ("a", "b", "c", "d", "e")
converted_list = list(original_tuple)
print(f"原始元组: {original_tuple}, 类型: {type(original_tuple)}")
print(f"转换后列表: {converted_list}, 类型: {type(converted_list)}")

# 字符串转列表和元组
text = "Python"
text_list = list(text)
text_tuple = tuple(text)
print(f"原始字符串: {text}")
print(f"转换为列表: {text_list}")
print(f"转换为元组: {text_tuple}")

# 列表推导式创建
squares_list = [x**2 for x in range(5)]
squares_tuple = tuple(x**2 for x in range(5))
print(f"列表推导式: {squares_list}")
print(f"元组推导式: {squares_tuple}")


# 嵌套列表
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"嵌套列表: {nested_list}")
print(f"访问嵌套元素: {nested_list[1][2]}")

# 修改嵌套列表
nested_list[1][2] = 99
print(f"修改后嵌套列表: {nested_list}")

# 嵌套元组
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"嵌套元组: {nested_tuple}")
print(f"访问嵌套元素: {nested_tuple[1][2]}")

# 混合嵌套
mixed_structure = [(1, 2), [3, 4], (5, 6)]
print(f"混合嵌套结构: {mixed_structure}")

# 可以修改列表部分
mixed_structure[1][0] = 99
print(f"修改列表部分后: {mixed_structure}")

# 但不能修改元组部分
try:
    mixed_structure[0][0] = 99
except TypeError as e:
    print(f"修改元组部分时出错: {e}")  #'tuple' object does not support item assignment



# 元组包含列表 列表里面的元素是可变的
mixed_structure = ((1, 2), [3, 4], (5, 6))
print(f"混合嵌套结构: {mixed_structure}")
mixed_structure[1][1] = 44
print(f"混合嵌套结构: {mixed_structure}")
mixed_structure[1] = 2  #'tuple' object does not support item assignment
mixed_structure = ((1, 2), [3, 4], (5, 6))
dict = {}
dict[mixed_structure] = 100
# cannot use 'tuple' as a dict key (unhashable type: 'list')
# 如果一个元组里面包含列表的话，那么这个元素将不能作为字典的key了
"""

# 列表解包
coordinates = [10, 20, 30]
x, y, z = coordinates
print(f"坐标解包: x={x}, y={y}, z={z}")

# 元组解包
person_info = ("张三", 25, "北京")
name, age, city = person_info
print(f"人员信息解包: 姓名={name}, 年龄={age}, 城市={city}")

# 部分解包
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"部分解包: 第一个={first}, 中间={middle}, 最后一个={last}")


# 函数返回多个值
def get_statistics(data):
    # 返回数据的统计信息
    # return min(data), max(data), sum(data) / len(data)
    return (min(data), max(data), sum(data) / len(data))


data = [1, 2, 3, 4, 5]
print(get_statistics(data))
min_val, max_val, avg_val = get_statistics(data)
print(f"统计信息: 最小值={min_val}, 最大值={max_val}, 平均值={avg_val:.2f}")

# 交换变量值
a, b = 10, 20
print(f"交换前: a={a}, b={b}")
a, b = b, a
print(f"交换后: a={a}, b={b}")
