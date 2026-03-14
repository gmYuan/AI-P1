"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # 注意这里

# 一般递归，会存在 栈溢出问题：
# RecursionError: maximum recursion depth exceeded
print(factorial(1000))  # 120
"""


# 尾递归的特点：
# 1.递归调用是函数体中最后一步操作
# 2.并且这个调用的返回值 直接被当前函数返回，没有任何额外的运算。
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1)  # 注意这里

# 这种实现还是会报错，因为不是正确的 尾递归实现
print(factorial(1000))  # 120
"""


# 尾递归的特点：
# 1.递归调用是函数体中最后一步操作
# 2.并且这个调用的返回值 直接被当前函数返回，没有任何额外的运算。
# ygm：关于 尾递归，最好的形象化理解，就是 接力棒传递的比喻 🌟🌟

def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        # 递归调用是最后的、唯一的操作
        return factorial_tail(n - 1, n * accumulator)


# 实际实现上，py 没有支持 尾递归
# RecursionError: maximum recursion depth exceeded 阈值就是996
print(factorial_tail(999))



"""
def toString(str):
    print(str)


name = "hello"
toString(name + "world")
# 如果N是一个基本类型的话，是值传递，就是把值赋值一份传递过去，传完后和原来的变量 就没有关系
# 原来的变量 就可以垃圾回收了
"""