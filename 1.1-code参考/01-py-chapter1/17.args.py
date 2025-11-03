"""
# 定义一个函数，使用*args接受任意数量的位置参数
def calculate_sum(*args):
    # 打印所有接收到的参数
    print(f"接收到的参数: {args}")
    # 打印参数类型
    print(f"参数类型: {type(args)}")
    # 返回所有参数的和
    return sum(args)


# 调用calculate_sum函数，传入两个参数
result1 = calculate_sum(1, 2)
print(f"两个参数的和: {result1}")
# 输出: 接收到的参数: (1, 2)
#      参数类型: <class 'tuple'>
#      两个参数的和: 3

# 调用calculate_sum函数，传入四个参数
result2 = calculate_sum(1, 2, 3, 4)
print(f"四个参数的和: {result2}")
# 输出: 接收到的参数: (1, 2, 3, 4)
#      参数类型: <class 'tuple'>
#      四个参数的和: 10

# 调用calculate_sum函数，传入更多参数
result3 = calculate_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"十个参数的和: {result3}")
# 输出: 接收到的参数: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#      参数类型: <class 'tuple'>
#      十个参数的和: 55


# 定义一个函数，使用**kwargs接受任意数量的关键字参数
def display_info(**kwargs):
    # 打印所有接收到的关键字参数
    print(f"接收到的信息: {kwargs}")
    # 打印参数类型
    print(f"参数类型: {type(kwargs)}")
    # 遍历字典并打印键值对
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 调用display_info函数，传入不同的关键字参数
display_info(name="Alice", age=30)
# 输出: 接收到的信息: {'name': 'Alice', 'age': 30}
#      参数类型: <class 'dict'>
#      name: Alice
#      age: 30

# 调用display_info函数，传入更多关键字参数
display_info(city="New York", population=8000000, country="USA")
# 输出: 接收到的信息: {'city': 'New York', 'population': 8000000, 'country': 'USA'}
#      参数类型: <class 'dict'>
#      city: New York
#      population: 8000000
#      country: USA


# *args装得下所有没写名字的“逗号参数”
# **kwargs能兜住所有带名字的“等号参数”


# 定义一个同时使用*args和**kwargs的函数
def flexible_function(fixed_arg, *args, **kwargs):
    # 打印固定参数
    print(f"固定参数: {fixed_arg}")
    # 打印位置参数元组
    print(f"可变位置参数: {args}")
    # 打印关键字参数字典
    print(f"可变关键字参数: {kwargs}")
    # 计算总参数数量
    total_args = 1 + len(args) + len(kwargs)
    print(f"总参数数量: {total_args}")


# 调用flexible_function，只提供固定参数
flexible_function(10)
# 输出: 固定参数: 10
#      可变位置参数: ()
#      可变关键字参数: {}
#      总参数数量: 1

# 调用flexible_function，提供固定参数和位置参数
flexible_function(10, 20, 30)
# 输出: 固定参数: 10
#      可变位置参数: (20, 30)
#      可变关键字参数: {}
#      总参数数量: 3

# 调用flexible_function，提供固定参数和关键字参数
flexible_function(10, key1="value1", key2="value2")
# 输出: 固定参数: 10
#      可变位置参数: ()
#      可变关键字参数: {'key1': 'value1', 'key2': 'value2'}
#      总参数数量: 3

# 调用flexible_function，提供所有类型的参数
flexible_function(10, 20, 30, key1="value1", key2="value2")
# 输出: 固定参数: 10
#      可变位置参数: (20, 30)
#      可变关键字参数: {'key1': 'value1', 'key2': 'value2'}
#      总参数数量: 5


# 实际应用示例：日志记录函数
def log_message(level, message, *args, **kwargs):
    # 格式化消息
    formatted_message = message.format(*args) if args else message
    # 打印日志级别和消息
    print(f"[{level.upper()}] {formatted_message}")
    # 如果有额外信息，打印它们
    if kwargs:
        print("额外信息:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")


# 使用日志函数
log_message("info", "用户 {} 登录成功", "Alice")
# 输出: [INFO] 用户 Alice 登录成功

log_message("error", "数据库连接失败", user_id=123, timestamp="2023-12-01")
# 输出: [ERROR] 数据库连接失败
#      额外信息:
#        user_id: 123
#        timestamp: 2023-12-01


from functools import singledispatch


@singledispatch
def process_data(arg):
    print(f"默认处理:{arg} 类型 {type(arg).__name__}")


# 为int类型注册一个特定的实现
@process_data.register(int)
def _(arg):
    print(f"处理整数:{arg*2}")


@process_data.register(list)
def _(arg):
    print(f"处理列表:{len(arg)}")


@process_data.register(str)
def _(arg):
    print(f"处理整数:{len(arg)}")


process_data(10)
process_data([1, 2, 3])
process_data("abc")
process_data(set())


# 从functools模块导入singledispatch装饰器
from functools import singledispatch
from typing import Union, List, Dict


# 定义一个更复杂的泛型函数
@singledispatch
def serialize_data(data, suffix):
    # 默认序列化逻辑
    return str(data)


# 为字典类型注册序列化方法
@serialize_data.register(dict)
def _(data, suffix):
    # 字典序列化逻辑
    result = []
    for key, value in data.items():
        result.append(f"{key}: {value}")
    return "{" + ", ".join(result) + "} " + suffix


# 为列表类型注册序列化方法
@serialize_data.register(list)
def _(data):
    # 列表序列化逻辑
    return "[" + ", ".join(map(str, data)) + "]"


# 为字符串类型注册序列化方法
@serialize_data.register(str)
def _(data):
    # 字符串序列化逻辑
    return f'"{data}"'


# 为数字类型注册序列化方法
@serialize_data.register(int)
def _(data):
    # 整数序列化逻辑
    return f"整数: {data}"


@serialize_data.register(float)
def _(data):
    # 浮点数序列化逻辑
    return f"浮点数: {data:.2f}"


# 测试序列化函数
print("--- 序列化示例 ---")

# 序列化字典
dict_data = {"name": "Alice", "age": 30}
print(f"字典序列化: {serialize_data(dict_data,'我后缀')}")
# 输出: 字典序列化: {name: Alice, age: 30}

# 序列化列表
list_data = [1, 2, 3, 4, 5]
print(f"列表序列化: {serialize_data(list_data)}")
# 输出: 列表序列化: [1, 2, 3, 4, 5]

# 序列化字符串
str_data = "Hello World"
print(f"字符串序列化: {serialize_data(str_data)}")
# 输出: 字符串序列化: "Hello World"

# 序列化整数
int_data = 42
print(f"整数序列化: {serialize_data(int_data)}")
# 输出: 整数序列化: 整数: 42

# 序列化浮点数
float_data = 3.14159
print(f"浮点数序列化: {serialize_data(float_data)}")
# 输出: 浮点数序列化: 浮点数: 3.14

# 序列化其他类型（使用默认方法）
bool_data = True
print(f"布尔值序列化: {serialize_data(bool_data)}")
# 输出: 布尔值序列化: True
"""


def singledispatch(func):
    registry = {}

    def wrapper(*args, **kwargs):
        if args:
            arg_type = type(args[0])
            for cls in registry:
                if arg_type == cls:
                    # if isinstance(args[0], cls):
                    return registry[cls](*args, **kwargs)
        return func(*args, **kwargs)

    def register(cls):
        def decorator(f):
            registry[cls] = f
            return f

        return decorator

    wrapper.register = register
    return wrapper


@singledispatch
def greet(obj):
    return f"Hello,{obj}"


@greet.register(str)
def _(name):
    return f"Hello,{name}"


@greet.register(int)
def _(age):
    return f"You are {age} years old"


# ----------------------------------------------------
print(greet("Alice"))
print(greet(25))
print(greet([1, 2]))
# decorator是注册时执行，还是函数调用时执行
