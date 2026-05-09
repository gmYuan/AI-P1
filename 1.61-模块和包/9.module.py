

# -----------------------------------------------------------------------------

import my_module

my_module.hello()
print(my_module.variable)


from my_module import hello, variable

hello()
print(variable)



# -----------------------------------------------------------------------------

from my_package import module1, module2

module1.func1()
module2.func1()



# -----------------------------------------------------------------------------

# 导入Python标准库中的 math 模块
import math

# 使用 math 模块中的 sqrt 函数计算平方根
# 预期输出: 3.0
print(math.sqrt(9))

# 导入Python标准库中的 os 模块
import os

# 获取当前工作目录
# 预期输出: 当前工作目录的路径
print(os.getcwd())



# -----------------------------------------------------------------------------

# 假设 requests 库已经通过 pip install requests 安装
# 导入第三方库 requests
import requests

# 发送一个 HTTP GET 请求
response = requests.get("https://www.example.com")
# 打印响应状态码
print(response.status_code)



# -----------------------------------------------------------------------------

import importlib

import my_module
import my_module

importlib.reload(my_module)
import my_module
