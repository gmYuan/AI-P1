"""
# 定义一个二进制数，前缀为0b
# 二进制1010表示十进制10
binary_num = 0b1010
# 打印二进制数的十进制表示
print(f"二进制 0b1010 = {binary_num}")

# 定义一个八进制数，前缀为0o
# 八进制12表示十进制10
octal_num = 0o12
# 打印八进制数的十进制表示
print(f"八进制 0o12 = {octal_num}")

# 定义一个十六进制数，前缀为0x   0123456789ABCDEF
# 十六进制A表示十进制10
hexadecimal_num = 0xA
# 打印十六进制数的十进制表示
print(f"十六进制 0xA = {hexadecimal_num}")

# 验证所有进制表示相同的值
print(f"验证: {binary_num == octal_num == hexadecimal_num}")

# 示例2: 不同进制的较大数字
# 定义较大的数字
large_binary = 0b11111111  # 255
large_octal = 0o377  # 255=  7+56+64*3=
large_hex = 0xFF  # 255 =15+15*16

print(f"\n较大数字示例:")
print(f"二进制 0b11111111 = {large_binary}")
print(f"八进制 0o377 = {large_octal}")
print(f"十六进制 0xFF = {large_hex}")
print(f"验证: {large_binary == large_octal == large_hex}")

# 示例3: 负数表示
# 定义负数
negative_binary = -0b1010  # -10
negative_octal = -0o12  # -10
negative_hex = -0xA  # -10

print(f"\n负数示例:")
print(f"负二进制 -0b1010 = {negative_binary}")
print(f"负八进制 -0o12 = {negative_octal}")
print(f"负十六进制 -0xA = {negative_hex}")
print(f"验证: {negative_binary == negative_octal == negative_hex}")

# 定义不同进制的字符串
binary_str = "1010"
octal_str = "12"
hex_str = "A"
decimal_str = "10"

print(f"二进制字符串: {binary_str}")
print(f"八进制字符串: {octal_str}")
print(f"十六进制字符串: {hex_str}")
print(f"十进制字符串: {decimal_str}")

# 注意：字符串形式的数字不能直接进行数学运算
# 需要先转换为整数类型
print(f"\n字符串类型检查:")
print(f"binary_str 的类型: {type(binary_str)}")
print(f"0b1010 的类型: {type(0b1010)}")


# 示例1: 使用int()函数转换
# 定义一个二进制数字的字符串表示
binary_str = "1010"
# 使用int()函数将二进制字符串转换为十进制整数，基数为2
decimal_from_binary = int(binary_str, 2)
# 打印转换后的十进制结果
print(f"二进制 '{binary_str}' 转换为十进制: {decimal_from_binary}")

# 定义一个八进制数字的字符串表示
octal_str = "12"
# 使用int()函数将八进制字符串转换为十进制整数，基数为8
decimal_from_octal = int(octal_str, 8)
# 打印转换后的十进制结果
print(f"八进制 '{octal_str}' 转换为十进制: {decimal_from_octal}")

# 定义一个十六进制数字的字符串表示
hex_str = "A"
# 使用int()函数将十六进制字符串转换为十进制整数，基数为16
decimal_from_hex = int(hex_str, 16)
# 打印转换后的十进制结果
print(f"十六进制 '{hex_str}' 转换为十进制: {decimal_from_hex}")

# 示例2: 转换不同进制的较大数字
# 定义较大的数字字符串
large_binary_str = "11111111"  # 255
large_octal_str = "377"  # 255
large_hex_str = "FF"  # 255

print(f"\n较大数字转换:")
print(f"二进制 '{large_binary_str}' = {int(large_binary_str, 2)}")
print(f"八进制 '{large_octal_str}' = {int(large_octal_str, 8)}")
print(f"十六进制 '{large_hex_str}' = {int(large_hex_str, 16)}")

# 示例3: 转换负数
# 定义负数字符串
negative_binary_str = "-1010"
negative_octal_str = "-12"
negative_hex_str = "-A"

print(f"\n负数转换:")
print(f"负二进制 '{negative_binary_str}' = {int(negative_binary_str, 2)}")
print(f"负八进制 '{negative_octal_str}' = {int(negative_octal_str, 8)}")
print(f"负十六进制 '{negative_hex_str}' = {int(negative_hex_str, 16)}")

# 示例4: 自定义进制转换
# 使用int()函数可以转换任意进制的数字
custom_base_str = "123"  # 3+10+25=
# 转换为5进制
decimal_from_custom = int(custom_base_str, 5)
#
print(f"\n自定义进制转换:")
print(f"5进制 '{custom_base_str}' = {decimal_from_custom}")


# 示例1: 使用内置函数转换
# 定义一个十进制整数
decimal_num = 10

# 将十进制数转换为二进制字符串
binary_rep = bin(decimal_num)
# 打印二进制字符串，包含'0b'前缀
print(f"十进制 {decimal_num} 转换为二进制: {binary_rep}")

# 将十进制数转换为八进制字符串
octal_rep = oct(decimal_num)
# 打印八进制字符串，包含'0o'前缀
print(f"十进制 {decimal_num} 转换为八进制: {octal_rep}")

# 将十进制数转换为十六进制字符串
hex_rep = hex(decimal_num)
# 打印十六进制字符串，包含'0x'前缀
print(f"十进制 {decimal_num} 转换为十六进制: {hex_rep}")

# 示例2: 转换较大的数字
# 定义较大的十进制数
large_decimal = 255

print(f"\n较大数字转换:")
print(f"十进制 {large_decimal} 转换为二进制: {bin(large_decimal)}")
print(f"十进制 {large_decimal} 转换为八进制: {oct(large_decimal)}")
print(f"十进制 {large_decimal} 转换为十六进制: {hex(large_decimal)}")

# 示例3: 转换负数
# 定义负数
negative_decimal = -10

print(f"\n负数转换:")
print(f"十进制 {negative_decimal} 转换为二进制: {bin(negative_decimal)}")
print(f"十进制 {negative_decimal} 转换为八进制: {oct(negative_decimal)}")
print(f"十进制 {negative_decimal} 转换为十六进制: {hex(negative_decimal)}")

# 示例4: 去除前缀
# 获取不带前缀的字符串表示
binary_no_prefix = bin(decimal_num)[2:]  # 去除'0b'前缀
octal_no_prefix = oct(decimal_num)[2:]  # 去除'0o'前缀
hex_no_prefix = hex(decimal_num)[2:]  # 去除'0x'前缀

print(f"\n去除前缀:")
print(f"二进制（无前缀）: {binary_no_prefix}")
print(f"八进制（无前缀）: {octal_no_prefix}")
print(f"十六进制（无前缀）: {hex_no_prefix}")
"""


def convert_to_custom_base(decimal, base):
    if decimal == 0:
        return "0"
    result = ""
    while decimal > 0:
        remander = decimal % base
        if remander < 10:
            result = str(remander) + result
        else:
            result = chr(ord("A") + remander - 10) + result
        decimal //= base
    return result


# 自定义进制转换函数
def convert_base(number_str, from_base, to_base):
    # .1先把任意进制转成十进制
    decimal = int(number_str, from_base)
    if to_base == 2:
        return bin(decimal)
    elif to_base == 8:
        return oct(decimal)
    elif to_base == 16:
        return hex(decimal)
    else:
        return convert_to_custom_base(decimal, to_base)


test_number = "11111111"  # 10
# print(f"二进制{test_number} 转为八进制:{convert_base(test_number,2,8)}")
# print(f"二进制{test_number} 转为十六进制:{convert_base(test_number,2,16)}")
print(f"二进制{test_number} 转为五进制:{convert_base(test_number,2,32)}")  # 5进制20

print(ord("A"))
print(chr(ord("A")))
# ABCDEF
# result = chr(ord("A") + remander - 10) + result
