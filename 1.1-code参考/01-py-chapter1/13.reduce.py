# 导入reduce函数
from functools import reduce

"""

# 定义一个加法函数，用于累积求和
def add(x, y):
    # 返回两个参数的和
    return x + y


# 定义一个包含数字的列表
numbers = [1, 2, 3, 4, 5]
# 使用reduce函数对列表中的数字进行累积求和
# reduce会依次将1+2=3, 3+3=6, 6+4=10, 10+5=15
result = reduce(add, numbers)
# 打印最终结果
print(result)
# 输出: 15

# 验证reduce的工作过程
print("--- reduce工作过程演示 ---")
# 手动模拟reduce的工作过程
accumulator = numbers[0]  # 初始值为第一个元素1
print(f"初始值: {accumulator}")
# 从第二个元素开始累积
for i in range(1, len(numbers)):
    # 计算当前累积值和下一个元素的和
    accumulator = add(accumulator, numbers[i])
    # 打印每一步的结果
    print(f"步骤{i}: {accumulator}")
# 最终输出: 15



def reduce(function, sequence, initial={}):

    it = iter(sequence)
    value = initial

    for element in it:
        value = function(value, element)

    return value


keyValueParies = [["name", "张三"], ["age", 25], ["city", "北京"]]
# 可以使用dict
obj = dict(keyValueParies)
print(obj)

obj = {key: value for key, value in keyValueParies}
print(obj)


def accumulator(acc, pair):
    key, value = pair
    return {**acc, key: value}


# obj = reduce(lambda acc, pair: {**acc, pair[0]: pair[1]}, keyValueParies, {})
obj = reduce(accumulator, keyValueParies, {})
print(obj)


lst = ["a", 1, "b", 2, "c", 3]


obj = reduce(lambda acc, i: {**acc, lst[i]: lst[i + 1]}, range(0, len(lst), 2), {})
print(obj)



# 定义一个包含单词的列表
words = ["Hello", "Python", "World"]
# 使用reduce函数连接字符串
# lambda x, y: x + " " + y 在两个字符串之间添加空格
result = reduce(lambda x, y: x + " " + y, words)
print(f"连接结果: {result}")
# 输出: "Hello Python World"

# 不使用空格连接字符串
result_no_space = reduce(lambda x, y: x + y, words)
print(f"无空格连接: {result_no_space}")
# 输出: "HelloPythonWorld"

# 使用特定分隔符连接
separator = " | "
result_with_separator = reduce(lambda x, y: x + separator + y, words)
print(f"使用分隔符连接: {result_with_separator}")
# 输出: "Hello | Python | World"

# 实际应用：构建SQL查询条件
conditions = ["age > 18", "status = 'active'", "city = 'Beijing'"]
# 使用AND连接条件
sql_conditions = reduce(lambda x, y: x + " AND " + y, conditions)
print(f"SQL条件: {sql_conditions}")
# 输出: "age > 18 AND status = 'active' AND city = 'Beijing'"


# 定义一个包含数字的列表
numbers = [1, 2, 3, 4, 5]
# 第一步：使用map函数计算每个数字的平方
# map返回一个迭代器，包含 [1, 4, 9, 16, 25]
squared_numbers = map(lambda x: x * x, numbers)
# 第二步：使用filter函数过滤出偶数
# filter返回一个迭代器，包含 [4, 16]
filtered_numbers = filter(lambda x: x % 2 == 0, squared_numbers)
# 第三步：使用reduce函数计算过滤后数字的和
# reduce计算 4 + 16 = 20
result = reduce(lambda x, y: x + y, filtered_numbers, 0)
print(f"最终结果: {result}")
# 输出: 20

# 分步骤展示过程
print("--- 分步骤展示 ---")
# 第一步：计算平方
squared = list(map(lambda x: x * x, numbers))
print(f"平方结果: {squared}")
# 输出: [1, 4, 9, 16, 25]

# 第二步：过滤偶数
filtered = list(filter(lambda x: x % 2 == 0, squared))
print(f"过滤结果: {filtered}")
# 输出: [4, 16]

# 第三步：求和
sum_result = reduce(lambda x, y: x + y, filtered, 0)
print(f"求和结果: {sum_result}")
# 输出: 20

# 实际应用：处理学生成绩
scores = [85, 92, 78, 96, 88, 73, 91, 84, 79, 95]
# 第一步：过滤出优秀成绩（>=90）
excellent_scores = filter(lambda x: x >= 90, scores)
# 第二步：计算优秀成绩的平均分
excellent_list = list(excellent_scores)
if excellent_list:
    # 计算总分
    total = reduce(lambda x, y: x + y, excellent_list)
    # 计算平均分
    average = total / len(excellent_list)
    print(f"优秀成绩: {excellent_list}")
    print(f"优秀成绩平均分: {average}")
else:
    print("没有优秀成绩")
# 输出: 优秀成绩: [92, 96, 91, 95]
#       优秀成绩平均分: 93.5
# js 的map 和filter直接是数组，然后python出来不是  还要list一下
"""
numbers = [1, 2, 3, 4, 5]


def mapFn(x):
    print("计算mapFn的x的值", x)
    return x * x


squared_numbers = map(mapFn, numbers)
print(squared_numbers)
next(squared_numbers)
squared_numbers.__next__()
# list(squared_numbers)
for item in squared_numbers:
    print(item)
