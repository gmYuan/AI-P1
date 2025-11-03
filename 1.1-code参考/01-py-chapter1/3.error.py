"""
# 定义一个包含姓名和年龄的字典
my_dict = {"name": "Alice", "age": 25}

# 尝试访问字典中不存在的键 'gender'
# 这将导致 KeyError，因为字典中没有名为 'gender' 的键
try:
    print(my_dict["gender"])  # KeyError: 'gender'
except KeyError:
    print(f"错误：尝试访问不存在的键")


# 定义一个包含姓名和年龄的字典
my_dict = {"name": "Alice", "age": 25}

# 使用 get() 方法访问存在的键 'name'
# 如果键存在，返回对应的值 'Alice'
print(f"姓名: {my_dict.get('name')}")

# 使用 get() 方法访问不存在的键 'gender'
# 并提供一个默认值 '未知'，如果键不存在则返回 '未知'
print(f"性别: {my_dict.get('gender', '未知')}")

# 使用 get() 方法访问不存在的键 'city'
# 不提供默认值，如果键不存在将返回 None
print(f"城市: {my_dict.get('city')}")


# 尝试将一个字符串 '3' 和一个整数 4 相加
# 字符串和整数之间不支持 '+' 运算符，这将导致 TypeError
result = int("3") + 4
print(result)  # TypeError: can only concatenate str (not "int") to str


# 定义一个变量，其类型可能不确定
some_variable_int = 10
some_variable_str = "hello"
some_variable_list = [1, 2, 3]

# 检查 some_variable_int 是否是整数类型
# 如果是整数，则打印相应信息
# isinstance判断某个变量是不是一个对应的类型
if isinstance(some_variable_int, int):
    print(f"'{some_variable_int}' 是一个整数！")
else:
    print(f"'{some_variable_int}' 不是一个整数。")

# 检查 some_variable_str 是否是整数类型
# 如果不是整数，则打印相应信息
if isinstance(some_variable_str, int):
    print(f"'{some_variable_str}' 是一个整数！")
else:
    print(f"'{some_variable_str}' 不是一个整数。")

# 检查 some_variable_list 是否是列表类型
# 如果是列表，则打印相应信息
if isinstance(some_variable_list, list):
    print(f"'{some_variable_list}' 是一个列表！")
else:
    print(f"'{some_variable_list}' 不是一个列表。")


# 示例：安全地进行加法操作
def safe_add(a, b):
    # 检查两个参数是否都是整数或浮点数
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # 如果类型兼容，执行加法并返回结果
        return a + b
    else:
        # 如果类型不兼容，打印错误信息并返回 None
        print(
            f"错误：参数类型不兼容，无法执行加法。a类型: {type(a).__name__}, b类型: {type(b).__name__}"
        )
        return None


# 调用安全加法函数，传入兼容类型
print(f"安全加法 (1, 2): {safe_add(1, 2)}")
# 调用安全加法函数，传入不兼容类型
print(f"安全加法 ('1', 2): {safe_add('1', 2)}")


# 尝试将一个非数字的字符串 'abc' 转换为整数
# 字符串 'abc' 的类型是正确的（str），但其值无法被解释为整数
# 这将导致 ValueError
num = int("abc")
print(num)  # ValueError: invalid literal for int() with base 10: 'abc'

"""

# 定义一个可能包含非数字字符的字符串
input_string_valid = "123"
input_string_invalid = "abc"
input_string_float = "3.14"

# 验证 input_string_valid 是否只包含数字
if input_string_valid.isdigit():
    # 如果是，则将其转换为整数并打印
    num = int(input_string_valid)
    print(f"'{input_string_valid}' 转换为整数: {num}")
else:
    # 如果不是，则打印错误信息
    print(f"'{input_string_valid}' 是无效输入，不是一个纯数字。")

# 验证 input_string_invalid 是否只包含数字
if input_string_invalid.isdigit():
    # 如果是，则将其转换为整数并打印
    num = int(input_string_invalid)
    print(f"'{input_string_invalid}' 转换为整数: {num}")
else:
    # 如果不是，则打印错误信息
    print(f"'{input_string_invalid}' 是无效输入，不是一个纯数字。")

# 注意：isdigit() 不会识别浮点数（如 '3.14'），如果需要处理浮点数，需要更复杂的验证
# 验证 input_string_float 是否只包含数字
if input_string_float.isdigit():
    # 如果是，则将其转换为整数并打印
    num = int(input_string_float)
    print(f"'{input_string_float}' 转换为整数: {num}")
else:
    # 如果不是，则打印错误信息
    print(f"'{input_string_float}' 是无效输入，不是一个纯数字。")


# 更通用的数值转换验证（使用 try-except）
def safe_int_convert(s):
    # 尝试在 try 块中进行类型转换
    try:
        # 尝试将字符串转换为整数
        return int(s)
    # 如果发生 ValueError
    except (KeyError, TypeError, ValueError):
        # 打印错误信息并返回 None
        print(f"错误：无法将 '{s}' 转换为整数。")
        return None


# 调用安全转换函数，传入可转换的字符串
print(f"安全转换 ('123'): {safe_int_convert('123')}")  # 123
# 调用安全转换函数，传入不可转换为整数的字符串
print(f"安全转换 ('abc'): {safe_int_convert('abc')}")  # None
# 调用安全转换函数，传入浮点数字符串（int() 无法直接转换）
print(f"安全转换 ('3.14'): {safe_int_convert('3.14')}")  # None

None
# 昨天的join函数也是不能"3".join(4) 也是要转换#
# TypeError: can only join an iterable join只能连接可迭代对象
# print("3".join(4))
# isinstance支持多个类型传入判断这个功能比js好，省得写那么多
str = "abc"
if isinstance(str, (int, float)):
    print("是整形或者浮点数")


print("3".join("4"))
