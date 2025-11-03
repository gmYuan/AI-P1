"""
long_variable_name = (
    "This is a very long string that needs to be broken "
    "into multiple lines for better readability."
)
print(long_variable_name)

## js  //-> #
x = 10  # 这是一个行内注释，解释变量x的赋值

## js /**/

# 这是一个块注释，用于解释下面的代码块
# 它应该与代码块保持相同的缩进级别
# 它应该与代码块保持相同的缩进级别
# 它应该与代码块保持相同的缩进级别
## 多行字符串
s1 =
这是一个块注释，用于解释下面的代码块
它应该与代码块保持相同的缩进级别
它应该与代码块保持相同的缩进级别
它应该与代码块保持相同的缩进级别


# 就是文档字符串注释

这是一个块注释，用于解释下面的代码块
它应该与代码块保持相同的缩进级别
它应该与代码块保持相同的缩进级别
它应该与代码块保持相同的缩进级别



def calculate_sum(a, b):

    这是一个文档字符串，用于解释函数的功能。
    它计算两个数字的和。

    Args:
        a (int): 第一个加数。
        b (int): 第二个加数。

    Returns:
        int: 两个数字的和。


    def minus(a, b):
        return a - b

    return a + b




Variable = 1
variable = 2
print(Variable)
print(variable)

b = 3

print(a)


模块、函数、变量名：使用小写字母和下划线连接 hello_world
类名：使用单词首字母大写（CamelCase）。   HelloWorld
常量：使用全大写字母和下划线连接。   HELLO_WORLD
私有成员：以单下划线开头（_private_member）。 _helloworld
特殊方法/属性：以双下划线开头和结尾（__dunder_method__）。   __helloworld__ 魔术方法 类里的初始化方法 __init__ 类似于js 类的constructor


# 先导入内部模块
import os

# 再导第三方模块
import requests

# 再导自己项目的模块
import module1

# 这个推荐的导入顺序和js是一样的

## js import 成员 from 模块
## py from 模块 import 成员
"""


class Person:
    # 魔术方法就是一些python规定好的一些特殊方法，你只要实现了它，python会在特定的场 合调用它
    def __init__(self):
        print("init")

    def __str__(self):
        return "张三"


print(__name__)
p1 = Person()
# 刚才在类中定义的 __str__ 为什么在外面可以直接调用 str


def str(obj):
    return obj.__str__()


print(str(p1))
# 特殊属性和方法 都是内置的么 是的
