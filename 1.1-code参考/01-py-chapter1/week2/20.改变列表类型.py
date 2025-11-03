"""

# 定义一个包含不同数据类型的原始列表
original_list_str = [1, 2.5, "aaa", True]
# ValueError: could not convert string to float: 'aaa'
# 使用列表推导式将原始列表中的所有元素转换为字符串类型
# string_list = [float(item) for item in original_list_str]
# 打印转换后的列表，验证所有元素是否都已变为字符串
# print(f"转换为字符串后的列表: {string_list}")
# 预期输出: ['1', '2.5', '3', 'True']


def safe_convert_to_int(item):
    try:
        return int(item)
    except (ValueError, TypeError):
        return None


def safe_convert_to_int_with_default(item):
    try:
        return int(item)
    except (ValueError, TypeError):
        return 0


original_list_str = [1, 2.5, "aaa", True]

int_list = [safe_convert_to_int_with_default(item) for item in original_list_str]
print(int_list)


# 布尔值转换规则
bool_values = [True, False]
# 布尔值转整数：True转换为1，False转换为0
bool_to_int = [int(b) for b in bool_values]
print(f"布尔值转整数: {bool_to_int}")

# 布尔值转字符串
bool_to_str = [str(b) for b in bool_values]
print(f"布尔值转字符串: {bool_to_str}")

# 浮点数转整数规则
float_values = [3.7, 2.1, 5.9]
# 浮点数转整数：会截断小数部分，只保留整数部分
float_to_int = [int(f) for f in float_values]
print(f"浮点数转整数: {float_to_int}")

# 字符串转数字规则
str_numbers = ["123", "45", "0", "-10"]
# 字符串转整数（必须是有效的整数表示）
str_to_int = [int(s) for s in str_numbers]
print(f"字符串转整数: {str_to_int}")

# 字符串转浮点数
str_to_float = [float(s) for s in str_numbers]
print(f"字符串转浮点数: {str_to_float}")


# 定义一个包含不同数据类型的原始列表
original_list_map = [1, 2.5, "3", True]
# 使用map()函数将str类型应用于original_list_map中的每个元素
# map()返回一个迭代器，需要用list()将其转换为列表
string_list_map = list(map(str, original_list_map))
# 打印使用map()函数转换后的列表
print(f"使用map()转换为字符串后的列表: {string_list_map}")
# 预期输出: ['1', '2.5', '3', 'True']

# 使用map()进行其他类型转换
int_list_map = list(map(int, ["1", "2", "3", "4"]))
print(f"使用map()转换为整数后的列表: {int_list_map}")


# 使用map()与自定义函数
def custom_converter(x):

    # 如果是字符串，尝试转换为整数
    if isinstance(x, str) and x.isdigit():
        return int(x)
    # 如果是数字，转换为字符串
    elif isinstance(x, (int, float)):
        return str(x)
    # 其他情况返回原值
    else:
        return x


# 使用自定义转换函数
custom_list = [1, "2", 3.0, "hello", True]
custom_result = list(map(custom_converter, custom_list))
print(f"使用自定义函数转换后的列表: {custom_result}")


# 定义一个包含嵌套列表和字典的复杂原始数据结构
original_list_nested = [1, [2.5, "3"], {"key": True, "nested_list": [4, "five"]}]


# 定义一个递归函数，用于将嵌套结构中的所有基本元素转换为字符串
def recursive_str_convert(item):
    # 如果当前元素是列表类型
    if isinstance(item, list):
        # 递归地处理列表中的每一个元素，并返回一个新的列表
        return [recursive_str_convert(elem) for elem in item]
    # 如果当前元素是字典类型
    elif isinstance(item, dict):
        # 递归地处理字典中的每一个键值对，将值转换为字符串，并返回一个新的字典
        return {k: recursive_str_convert(v) for k, v in item.items()}
    # 如果当前元素既不是列表也不是字典（即基本类型）
    else:
        # 将基本类型元素转换为字符串并返回
        return str(item)


# 调用递归函数对原始的嵌套列表进行转换
string_list_nested = recursive_str_convert(original_list_nested)
# 打印转换后的嵌套列表，所有基本元素都已变为字符串
print(f"递归转换为字符串后的嵌套列表: {string_list_nested}")
# 预期输出: ['1', ['2.5', '3'], {'key': 'True', 'nested_list': ['4', 'five']}]
"""

# 定义一个包含多种类型元素的列表
mixed_list = [1, "2", 3.5, "hello", 4, "world", 5.7]


# 只转换数字类型的元素为字符串
def convert_numbers_to_string(item):
    """
    只将数字类型的元素转换为字符串
    """
    # 如果是数字类型（整数或浮点数）
    if isinstance(item, (int, float)):
        return str(item)
    # 其他类型保持原样
    else:
        return item


# 使用条件转换
conditional_result = [convert_numbers_to_string(item) for item in mixed_list]
print(f"条件转换结果: {conditional_result}")


# 使用列表推导式进行更复杂的条件转换
def is_numeric_string(item):
    """
    检查字符串是否表示数字
    """
    if isinstance(item, str):
        try:
            float(item)
            return True
        except ValueError:
            return False
    return False


# 只转换数字字符串为浮点数
numeric_strings_to_float = [
    float(item) if is_numeric_string(item) else item for item in mixed_list
]
print(f"数字字符串转浮点数: {numeric_strings_to_float}")

# isInstance 还能判断元组里的每个类型？
