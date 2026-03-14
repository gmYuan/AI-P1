# 1.递归调用是函数体中最后一步操作
# 2.并且这个调用的返回值直接被当前函数返回，没有任何额外的运算。
def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        # 递归调用是最后的、唯一的操作
        return factorial_tail(n - 1, n * accumulator)


# RecursionError: maximum recursion depth exceeded 阈值就是996
print(factorial_tail(999))

"""
def toString(str):
    print(str)


name = "hello"
toString(name + "world")
# 如果N是一基本类型的话值传递，就是把值赋值一份传递过去，传完后和原来的变量就没有关系
# 原来的变量就可以垃圾回收了
"""
