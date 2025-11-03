# 把十进制的整数转成为任意目标进制的字符串
def int_to_base(n, base):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    # 255
    while n > 0:
        last = n % base  # 255%16 =15    15
        char = digits[last]  # F  F
        result = char + result  # FF
        n //= base  # 15 0
    return result


def convert_base(number_str, from_base, to_base):
    if not (2 <= from_base <= 16 and 2 <= to_base <= 16):
        raise ValueError("进制必须是2到16之间")
    # 把输入的字符串转成十进制
    decimal_value = int(number_str, from_base)  # 255
    if to_base == 10:
        return str(decimal_value)
    return int_to_base(decimal_value, to_base)


# 进制转换测试用例
test_cases = [("255", 10, 16, "FF"), ("1010", 2, 10, "10"), ("FF", 16, 2, "11111111")]

# 遍历进制转换测试用例，分别调用转换函数并输出结果
for number, from_b, to_b, expected in test_cases:
    result = convert_base(number, from_b, to_b)
    print(f"{number} ({from_b}进制) -> {result} ({to_b}进制) [期望: {expected}]")
