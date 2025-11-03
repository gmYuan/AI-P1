"""
# 定义一个简单的Lambda函数，接收两个参数并返回它们的和
add = lambda x, y: x + y
# 调用Lambda函数并打印结果
print(add(3, 5))
# 输出: 8

# 定义一个Lambda函数，计算数字的平方
square = lambda x: x**2
# 调用Lambda函数计算5的平方
result = square(5)
print(f"5的平方: {result}")
# 输出: 5的平方: 25

# 定义一个Lambda函数，判断数字是否为偶数
is_even = lambda x: x % 2 == 0
# 测试Lambda函数
print(f"4是偶数: {is_even(4)}")
print(f"7是偶数: {is_even(7)}")
# 输出: 4是偶数: True
#       7是偶数: False

# 定义一个Lambda函数，获取字符串的长度
get_length = lambda s: len(s)
# 测试Lambda函数
text = "Hello World"
length = get_length(text)
print(f"'{text}'的长度: {length}")
# 输出: 'Hello World'的长度: 11


# 定义一个包含字符串的列表
words = ["apple", "banana", "cherry", "date", "elderberry"]
# 使用sort方法对列表进行排序，key参数指定排序依据
# Lambda函数接收一个字符串x，返回其长度，从而实现按字符串长度排序
words.sort(key=lambda x: len(x))
# 打印排序后的列表
print(words)
# 输出: ['date', 'apple', 'banana', 'cherry', 'elderberry']

# 按字符串长度降序排序
words_desc = ["apple", "banana", "cherry", "date", "elderberry"]
# 使用Lambda函数按长度降序排序
words_desc.sort(key=lambda x: len(x), reverse=True)
print(f"按长度降序: {words_desc}")
# 输出: 按长度降序: ['elderberry', 'banana', 'cherry', 'apple', 'date']

# 复杂对象的排序
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 19, "grade": 92},
    {"name": "Charlie", "age": 21, "grade": 78},
]
# 按年龄排序
students_by_age = sorted(students, key=lambda x: x["age"])
print("按年龄排序:")
for student in students_by_age:
    print(f"{student['name']}: {student['age']}岁")

# 按成绩排序
students_by_grade = sorted(students, key=lambda x: x["grade"], reverse=True)
print("\n按成绩排序:")
for student in students_by_grade:
    print(f"{student['name']}: {student['grade']}分")


# 定义一个数字列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 使用列表推导式和Lambda函数创建新列表
# Lambda函数用于计算每个数字的平方
squared_numbers = [(lambda x: x**2)(num) for num in numbers]
print(f"平方数列表: {squared_numbers}")
# 输出: 平方数列表: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 使用Lambda函数进行条件过滤
# Lambda函数判断数字是否大于5
large_numbers = [num for num in numbers if (lambda x: x > 5)(num)]
print(f"大于5的数字: {large_numbers}")
# 输出: 大于5的数字: [6, 7, 8, 9, 10]

# 使用Lambda函数进行字符串处理
texts = ["hello", "world", "python", "programming"]
# Lambda函数将字符串转换为大写
upper_texts = [(lambda s: s.upper())(text) for text in texts]
print(f"大写字符串: {upper_texts}")
# 输出: 大写字符串: ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']
"""

# 1. Lambda函数只能包含表达式，不能包含语句
# 以下代码会报错，因为Lambda函数不能包含print语句
invalid_lambda = lambda x: print(x)  # 这会导致语法错误


# 2. Lambda函数不能包含复杂的逻辑
# 如果需要复杂逻辑，应该使用def函数
def complex_function(x):
    # 复杂的逻辑处理
    if x > 0:
        return x * 2
    elif x == 0:
        return 0
    else:
        return x * -1


# 3. Lambda函数不能包含多行代码
# 以下代码会报错
# multi_line_lambda = lambda x:y = x * 2 return y

# 4. Lambda函数不能包含异常处理
# 以下代码会报错
# error_handling_lambda = lambda x: try: x/0 except: 0


# 正确的做法：使用def函数
def safe_divide(x, y):
    # 使用def函数处理异常
    try:
        return x / y
    except ZeroDivisionError:
        return 0


# 测试安全除法函数
result = safe_divide(10, 0)
print(f"安全除法结果: {result}")

# 5. Lambda函数不能包含循环
# 以下代码会报错
# loop_lambda = lambda x: for i in range(x): print(i)


# 正确的做法：使用def函数
def print_range(n):
    # 使用def函数实现循环
    for i in range(n):
        print(i)


# 测试循环函数
print("打印范围:")
print_range(3)

# 复杂的 lambda 函数也是这种 :  格式吗？还是要写 return