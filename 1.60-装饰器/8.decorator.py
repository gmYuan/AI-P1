

# -----------------------------------------------------------------------------

def decorator_name(func):
    def wrapper(*args, **kwargs):
        # 在调用原始函数前可加入自定义操作
        print("开始执行")
        result = func(*args, **kwargs)
        # 在调用原始函数后可加入自定义操作
        print("执行结束")
        return result

    return wrapper


@decorator_name  # 等效于 func = decorator_name(func)
def func():
    print("这是原始函数内容")

func()



# -----------------------------------------------------------------------------

# 定义装饰器工厂函数，接受参数
def repeat(num_times):
    # 返回实际的装饰器函数
    def decorator(func):
        # 定义包装函数，处理参数传递
        def wrapper(*args, **kwargs):
            # 根据指定次数重复执行函数
            for i in range(num_times):
                print(f"第 {i+1} 次执行：")
                # 调用原始函数并传递所有参数
                result = func(*args, **kwargs)
            # 返回最后一次执行的结果
            return result

        # 返回包装函数
        return wrapper

    # 返回装饰器函数
    return decorator


# 使用带参数的装饰器
@repeat(3)
def greet(name):
    # 问候函数
    print(f"Hello {name}!")
    # 返回问候信息
    return f"Greeting for {name}"


# 调用被装饰的函数
result = greet("Python")
print(f"最终结果：{result}")



# -----------------------------------------------------------------------------

class Logger:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print(f"开始执行:{self.__func.__name__}")
        result = self.__func(*args, **kwargs)
        print(f"结束执行:{self.__func.__name__}")
        return result


# @Logger
def say_hello(name):
    print(f"hello,{name}")


say_hello = Logger(say_hello)
say_hello("python")



# -----------------------------------------------------------------------------

def singleton(cls):
    _instance = {}

    def get_instance(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return get_instance


@singleton
class MyDatabase:
    def __init__(self):
        print(f"初始化数据库连接")


db1 = MyDatabase()
db2 = MyDatabase()
print(db1 is db2)



# -----------------------------------------------------------------------------

# 还可以使用类装饰器为类注入通用的功能，比如说动态添加新的方法
def add_say_hi(cls):
    def say_hi(self):
        print(f"Hi,我是{self.__class__.__name__}")

    cls.say_hi = say_hi
    return cls


@add_say_hi
class People:
    pass


people = People()
people.say_hi()




# -----------------------------------------------------------------------------

from calculator import calculate_sum

result = calculate_sum(5, 3)
print(result)
print(f"函数名:{calculate_sum.__name__}")
print(f"函数文档:{calculate_sum.__doc__}")
print(f"函数模块:{calculate_sum.__module__}")



# -----------------------------------------------------------------------------

def logger1(func):
    def wrapper(*args, **kwargs):
        # 在调用原始函数前可加入自定义操作
        print("logger1开始执行")
        result = func(*args, **kwargs)
        # 在调用原始函数后可加入自定义操作
        print("logger1执行结束")
        return result

    return wrapper


def logger2(func):
    def wrapper(*args, **kwargs):
        # 在调用原始函数前可加入自定义操作
        print("logger2开始执行")
        result = func(*args, **kwargs)
        # 在调用原始函数后可加入自定义操作
        print("logger2执行结束")
        return result

    return wrapper


@logger1  # 等效于 func = decorator_name(func)
@logger2
def func():
    print("这是原始函数内容")


func()




# -----------------------------------------------------------------------------

import inspect


# 函数的签名 位置参数 默认参数 可变参数 关键字参数 可变关键字参数
# sig = inspect.signature(example_func)
## print(sig)
# print(type(sig))



# 签名的结构
def example_func(name: str, age=25, *args, email=None, **kwargs):
    pass

# example_func("张三", 30)
# example_func(name="张三", age=30)

def analyze_signature(func):
    sig = inspect.signature(func)
    print(f"函数{func.__name__}的签名{sig}")
    for param_name, param in sig.parameters.items():
        print(f"参数名:{param_name}")  # 参数名
        print(f"类型:{param.kind}")  # 类型
        print(f"默认值:{param.default}")  # 默认值
        print(f"注解:{param.annotation}")  # 注解


analyze_signature(example_func)

"""
函数example_func的签名(name: str, age=25, *args, email=None, **kwargs)
参数名:name
类型:POSITIONAL_OR_KEYWORD
默认值:<class 'inspect._empty'>
注解:<class 'str'>
参数名:age
类型:POSITIONAL_OR_KEYWORD
默认值:25
注解:<class 'inspect._empty'>
参数名:args
类型:VAR_POSITIONAL
默认值:<class 'inspect._empty'>
注解:<class 'inspect._empty'>
参数名:email
类型:KEYWORD_ONLY
默认值:None
注解:<class 'inspect._empty'>
参数名:kwargs
类型:VAR_KEYWORD
默认值:<class 'inspect._empty'>
注解:<class 'inspect._empty'>
"""



# -----------------------------------------------------------------------------

import inspect

def func(a, b, c=10):
    return a + b + c


sig = inspect.signature(func)
try:
    bound_args = sig.bind(1, 2)# BoundArguments
    print(f"绑定成功:", bound_args.arguments)
except TypeError as e:
    print(f"绑定失败:{e}")



# --------------------------

import inspect


def func(x, y=10, z=20):
    return x + y + z


sig = inspect.signature(func)
bound_args = sig.bind(5, z=30)
# 应用参数的默认值，补全未传递的参数
bound_args.apply_defaults()
print(f"bound_args:{type(bound_args)}")
print(f"arguments:{bound_args.arguments}")
print(f"args:{bound_args.args}")
print(f"kwargs:{bound_args.kwargs}")
print(f"signature:{bound_args.signature}")



# -----------------------------------------------------------------------------

def foo(a: int, b: str = "default", c: float = 3.14) -> bool:
    pass


for name, t in foo.__annotations__.items():
    print(f"{name},{t}")



# -----------------------------------------------------------------------------

import inspect


def func(x, y=10, z=20):
    return x + y + z


sig = inspect.signature(func)
bound_args = sig.bind(5, z=30)
# 应用参数的默认值，补全未传递的参数
bound_args.apply_defaults()
print(f"bound_args:{type(bound_args)}")
print(f"arguments:{bound_args.arguments}")
print(f"args:{bound_args.args}")
print(f"kwargs:{bound_args.kwargs}")
print(f"signature:{bound_args.signature}")




# -----------------------------------------------------------------------------

import inspect
from functools import wraps


def type_assert(func):
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        for name, value in bound_args.arguments.items():
            expected_type = func.__annotations__[name]
            if not isinstance(value, expected_type):
                raise TypeError(
                    f"参数{name}期望的类型是{expected_type.__name__},但是你传递的类型是{type(value).__name__}"
                )
        return func(*args, **kwargs)

    return wrapper


# 注解只是一种提示/文档机制，Python 不会自动强制类型校验（除非用第三方工具或自定义装饰器）。
@type_assert
def greet(name: str, age: int):
    print(f"大家好，我叫{name},今年{age}岁了")


# greet("张三", 25)
# TypeError: 参数age期望的类型是int,但是你传递的类型是str
greet("李四", "四十")
