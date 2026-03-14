# 尾递归版本
# def factorial_tail(n, accumulator=1):
#    if n == 0:
#        return accumulator
#    else:
#        return factorial_tail(n - 1, n * accumulator)


# 转换为循环版本
def factorial_loop(n):
    accumulator = 1
    while n > 0:
        accumulator = n * accumulator
        n = n - 1
    return accumulator


# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
#  use sys.set_int_max_str_digits() to increase the limit

print(factorial_loop(5))
