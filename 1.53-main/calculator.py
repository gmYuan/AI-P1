# from functools import wraps


def wraps(original_func):
    def decorator(wrapper_func):
        wrapper_func.__name__ = original_func.__name__
        wrapper_func.__doc__ = original_func.__doc__
        wrapper_func.__module__ = original_func.__module__
        return wrapper_func

    return decorator


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("函数执行前")
        result = func(*args, **kwargs)
        print("函数执行后")
        return result

    return wrapper


@my_decorator
def calculate_sum(a, b):
    """
    计算两个数的和
    Args:
        a(int):第一个数
        b(int):第二个数
    Returns:
        int: 两数之和
    """
    return a + b
