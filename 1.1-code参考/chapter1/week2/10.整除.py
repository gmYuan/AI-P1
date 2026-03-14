"""

# 正数的整数除法示例
a = 7
b = 2
# 执行整数除法：7 ÷ 2 = 3.5，向下取整得到3
result = a // b
print(f"{a} // {b} = {result}")  # 输出: 7 // 2 = 3

# 负数的整数除法示例
a = -7
b = 2
# 执行整数除法：-7 ÷ 2 = -3.5，向负无穷方向取整得到-4
result = a // b
print(f"{a} // {b} = {result}")  # 输出: -7 // 2 = -4

# 浮点数的整数除法
a = 10.5
b = 3.2
# 执行整数除法：10.5 ÷ 3.2 = 3.28125，向下取整得到3.0
result = a // b
print(f"{a} // {b} = {result}")  # 输出: 10.5 // 3.2 = 3.0


# 场景1：计算页数（每页显示固定数量的项目）
total_items = 25
items_per_page = 10
# 计算需要的页数
pages_needed = (total_items + items_per_page - 1) // items_per_page
print(
    f"总共{total_items}个项目，每页{items_per_page}个，需要{pages_needed}页"
)  # 总共25个项目，每页10个，需要3页

# 场景2：时间转换（秒转换为小时、分钟）
total_seconds = 3661
# 计算小时数
hours = total_seconds // 3600
# 计算剩余分钟数
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
# 计算剩余秒数
seconds = remaining_seconds % 60
print(
    f"{total_seconds}秒 = {hours}小时{minutes}分钟{seconds}秒"
)  # 3661秒 = 1小时1分钟1秒

"""


# 场景1：判断奇偶数
def is_even(number):
    # 如果number % 2 == 0，则为偶数
    return number % 2 == 0


def is_odd(number):
    # 如果number % 2 == 1，则为奇数
    return number % 2 == 1


# 测试奇偶判断
test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in test_numbers:
    if is_even(num):
        print(f"{num} 是偶数")
    else:
        print(f"{num} 是奇数")


# 场景2：循环数组索引
def get_circular_index(index, array_length):
    # 使用取模运算实现循环数组索引
    return index % array_length


# 测试循环数组索引
array_length = 5
indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# array = [10, 6, 7, 8, 9]
print(f"数组长度为{array_length}时的循环索引:")
for idx in indices:
    circular_idx = get_circular_index(idx, array_length)
    print(f"索引{idx} -> 循环索引{circular_idx}")


# 场景3：周期性计算
def get_day_of_week(day_number):
    # 假设0是星期一，计算任意天数后是星期几
    days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return days[day_number % 7]


# 测试周期性计算
for day in range(0, 15):
    weekday = get_day_of_week(day)
    print(f"第{day}天是{weekday}")


# 场景4：二进制转换
def decimal_to_binary(decimal):
    # 将十进制数转换为二进制字符串
    if decimal == 0:
        return "0"

    binary = ""
    while decimal > 0:
        # 使用位运算和幂运算进行转换
        binary = str(decimal % 2) + binary
        decimal = decimal // 2

    return binary


# 测试二进制转换
test_numbers = [0, 1, 5, 10, 15, 255]
for num in test_numbers:
    binary = decimal_to_binary(num)
    print(f"{num} 的二进制表示: {binary}")


# a = (a // b) * b + (a % b)
a=10
b=3
10=3*3+1
