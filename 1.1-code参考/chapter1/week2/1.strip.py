"""
# 定义一个包含前置空格的字符串
my_string = "   Hello, World!"
print("原始字符串:")
print(f"'{my_string}'")

# 使用lstrip()删除前置空格
trimmed_string = my_string.lstrip()
print("\n使用lstrip()处理后:")
print(f"'{trimmed_string}'")

# 验证空格是否被删除
print(f"\n原始字符串长度: {len(my_string)}")
print(f"处理后字符串长度: {len(trimmed_string)}")
print(f"删除的空格数量: {len(my_string) - len(trimmed_string)}")

# 处理不同类型的空白字符
print("\n=== 处理不同类型的空白字符 ===")
# 包含空格、制表符、换行符的字符串
mixed_whitespace = " \t\n  Hello, World!"
print(f"混合空白字符字符串: '{mixed_whitespace}'")
print(f"混合空白字符字符串长度: {len(mixed_whitespace)}")

# 使用lstrip()删除所有前置空白字符
cleaned_string = mixed_whitespace.lstrip()
print(f"清理后字符串: '{cleaned_string}'")
print(f"清理后字符串长度: {len(cleaned_string)}")


# \t有可能对应2个空格，也有可能对应4个空格 tabSize=4
print("姓名\t年龄\t成绩")
print("张三\t十八   九十")


# 删除特定的前置字符
text_with_prefix = "xxxHello, World!"
print(f"原始字符串: '{text_with_prefix}'")

# 删除所有前置的'x'字符
cleaned_text = text_with_prefix.lstrip("x")
print(f"删除'x'后: '{cleaned_text}'")

# 删除多个不同的前置字符
text_with_multiple = "aabbccHello, World!"
print(f"\n原始字符串: '{text_with_multiple}'")

# 删除前置的'a'、'b'、'c'字符 注意参数是一个字符的集合{a,b,c} 类似于正则里的[abc]
cleaned_multiple = text_with_multiple.lstrip("abc")
print(f"删除'abc'后: '{cleaned_multiple}'")

# 删除数字字符
text_with_numbers = "123Hello, World!"
print(f"\n原始字符串: '{text_with_numbers}'")

# 删除前置的数字字符
cleaned_numbers = text_with_numbers.lstrip("0123456789")
print(f"删除数字后: '{cleaned_numbers}'")

# 删除标点符号
text_with_punctuation = "!!!Hello, World!"
print(f"\n原始字符串: '{text_with_punctuation}'")

# 删除前置的感叹号
cleaned_punctuation = text_with_punctuation.lstrip("!")
print(f"删除感叹号后: '{cleaned_punctuation}'")



# 删除标点符号
text_with_punctuation = "cba Hello a world"
print(f"\n原始字符串: '{text_with_punctuation}'")

# 删除前置的感叹号
cleaned_punctuation = text_with_punctuation.lstrip("abc")
print(f"删除感叹号后: '{cleaned_punctuation}'")



# 定义一个包含后置空格的字符串
my_string = "Hello, World!   "
print("原始字符串:")
print(f"'{my_string}'")

# 使用rstrip()删除后置空格
trimmed_string = my_string.rstrip()
print("\n使用rstrip()处理后:")
print(f"'{trimmed_string}'")

# 验证空格是否被删除
print(f"\n原始字符串长度: {len(my_string)}")
print(f"处理后字符串长度: {len(trimmed_string)}")
print(f"删除的空格数量: {len(my_string) - len(trimmed_string)}")

# 处理不同类型的空白字符
print("\n=== 处理不同类型的空白字符 ===")
# 包含空格、制表符、换行符的字符串
mixed_whitespace = "Hello, World! \t\n  "
print(f"混合空白字符字符串: '{mixed_whitespace}'")
print(f"混合空白字符字符串长度: {len(mixed_whitespace)}")

# 使用rstrip()删除所有后置空白字符
cleaned_string = mixed_whitespace.rstrip()
print(f"清理后字符串: '{cleaned_string}'")
print(f"清理后字符串长度: {len(cleaned_string)}")


# rstrip()方法支持自定义字符删除
print("=== rstrip()自定义字符删除 ===")

# 删除特定的后置字符
text_with_suffix = "Hello, World!xxx"
print(f"原始字符串: '{text_with_suffix}'")

# 删除所有后置的'x'字符
cleaned_text = text_with_suffix.rstrip("x")
print(f"删除'x'后: '{cleaned_text}'")

# 删除多个不同的后置字符
text_with_multiple = "Hello, World!cba"
print(f"\n原始字符串: '{text_with_multiple}'")

# 删除后置的'a'、'b'、'c'字符
cleaned_multiple = text_with_multiple.rstrip("abc")
print(f"删除'abc'后: '{cleaned_multiple}'")

# 删除数字字符
text_with_numbers = "Hello, World!123"
print(f"\n原始字符串: '{text_with_numbers}'")

# 删除后置的数字字符
cleaned_numbers = text_with_numbers.rstrip("0123456789")
print(f"删除数字后: '{cleaned_numbers}'")

# 删除标点符号
text_with_punctuation = "Hello, World!!!"
print(f"\n原始字符串: '{text_with_punctuation}'")

# 删除后置的感叹号
cleaned_punctuation = text_with_punctuation.rstrip("!")
print(f"删除感叹号后: '{cleaned_punctuation}'")


# 定义一个包含前置和后置空格的字符串
my_string = "   Hello, World!   "
print("原始字符串:")
print(f"'{my_string}'")

# 使用strip()删除两端的空格
trimmed_string = my_string.strip()
print("\n使用strip()处理后:")
print(f"'{trimmed_string}'")

# 验证空格是否被删除
print(f"\n原始字符串长度: {len(my_string)}")
print(f"处理后字符串长度: {len(trimmed_string)}")
print(f"删除的空格数量: {len(my_string) - len(trimmed_string)}")

# 处理不同类型的空白字符
print("\n=== 处理不同类型的空白字符 ===")
# 包含空格、制表符、换行符的字符串
mixed_whitespace = " \t\n  Hello, World! \t\n  "
print(f"混合空白字符字符串: '{mixed_whitespace}'")
print(f"混合空白字符字符串长度: {len(mixed_whitespace)}")

# 使用strip()删除两端的空白字符
cleaned_string = mixed_whitespace.strip()
print(f"清理后字符串: '{cleaned_string}'")
print(f"清理后字符串长度: {len(cleaned_string)}")

"""

# 定义一个包含前置和后置空格的字符串
my_string = "aabcHello, World!   "
print("原始字符串:")
print(f"'{my_string}'")

# 使用strip()删除两端的空格
trimmed_string = my_string.strip("abc")
print("\n使用strip()处理后:")
print(f"'{trimmed_string}'")
