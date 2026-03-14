"""
# 将整数5赋值给变量x
x = 5
# 打印x的值以验证赋值
print(f"x = {x}")  # 输出: x = 5

# 将字符串赋值给变量
name = "Alice"
print(f"name = {name}")  # 输出: name = Alice

# 将列表赋值给变量
numbers = [1, 2, 3, 4, 5]
print(f"numbers = {numbers}")  # 输出: numbers = [1, 2, 3, 4, 5]

# 将字典赋值给变量
person = {"name": "Bob", "age": 25}
print(f"person = {person}")  # 输出: person = {'name': 'Bob', 'age': 25}

# 多重赋值
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")  # 输出: a = 1, b = 2, c = 3

# 序列解包赋值
data = [10, 20, 30]
x, y, z = data
print(f"x = {x}, y = {y}, z = {z}")  # 输出: x = 10, y = 20, z = 30


# 初始化变量
x = 10
print(f"初始值 x = {x}")

# 加法赋值 (+=)
# 将x的值增加5，相当于 x = x + 5
x += 5
print(f"x += 5 后，x = {x}")  # 输出: x = 15

# 减法赋值 (-=)
# 将x的值减少3，相当于 x = x - 3
x -= 3
print(f"x -= 3 后，x = {x}")  # 输出: x = 12

# 乘法赋值 (*=)
# 将x的值乘以2，相当于 x = x * 2
x *= 2
print(f"x *= 2 后，x = {x}")  # 输出: x = 24

# 除法赋值 (/=)
# 将x的值除以4，相当于 x = x / 4
x /= 4
print(f"x /= 4 后，x = {x}")  # 输出: x = 6.0

# 整除赋值 (//=)
# 将x的值整除3，相当于 x = x // 3
x //= 3
print(f"x //= 3 后，x = {x}")  # 输出: x = 2.0

# 取余赋值 (%=)
# 将x的值取余2，相当于 x = x % 2
x %= 2
print(f"x %= 2 后，x = {x}")  # 输出: x = 0.0

# 指数赋值 (**=)
# 将x的值计算2的3次方，相当于 x = x ** 3
x = 2
x **= 3
print(f"x **= 3 后，x = {x}")  # 输出: x = 8


# 应用1：计数器
counter = 0
print("计数器应用:")
for i in range(5):
    # 每次循环计数器加1
    counter += 1
    print(f"第 {counter} 次循环")

# 应用2：累加器
total = 0
numbers = [1, 2, 3, 4, 5]
print(f"\n累加器应用:")
print(f"数字列表: {numbers}")
for num in numbers:
    # 累加每个数字
    total += num
    print(f"累加 {num} 后，总和 = {total}")

# 应用3：字符串拼接
message = "Hello"
print(f"\n字符串拼接应用:")
print(f"初始消息: {message}")
# 拼接字符串
message += " World"
print(f"拼接后: {message}")
message += "!"
print(f"最终消息: {message}")

# 应用4：列表操作
my_list = [1, 2, 3]
print(f"\n列表操作应用:")
print(f"初始列表: {my_list}")
# 添加元素到列表
my_list += [4, 5]
print(f"添加元素后: {my_list}")
# 重复列表
my_list *= 2
print(f"重复列表后: {my_list}")


# 定义两个变量用于算术运算
a = 10
b = 3
print(f"a = {a}, b = {b}")

# 加法运算 (+)
# 10 + 3 = 13
result = a + b
print(f"加法 (a + b): {result}")  # 输出: 加法 (a + b): 13

# 减法运算 (-)
# 10 - 3 = 7
result = a - b
print(f"减法 (a - b): {result}")  # 输出: 减法 (a - b): 7

# 乘法运算 (*)
# 10 * 3 = 30
result = a * b
print(f"乘法 (a * b): {result}")  # 输出: 乘法 (a * b): 30

# 除法运算 (/)
# 10 / 3 = 3.333...
result = a / b
print(f"除法 (a / b): {result}")  # 输出: 除法 (a / b): 3.3333333333333335

# 整除运算 (//)
# 10 // 3 = 3
result = a // b
print(f"整除 (a // b): {result}")  # 输出: 整除 (a // b): 3

# 取余运算 (%)
# 10 % 3 = 1
result = a % b
print(f"取余 (a % b): {result}")  # 输出: 取余 (a % b): 1

# 指数运算 (**)
# 10 ** 3 = 1000
result = a**b
print(f"指数 (a ** b): {result}")  # 输出: 指数 (a ** b): 1000



# 情况1：负数运算
print("负数运算:")
a = -10
b = 3
print(f"负数除法: {a} / {b} = {a / b}")  # -3.3333333333333335
print(f"负数整除: {a} // {b} = {a // b}")  # -4
print(f"负数取余: {a} % {b} = {a % b}")  # 2

# 情况2：浮点数运算
print("\n浮点数运算:")
x = 0.1
y = 0.2
print(f"浮点数加法: {x} + {y} = {x + y}")  # 0.30000000000000004
print(f"浮点数乘法: {x} * 3 = {x * 3}")  # 0.30000000000000004

# 情况3：大数运算
print("\n大数运算:")
big_num1 = 2**100
big_num2 = 3**50
print(f"2^100 = {big_num1}")  # 1267650600228229401496703205376
print(f"3^50 = {big_num2}")  # 717897987691852588770249
print(f"大数相加: {big_num1 + big_num2}")  #  1267651318126217093349291975625

# 情况4：零除错误
print("\n零除错误处理:")
try:
    # 尝试除以零
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"零除错误: {e}")

try:
    # 尝试整除零
    result = 10 // 0
except ZeroDivisionError as e:
    print(f"整除零错误: {e}")

try:
    # 尝试取余零
    result = 10 % 0
except ZeroDivisionError as e:
    print(f"取余零错误: {e}")



# 运行符的优先级从高到低计算
# 如果优先一样的话，会有结合的顺序
# ** 和赋值 从右向左结合的
# 其它的都是从左向右结合的

val = 2**3**4
print(3**4)
print(2**81)
print(val)
val2 = 1 + 2 + 3


# 定义变量
a = 2
b = 3
c = 4

# 1. 指数运算的优先级高于乘法、加法
# 实际计算为 a + (b * c ** b)
result = a + b * c**b
print(result)  # 输出: 2 + 3 * (4 ** 3) = 2 + 3 * 64 = 2 + 192 = 194

# 2. 使用括号优先加法
# 实际计算为 (a + b) * (c ** b)
result2 = (a + b) * (c**b)
print(result2)  # 输出: 5 * 64 = 320

# 3. 赋值运算符优先级最低，最后才执行
d = 10
d += 2 * 3  # 首先计算2*3=6，然后d = d + 6
print(d)  # 输出: 16

# 4. 逻辑优先级演示
x = 5
y = 10
z = 0

print(x > 3 and y < 20 or z)  # True，先计算关系运算，再and，最后or
# True and True or False
# True or Fale
# True


# 5. 建议多用括号
calc = (a + b) * (c - 1)
print(calc)  # 明确表达式含义，输出: (2+3)*(4-1)=5*3=15


# 定义两个整数用于位运算
x = 10  # 二进制: 1010
y = 4  # 二进制:  0100

print(f"x = {x} (二进制: {bin(x)})")
print(f"y = {y} (二进制: {bin(y)})")

# 位与 (AND) 运算符
# 1010 & 0100 = 0000 (0)
result = x & y
print(f"位与 (x & y): {result} (二进制: {bin(result)})")

# 位或 (OR) 运算符
# 1010 | 0100 = 1110 (14)
result = x | y
print(f"位或 (x | y): {result} (二进制: {bin(result)})")

# 位异或 (XOR) 运算符  布衣  不一 统领 同零
# 1010 ^ 0100 = 1110 (14)
# 1010
# 0100
# 1110
result = x ^ y
print(f"位异或 (x ^ y): {result} (二进制: {bin(result)})")

# 位非 (NOT) 运算符
# ~10 = -11     ~x=-x-1
# 1010
# 0101
result = ~x
print(f"位非 (~x): {result} (二进制: {bin(result)})")

# 左移 (Left Shift) 运算符
# 1010 << 1 = 10100 (20)
result = x << 1
print(f"左移 (x << 1): {result} (二进制: {bin(result)})")

# 右移 (Right Shift) 运算符
# 1010 >> 1 = 0101 (5)
result = x >> 1
print(f"右移 (x >> 1): {result} (二进制: {bin(result)})")

# 位运算的实际应用
print("\n位运算的实际应用:")
# 应用1：检查奇偶性
num = 15
is_even = (num & 1) == 0
print(f"{num} 是偶数: {is_even}")

# 应用2：快速计算2的幂
power = 3
result = 1 << power  # 相当于 2^power
print(f"2^{power} = {result}")

# 应用3：交换两个数（不使用临时变量）
a, b = 5, 10
print(f"交换前: a = {a}, b = {b}")
a ^= b
b ^= a
a ^= b
print(f"交换后: a = {a}, b = {b}")


# 定义字符串和列表
my_string = "apple"
my_list = [1, 2, 3, 4, 5]
my_dict = {"name": "Alice", "age": 25}

# in 运算符：检查元素是否在序列中
print("in 运算符:")
print(f"'a' in my_string: {'a' in my_string}")  # 输出: 'a' in 'apple': True
print(f"'z' in my_string: {'z' in my_string}")  # 输出: 'z' in 'apple': False
print(f"3 in my_list: {3 in my_list}")  # 输出: 3 in [1,2,3,4,5]: True
print(f"6 in my_list: {6 in my_list}")  # 输出: 6 in [1,2,3,4,5]: False
print(f"'name' in my_dict: {'name' in my_dict}")  # 输出: 'name' in dict: True

# not in 运算符：检查元素是否不在序列中
print("\nnot in 运算符:")
print(
    f"'a' not in my_string: {'a' not in my_string}"
)  # 输出: 'a' not in 'apple': False
print(f"'z' not in my_string: {'z' not in my_string}")  # 输出: 'z' not in 'apple': True
print(f"3 not in my_list: {3 not in my_list}")  # 输出: 3 not in [1,2,3,4,5]: False
print(f"6 not in my_list: {6 not in my_list}")  # 输出: 6 not in [1,2,3,4,5]: True

# 实际应用：数据验证
print("\n实际应用：数据验证")


def validate_input(user_input, valid_options):
    if user_input in valid_options:
        return f"'{user_input}' 是有效选项"
    else:
        return f"'{user_input}' 不是有效选项"


# 测试数据验证
valid_choices = ["A", "B", "C", "D"]
test_inputs = ["A", "E", "B", "F"]

for input_val in test_inputs:
    result = validate_input(input_val, valid_choices)
    print(result)

"""

# 左结合示例
result = 10 - 5 - 2  # 等价于 (10 - 5) - 2 = 3
print(result)  # 输出: 3

# 右结合示例（幂运算和赋值）
print(2**3**2)  # 输出: 512，因为等价于 2 ** (3 ** 2) = 2 ** 9 = 512
a = b = c = 7
print(a, b, c)  # 输出: 7 7 7


# 测试表达式
a, b, c = 2, 3, 4

# 测试1：指数运算优先级
# 指数运算符 `**` 是右结合的**，这意味着：
# 当有多个连续的指数运算时，计算顺序是从右向左
# `a ** b ** c` 等价于 `a ** (b ** c)`
result1 = a**b**c
result2 = (a**b) ** c
print(f"a ** b ** c = {result1}")  # 2417851639229258349412352
print(f"(a ** b) ** c = {result2}")  # 4096

# 测试2：乘除运算优先级
result3 = a * b / c
result4 = a / b * c
print(f"a * b / c = {result3}")  # 1.5
print(f"a / b * c = {result4}")  # 6666666666666665

# 测试3：加减运算优先级
result5 = a + b - c
result6 = a - b + c
print(f"a + b - c = {result5}")  # 1
print(f"a - b + c = {result6}")  # 3

# 测试4：比较运算优先级
result7 = a + b > c
result8 = a * b == c + 2
print(f"a + b > c = {result7}")  # True
print(f"a * b == c + 2 = {result8}")  # True

# 测试5：逻辑运算优先级
result9 = a > b and b > c
result10 = a < b or b > c
print(f"a > b and b > c = {result9}")  # False
print(f"a < b or b > c = {result10}")  # True
