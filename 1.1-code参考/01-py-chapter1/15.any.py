"""
# 测试全为假值的情况
# 创建包含假值的列表
falsy_list = [0, False, None]
# 使用any()检查是否有真值
print(f"any([0, False, None]): {any(falsy_list)}")  # 输出: False

# 测试包含真值的情况
# 创建包含真值的列表
mixed_list = [0, 1, False]
# 使用any()检查是否有真值
print(f"any([0, 1, False]): {any(mixed_list)}")  # 输出: True

# 测试空列表的情况
# 创建空列表
empty_list = []
# 使用any()检查空列表
print(f"any([]): {any(empty_list)}")  # 输出: False

# 测试空字符串的情况
# 创建包含空字符串的列表
empty_string_list = [""]
# 使用any()检查空字符串
print(f"any(['']): {any(empty_string_list)}")  # 输出: False

# 测试字符串的情况
# 创建包含非空字符串的列表
string_list = ["hello", "", "world"]
# 使用any()检查字符串列表
print(f"any(['hello', '', 'world']): {any(string_list)}")  # 输出: True

# 测试数字的情况
# 创建包含数字的列表
number_list = [0, 0.0, 0j, 1, 2, 3]
# 使用any()检查数字列表
print(f"any([0, 0.0, 0j, 1, 2, 3]): {any(number_list)}")  # 输出: True


# 测试全为真值的情况
# 创建包含真值的列表
truthy_list = [1, 2, 3]
# 使用all()检查是否所有值都为真
print(f"all([1, 2, 3]): {all(truthy_list)}")  # 输出: True

# 测试包含假值的情况
# 创建包含假值的列表
mixed_list = [0, 1, 2]
# 使用all()检查是否所有值都为真
print(f"all([0, 1, 2]): {all(mixed_list)}")  # 输出: False

# 测试空列表的情况
# 创建空列表
empty_list = []
# 使用all()检查空列表（空集合被认为是"所有条件都满足"）
print(f"all([]): {all(empty_list)}")  # 输出: True

# 测试包含假值的列表
# 创建包含假值的列表
falsy_mixed_list = [1, 0, False]
# 使用all()检查是否所有值都为真
print(f"all([1, 0, False]): {all(falsy_mixed_list)}")  # 输出: False

# 测试字符串的情况
# 创建包含非空字符串的列表
string_list = ["hello", "world", "python"]
# 使用all()检查字符串列表
print(f"all(['hello', 'world', 'python']): {all(string_list)}")  # 输出: True

# 测试包含空字符串的列表
# 创建包含空字符串的列表
empty_string_list = ["hello", "", "world"]
# 使用all()检查包含空字符串的列表
print(f"all(['hello', '', 'world']): {all(empty_string_list)}")  # 输出: False



# 定义测试函数，用于观察短路求值行为
def test_function(value):
    # 打印函数调用信息
    print(f"  调用 test_function({value})")
    # 返回值的布尔表示
    return bool(value)


# 测试any()的短路求值
# 创建测试列表
test_list = [0, 1, 2, 3]
# 打印any()测试标题
print("any() 短路求值测试：")
# 使用any()和map()测试短路求值
result = any(map(lambda x: test_function(x), test_list))
# 打印any()的结果
print(f"结果: {result}")

# 测试all()的短路求值
# 创建包含假值的测试列表
test_list2 = [1, 0, 2, 3]
# 打印all()测试标题
print("\nall() 短路求值测试：")
# 使用all()和map()测试短路求值
result2 = all(map(lambda x: test_function(x), test_list2))
# 打印all()的结果
print(f"结果: {result2}")
"""


def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False


def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
