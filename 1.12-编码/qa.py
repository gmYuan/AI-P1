

"""
# -------------------------------------------------------------------------------
1.12-1.1 str既是类型，也可以是工具函数

print(type("hello"))  # <class 'str'>

"""




"""
# -------------------------------------------------------------------------------
1.12-2.1 码点（字符在unicode中的编号）和 字符编码

char = "中"
print(ord(char))
print(char.encode("utf-8"))


# 转化为码点 展示
char_unicode = 255  # FF
print(f"U+{char_unicode:04X}")

"""



"""
# -------------------------------------------------------------------------------
1.12-2.2 编码错误处理

# UnicodeEncodeError: 'ascii' codec can't encode characters in position 6-7: ordinal not in range(128)
# 如果遇到不识别无法编码的字符就替换成?
print("Hello 世界".encode("ascii", errors="replace"))

"""
