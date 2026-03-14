"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # 注意这里


# RecursionError: maximum recursion depth exceeded
print(factorial(1000))  # 120
"""


# 1.递归调用是函数体中最后一步操作
# 2.并且这个调用的返回值直接被当前函数返回，没有任何额外的运算。
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1)  # 注意这里


print(factorial(1000))  # 120
