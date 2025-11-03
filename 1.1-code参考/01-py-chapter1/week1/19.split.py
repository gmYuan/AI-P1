"""
# 例1：按照空格分割
s = "hello                       world python"
print(s.split())  # ['hello', 'world', 'python']

# 例2：按照其它字符分割
data = "2024-06-01"
print(data.split("-"))  # ['2024', '06', '01']

# 例3：使用maxsplit参数
record = "id,name,age,gender"
print(record.split(",", maxsplit=2))  # ['id', 'name', 'age,gender']

# 例4：多种空白字符自动分割
multi_space = "one\t two   three\nfour"
print(multi_space.split())  # ['one', 'two', 'three', 'four']


# 定义一个包含多个分隔符的字符串
text_with_multiple_separators = "a,b,c,d,e,f,g"
print("原始字符串:", text_with_multiple_separators)

# 不指定maxsplit，默认分割所有分隔符
# maxsplit默认为-1，表示不限制分割次数
all_split = text_with_multiple_separators.split(",")
print("全部分割:", all_split)

# 指定maxsplit=2，只分割前2个分隔符
# maxsplit=2表示最多分割2次，得到3个元素
limited_split = text_with_multiple_separators.split(",", maxsplit=2)
print("限制分割次数为2:", limited_split)

# 指定maxsplit=1，只分割1个分隔符
# maxsplit=1表示最多分割1次，得到2个元素
single_split = text_with_multiple_separators.split(",", maxsplit=1)
print("限制分割次数为1:", single_split)

# 使用maxsplit=0，不进行分割
# maxsplit=0表示不分割，返回原字符串
no_split = text_with_multiple_separators.split(",", maxsplit=0)
print("不分割:", no_split)


# 默认分隔符的使用演示
# 当sep=None时，split()会以任意空白字符作为分隔符

# 定义一个包含多种空白字符的字符串
text_with_whitespace = "apple   orange\tbanana\ncherry"
print("包含多种空白字符的字符串:")
print(repr(text_with_whitespace))  # 使用repr显示转义字符

# 不指定分隔符，使用默认的空白字符分割
# 默认会合并连续的空白字符
default_split = text_with_whitespace.split()
print("默认空白字符分割:", default_split)

# 指定空格作为分隔符
# 这样不会合并连续的空白字符
space_split = text_with_whitespace.split(" ")
print("指定空格分割:", space_split)

# 指定制表符作为分隔符
tab_split = text_with_whitespace.split("\t")
print("指定制表符分割:", tab_split)

# 指定换行符作为分隔符
newline_split = text_with_whitespace.split("\n")
print("指定换行符分割:", newline_split)


# 使用正则表达式进行复杂分割
import re

# 定义一个包含多种分隔符的复杂字符串
complex_text = "apple,banana;orange:grape|kiwi"
print("复杂分隔符字符串:", complex_text)

# 使用正则表达式分割多种分隔符
# 正则表达式'[,;:|]'表示匹配逗号、分号、冒号或竖线
regex_split = re.split("[,;:|]", complex_text)
print("正则表达式分割:", regex_split)

# 保留分隔符的分割
# 使用捕获组()来保留分隔符
regex_split_with_separators = re.split("([,;:|])", complex_text)
print("保留分隔符的分割:", regex_split_with_separators)

# 使用正则表达式分割空白字符
text_with_mixed_whitespace = "apple  \t  orange\n\nbanana"
print("\n混合空白字符字符串:")
print(repr(text_with_mixed_whitespace))

# 使用正则表达式分割一个或多个空白字符
regex_whitespace_split = re.split(r"\s+", text_with_mixed_whitespace)
print("正则表达式空白字符分割:", regex_whitespace_split)

# 使用正则表达式分割，限制分割次数
regex_limited_split = re.split(r"\s+", text_with_mixed_whitespace, maxsplit=1)
print("正则表达式限制分割次数:", regex_limited_split)


# 语法：separator.join(iterable)

# 定义一个包含字符串元素的列表
fruits = ["apple", "banana", "orange", "grape"]
print("字符串列表:", fruits)

# 使用逗号作为分隔符将列表元素连接成一个字符串
# separator是逗号，iterable是fruits列表
comma_joined = ",".join(fruits)
print("逗号连接:", comma_joined)

# 使用空格作为分隔符连接
space_joined = " ".join(fruits)
print("空格连接:", space_joined)

# 使用连字符作为分隔符连接
hyphen_joined = "-".join(fruits)
print("连字符连接:", hyphen_joined)

# 使用空字符串作为分隔符连接（无分隔符）
no_separator_joined = "".join(fruits)
print("无分隔符连接:", no_separator_joined)

# 使用多字符作为分隔符连接
multi_char_joined = " | ".join(fruits)
print("多字符分隔符连接:", multi_char_joined)
"""

# 列表
list_fruits = ["apple", "banana", "orange"]
list_joined = ", ".join(list_fruits)
print("列表连接:", list_joined)

# 元组
tuple_fruits = ("apple", "banana", "orange")
tuple_joined = ", ".join(tuple_fruits)
print("元组连接:", tuple_joined)

# 集合（注意：集合是无序的）
set_fruits = {"apple", "banana", "orange"}
set_joined = ", ".join(set_fruits)
print("集合连接:", set_joined)

# 字符串（字符串也是可迭代对象）
string_chars = "hello"
string_joined = "-".join(string_chars)
print("字符串字符连接:", string_joined)

# 生成器表达式
numbers = [1, 2, 3, 4, 5]
# 将数字转换为字符串后连接
numbers_joined = ", ".join(str(num) for num in numbers)
print("数字列表连接:", numbers_joined)

# 列表推导式
words = ["hello", "world", "python"]
# 将单词转换为大写后连接
upper_joined = " ".join(word.upper() for word in words)
print("大写单词连接:", upper_joined)
