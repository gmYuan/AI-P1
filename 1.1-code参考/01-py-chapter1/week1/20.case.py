"""
# 定义一个包含大写字母的字符串
string = "Hello, World!"
print("原始字符串:")
print(f"'{string}'")

# 使用lower()方法转换为小写
lowercase_string = string.lower()
print("\n使用lower()转换后:")
print(f"'{lowercase_string}'")

# 验证转换结果
print(f"\n原始字符串长度: {len(string)}")
print(f"转换后字符串长度: {len(lowercase_string)}")
print(f"字符串是否发生变化: {string != lowercase_string}")

# 处理不同类型的字符串
print("\n=== 处理不同类型的字符串 ===")

# 全大写字符串
upper_string = "PYTHON PROGRAMMING"
print(f"全大写字符串: '{upper_string}'")
print(f"转换为小写: '{upper_string.lower()}'")

# 混合大小写字符串
mixed_string = "PyThOn PrOgRaMmInG"
print(f"混合大小写字符串: '{mixed_string}'")
print(f"转换为小写: '{mixed_string.lower()}'")

# 包含数字和特殊字符的字符串
special_string = "Hello123!@#World"
print(f"包含特殊字符的字符串: '{special_string}'")
print(f"转换为小写: '{special_string.lower()}'")

# 已经是小写的字符串
already_lower = "hello world"
print(f"已经小写的字符串: '{already_lower}'")
print(f"转换为小写: '{already_lower.lower()}'")


# 定义一个包含小写字母的字符串
string = "Hello, World!"
print("原始字符串:")
print(f"'{string}'")

# 使用upper()方法转换为大写
uppercase_string = string.upper()
print("\n使用upper()转换后:")
print(f"'{uppercase_string}'")

# 验证转换结果
print(f"\n原始字符串长度: {len(string)}")
print(f"转换后字符串长度: {len(uppercase_string)}")
print(f"字符串是否发生变化: {string != uppercase_string}")

# 处理不同类型的字符串
print("\n=== 处理不同类型的字符串 ===")

# 全小写字符串
lower_string = "python programming"
print(f"全小写字符串: '{lower_string}'")
print(f"转换为大写: '{lower_string.upper()}'")

# 混合大小写字符串
mixed_string = "PyThOn PrOgRaMmInG"
print(f"混合大小写字符串: '{mixed_string}'")
print(f"转换为大写: '{mixed_string.upper()}'")

# 包含数字和特殊字符的字符串
special_string = "hello123!@#world"
print(f"包含特殊字符的字符串: '{special_string}'")
print(f"转换为大写: '{special_string.upper()}'")

# 已经是大写的字符串
already_upper = "HELLO WORLD"
print(f"已经大写的字符串: '{already_upper}'")
print(f"转换为大写: '{already_upper.upper()}'")


# 定义一个字符串
string = "hello, world!"
print("原始字符串:")
print(f"'{string}'")

# 使用capitalize()方法转换
capitalized_string = string.capitalize()
print("\n使用capitalize()转换后:")
print(f"'{capitalized_string}'")

# 验证转换结果
print(f"\n原始字符串长度: {len(string)}")
print(f"转换后字符串长度: {len(capitalized_string)}")
print(f"字符串是否发生变化: {string != capitalized_string}")

# 处理不同类型的字符串
print("\n=== 处理不同类型的字符串 ===")

# 全小写字符串
lower_string = "python programming"
print(f"全小写字符串: '{lower_string}'")
print(f"首字母大写: '{lower_string.capitalize()}'")

# 全大写字符串
upper_string = "PYTHON PROGRAMMING"
print(f"全大写字符串: '{upper_string}'")
print(f"首字母大写: '{upper_string.capitalize()}'")

# 混合大小写字符串
mixed_string = "PyThOn PrOgRaMmInG"
print(f"混合大小写字符串: '{mixed_string}'")
print(f"首字母大写: '{mixed_string.capitalize()}'")

# 已经是首字母大写的字符串
already_capitalized = "Hello world"
print(f"已经首字母大写的字符串: '{already_capitalized}'")
print(f"首字母大写: '{already_capitalized.capitalize()}'")

# 空字符串和单字符字符串
empty_string = ""
single_char = "a"
print(f"空字符串: '{empty_string}' -> '{empty_string.capitalize()}'")
print(f"单字符字符串: '{single_char}' -> '{single_char.capitalize()}'")


# 定义一个字符串
string = "hello, world!"
print("原始字符串:")
print(f"'{string}'")

# 使用title()方法转换
title_string = string.title()
print("\n使用title()转换后:")
print(f"'{title_string}'")

# 验证转换结果
print(f"\n原始字符串长度: {len(string)}")
print(f"转换后字符串长度: {len(title_string)}")
print(f"字符串是否发生变化: {string != title_string}")

# 处理不同类型的字符串
print("\n=== 处理不同类型的字符串 ===")

# 全小写字符串
lower_string = "python programming language"
print(f"全小写字符串: '{lower_string}'")
print(f"标题格式: '{lower_string.title()}'")

# 全大写字符串
upper_string = "PYTHON PROGRAMMING LANGUAGE"
print(f"全大写字符串: '{upper_string}'")
print(f"标题格式: '{upper_string.title()}'")

# 混合大小写字符串
mixed_string = "PyThOn PrOgRaMmInG LaNgUaGe"
print(f"混合大小写字符串: '{mixed_string}'")
print(f"标题格式: '{mixed_string.title()}'")

# 包含数字和特殊字符的字符串
special_string = "hello123 world456!@#"
print(f"包含特殊字符的字符串: '{special_string}'")
print(f"标题格式: '{special_string.title()}'")

# 已经是标题格式的字符串
already_title = "Hello World"
print(f"已经标题格式的字符串: '{already_title}'")
print(f"标题格式: '{already_title.title()}'")


# 定义一个包含特殊字符的字符串
string = "straße"
print("原始字符串:")
print(f"'{string}'")

# 使用casefold()方法转换
casefold_string = string.casefold()
print("\n使用casefold()转换后:")
print(f"'{casefold_string}'")

# 验证转换结果
print(f"\n原始字符串长度: {len(string)}")
print(f"转换后字符串长度: {len(casefold_string)}")
print(f"字符串是否发生变化: {string != casefold_string}")

# 处理不同类型的字符串
print("\n=== 处理不同类型的字符串 ===")

# 德语字符串
german_string = "Grüße"
print(f"德语字符串: '{german_string}'")
print(f"casefold转换: '{german_string.casefold()}'")

# 法语字符串
french_string = "Café"
print(f"法语字符串: '{french_string}'")
print(f"casefold转换: '{french_string.casefold()}'")

# 土耳其语字符串
turkish_string = "İstanbul"
print(f"土耳其语字符串: '{turkish_string}'")
print(f"casefold转换: '{turkish_string.casefold()}'")

# 希腊语字符串
greek_string = "ΣΟΦΙΑ"
print(f"希腊语字符串: '{greek_string}'")
print(f"casefold转换: '{greek_string.casefold()}'")

# 普通英文字符串
english_string = "Hello, World!"
print(f"英文字符串: '{english_string}'")
print(f"casefold转换: '{english_string.casefold()}'")
"""
