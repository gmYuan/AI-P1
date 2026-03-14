"""
# 定义一个包含多个元素的列表
items = ["苹果", "香蕉", "橙子", "葡萄"]

# 使用enumerate()遍历列表，同时获取索引和值
for index, value in enumerate(items, start=1):
    # 打印索引和对应的值
    print(f"索引: {index}, 值: {value}")

# 输出结果：
# 索引: 0, 值: 苹果
# 索引: 1, 值: 香蕉
# 索引: 2, 值: 橙子
# 索引: 3, 值: 葡萄


# 定义一个字符串
text = "Hello"

# 使用enumerate()遍历字符串
for position, character in enumerate(text):
    # 打印字符的位置和字符本身
    print(f"位置: {position}, 字符: '{character}'")

# 输出结果：
# 位置: 0, 字符: 'H'
# 位置: 1, 字符: 'e'
# 位置: 2, 字符: 'l'
# 位置: 3, 字符: 'l'
# 位置: 4, 字符: 'o'


# 定义一个包含坐标的元组列表
coordinates = [(10, 20), (30, 40), (50, 60), (70, 80)]

# 使用enumerate()遍历坐标
for point_index, (x, y) in enumerate(coordinates):
    # 打印点的索引和坐标
    print(f"点 {point_index + 1}: x={x}, y={y}")

# 输出结果：
# 点 1: x=10, y=20
# 点 2: x=30, y=40
# 点 3: x=50, y=60
# 点 4: x=70, y=80


# 定义一个字典
scores = {"数学": 95, "英语": 88, "物理": 92, "化学": 90}

# 使用enumerate()遍历字典的键
for subject_index, subject in enumerate(scores.keys()):
    # 获取对应的分数
    score = scores[subject]
    # 打印科目索引、科目名称和分数
    print(f"科目 {subject_index + 1}: {subject} = {score}分")


# 使用enumerate()遍历字典的键
for subject_index, (subject, score) in enumerate(scores.items()):
    # 打印科目索引、科目名称和分数
    print(f"科目 {subject_index + 1}: {subject} = {score}分")



# 将内容写入临时文件
with open("temp.txt", "w", encoding="utf-8") as f:
    f.write(file_content)

# 使用enumerate()读取文件并显示行号
with open("temp.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=-1):
        # 去除行尾的换行符并打印行号和内容
        print(f"第{line_number+2}行: {line.strip()}")

# 输出结果：
# 第1行: 第一行：Python基础语法
# 第2行: 数据类型和变量
# 第3行: 控制流程语句
# 第4行: 函数和模块
# 第5行: 面向对象编程

# 定义3个列表
names = ["张三", "李四", "王五"]
ages = (25, 30, 28)
cities = ["北京", "上海", "广州"]
# zip_result = [("张三", 25, "北京"), ("李四", 30, "上海"), ("王五", 28, "广州")]
zip_result = zip(names, ages, cities)
# for item in zip_result:
#    print(item)

# 使用enumerate()和zip()同时遍历多个序列
for index, (name, age, city) in enumerate(zip_result, start=1):
    # 打印索引和组合信息
    print(f"员工{index}: {name}, {age}岁, 来自{city}")

# 输出结果：
# 员工1: 张三, 25岁, 来自北京
# 员工2: 李四, 30岁, 来自上海
# 员工3: 王五, 28岁, 来自广州


# 定义一个数字列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_number(x):
    return x % 2 == 0


# 使用filter()过滤偶数
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
even_numbers = filter(get_number, numbers)
# 使用enumerate()遍历过滤后的结果
for index, number in enumerate(even_numbers[3:8], start=1):
    # 打印偶数的序号和值
    print(f"第{index}个偶数: {number}")

# 输出结果：
# 第1个偶数: 2
# 第2个偶数: 4
# 第3个偶数: 6
# 第4个偶数: 8
# 第5个偶数: 10


# 定义一个字符串列表
words = ["hello", "world", "python", "programming"]

# 使用map()将字符串转换为大写
upper_words = map(str.upper, words)

# 使用enumerate()遍历转换后的结果
for index, word in enumerate(upper_words, start=1):
    # 打印序号和大写单词
    print(f"单词{index}: {word}")

# 输出结果：
# 单词1: HELLO
# 单词2: WORLD
# 单词3: PYTHON
# 单词4: PROGRAMMING


# 定义一个列表
items = ["苹果", "香蕉", "橙子", "葡萄"]

# 使用enumerate()创建带索引的字典
indexed_dict = {
    "key" + str(index) + "suffix": item + "好吃" for index, item in enumerate(items)
}
# {0: '苹果', 1: '香蕉', 2: '橙子', 3: '葡萄'}
print(indexed_dict)
# 打印结果
print("带索引的字典:")
for key, value in indexed_dict.items():
    print(f"索引 {key}: {value}")


# 定义一个列表
fruits = ["苹果", "香蕉", "橙子", "葡萄", "香蕉", "苹果"]


# 查找特定元素的所有位置
def find_all_positions(lst, target):
    el = enumerate(lst)  # [(0,"苹果")]
    # 使用列表推导式和enumerate()查找所有位置
    positions = [index for index, value in enumerate(lst) if value == target]
    return positions


# 查找'香蕉'的所有位置
banana_positions = find_all_positions(fruits, "香蕉")
print(f"'香蕉'在列表中的位置: {banana_positions}")

# 查找'苹果'的所有位置
apple_positions = find_all_positions(fruits, "苹果")
print(f"'苹果'在列表中的位置: {apple_positions}")

"""

# 定义一个数字列表
scores = [85, 92, 78, 96, 88, 91, 87, 94]

# 统计大于90分的成绩及其位置
high_scores = []
for index, score in enumerate(scores):
    # 如果分数大于90分
    if score > 90:
        # 记录位置和分数
        high_scores.append((index, score))

# 打印结果
print(f"大于90分的成绩有{len(high_scores)}个:")
for position, score in high_scores:
    print(f"位置{position}: {score}分")
