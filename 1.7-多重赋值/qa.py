

# -------------------------------------------------------------------------------
# 1.7-4.2 高级 *星号解包 ==> 函数的 位置参数 和 关键字参数1

def mixed_function(a, b, c, name, age):
    # 混合参数函数
    return f"位置参数: {a}, {b}, {c}, 关键字参数: {name}, {age}"

arr = [1, 2, 3]
obj = {"name": "4", "age": 5}
# 相当于 print(mixed_function(a=1, b=2, c=3, name="4", age=5))
print(mixed_function(*arr, **obj))


# 1.7-4.2 高级 *星号解包 ==> 函数的 位置参数 和 关键字参数2

def mixed_function(a, b, c, name="xxxxx", age=0):
    # 混合参数函数
    return f"位置参数: {a}, {b}, {c}, 关键字参数: {name}, {age}"


result = mixed_function(2, c=1, b=3, age=30)
print(result)