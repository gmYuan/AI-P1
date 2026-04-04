
# ----------------------------------------------------------------

# 如何判断是函数类型
def my_function():
    pass

class MyClass:
    def method(self):
        pass

    def __call__(self, *args, **kwds):
        return "MyClass"


str = "123"
myClass = MyClass()

# .1 如果callable返回True,它就是可以当函数调用
print(callable(my_function), my_function())  # True None
print(callable(myClass), myClass())          # True MyClass
print(callable(str))                         # False



## 2.types
import types

lambdaFn = lambda x: x
print(isinstance(my_function, types.FunctionType))   # True
print(isinstance(lambdaFn, types.LambdaType))        # True



## 3.inspect
import inspect
print(inspect.isfunction(my_function))



# ----------------------------------------------------------------

posisition = 0
# 这是文件内容
file_content = "123\n456\n789\n"
posisition = 5
first_line = file_content[0:5]
reminder_content = file_content[5]



# ----------------------------------------------------------------

# 类是怎么判断来着的
print(inspect.isclass(MyClass))        # True
print(inspect.isclass(my_function))    # False
print(inspect.isclass(int))            # True
print(inspect.isclass("hello"))        # False

# 等价于
print(isinstance(MyClass, type))
print(isinstance(my_function, type))
print(isinstance(int, type))
print(isinstance("hello", type))



# ----------------------------------------------------------------

# \n对应换行符，在len 就是1个
str = "abc\n"
print(len(str))
print(str.encode("utf-8"))
print(len(str.encode("utf-8")))

str = "abc中"
print(len(str))  # 算的是字符的数量，可不是字节的数量
print(str.encode("utf-8"))       # 得到的字节串
print(len(str.encode("utf-8")))


# Q: 是不是统计字符的时候 /n算一个，但是readline的时候 指针 \n算2个
# A: 是的


# Q:  那python怎么获取字节数
# A:  先转字节串，再取字节串的长度