"""
# 定义一个原始字符串
original_string = "hello world"

# 使用replace()方法将"world"替换为"Python"
# replace方法会返回一个新的字符串，原始字符串不会改变
new_string = original_string.replace("world", "Python")

# 打印替换后的新字符串
# 预期输出: hello Python
print(new_string)


# 定义一个包含重复子字符串的文本
text = "hello hello hello"

# 只替换第一个"hello"为"hi"
# count参数设置为1，表示只替换一次
new_text = text.replace("hello", "hi", 1)

# 打印替换后的字符串
# 预期输出: hi hello hello
print(new_text)


# 导入re模块，用于正则表达式操作
import re

# 定义一个包含特定模式的文本
text = "The rain in Spain"

# 使用re.sub()将所有小写字母'a'替换为小写字母'o'
# r'a' 是正则表达式模式，'o' 是替换字符串，text 是原始字符串
new_text = re.sub(r"a", "o", text)

# 打印替换后的字符串
# 预期输出: The roin in Spoin
print(new_text)


# 导入re模块
import re

# 定义一个包含电话号码的文本
text_with_phone = "Contact us at 123-456-7890 or 987-654-3210"

# 使用正则表达式将所有电话号码替换为"XXX-XXX-XXXX"
# \d{3}-\d{3}-\d{4} 匹配格式为XXX-XXX-XXXX的电话号码
masked_text = re.sub(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", text_with_phone)

# 打印替换后的字符串
# 预期输出: Contact us at XXX-XXX-XXXX or XXX-XXX-XXXX
print(masked_text)

# 使用flags参数进行大小写不敏感的替换
text_case = "Hello WORLD, hello world"

# 使用re.IGNORECASE标志，忽略大小写进行替换

case_insensitive_text = re.sub(r"hello", "hi", text_case, flags=re.IGNORECASE)

# 打印替换后的字符串
# 预期输出: hi WORLD, hi world
print(case_insensitive_text)


# 定义一个包含多个替换项的文本
text = "I have an apple and an orange."

# 定义一个字典，键为要替换的旧子字符串，值为替换后的新子字符串
replacements = {"apple": "banana", "orange": "grape"}

# 遍历替换字典中的每一个键值对
# old_substring 是字典的键（要被替换的），new_substring 是字典的值（替换后的）
# Object.entries()
for old_substring, new_substring in replacements.items():
    # 每次循环都用当前替换对更新text字符串
    # 注意：这里text会被连续更新，每次替换都是基于上一次替换后的结果
    text = text.replace(old_substring, new_substring)

# 打印所有替换完成后的最终字符串
# 预期输出: I have a banana and a grape.
print(text)

# 导入re模块
import re

# 定义一个文本，其中包含需要替换的颜色名称（中文）


# 定义一个替换函数，它将根据匹配到的颜色返回新的颜色
# def replace_color(match):
#    print(match)
#    # match.group(0) 获取整个匹配到的字符串（即颜色名称）
#    # 从color_map中查找对应的替换值，如果找不到则返回原始匹配值
#    color = match.group(0)
#    return color_map.get(color, color)
#

# 构建一个正则表达式模式，匹配字典中所有的颜色名称
# keys = color_map.keys()  # ["red","blue","green"]
# print(keys)
# map_result = map(re.escape, keys)  # ["red","blue","green"]
# print(map_result)
# pattern_string = "|".join(map_result)
# print(pattern_string)
# pattern_colors = re.compile(pattern_string)
# print(pattern_colors)
# 使用re.sub()，并将replace_color函数作为替换参数

text_colors = "这些颜色有 red、blue 和 green。"
color_map = {"red": "red2", "blue": "blue2", "green": "green2"}
new_text_colors = re.compile("|".join(map(re.escape, color_map.keys()))).sub(
    lambda match: color_map.get(match.group(0)), text_colors
)
print(new_text_colors)




# 定义一个包含需要替换字符的文本
text_chars = "Hello, World!"

# 创建字符映射表
# str.maketrans() 创建字符映射表，将旧字符映射到新字符
translation_table = str.maketrans("HW", "hw")

# 使用translate()方法进行字符替换
# 将'H'替换为'h'，'W'替换为'w'
translated_text = text_chars.translate(translation_table)

# 打印替换后的字符串
# 预期输出: hello, world!
print(translated_text)

# 更复杂的字符替换示例
text_complex = "Python3 is great! 123 numbers."

# 创建更复杂的映射表
# 将数字替换为'X'，将标点符号替换为空格
complex_table = str.maketrans("0123456789!.,", "XXXXXXXXXX   ")

# 应用字符替换
complex_translated = text_complex.translate(complex_table)

# 打印替换后的字符串
# 预期输出: PythonX is great   XXX numbers
print(complex_translated)



# 场景：清洗用户输入的数据
def clean_user_input(user_input):
    # 定义需要替换的字符映射
    replacements = {
        "  ": " ",  # 将双空格替换为单空格
        "\t": " ",  # 将制表符替换为空格
        "\n": " ",  # 将换行符替换为空格
        "&": " ",  # 将&符号替换为and
        "@": " ",  # 将@符号替换为at
    }

    # 应用所有替换
    cleaned_input = user_input
    for old, new in replacements.items():
        cleaned_input = cleaned_input.replace(old, new)

    # 去除首尾空格
    cleaned_input = cleaned_input.strip()

    return cleaned_input


# 测试数据清洗
dirty_input = "Hello  world\t\n&@test"
clean_result = clean_user_input(dirty_input)
print("清洗前:", repr(dirty_input))
print("清洗后:", repr(clean_result))

"""


# 场景：邮件模板替换
def replace_email_template(template, user_data):
    # 使用字典进行模板变量替换
    for key, value in user_data.items():
        # 将模板中的占位符替换为实际值
        template = template.replace(f"{{{key}}}", str(value))

    return template


# 定义邮件模板
email_template = """
Dear {name},

Thank you for your order #{order_id}.
Your total amount is ${amount}.

Best regards,
Customer Service
"""

# 定义用户数据
user_data = {"name": "Alice", "order_id": "12345", "amount": "99.99"}

# 替换模板
final_email = replace_email_template(email_template, user_data)
print("最终邮件内容:")
print(final_email)
