"""
# 定义一个名为my_function的函数
def my_function():
    # 在函数内部定义一个局部变量x，并赋值为10
    x = 10
    # 打印局部变量x的值
    print(f"函数内部访问x: {x}")
    # 预期输出: 函数内部访问x: 10


# 调用my_function函数，这将执行函数内部的代码
my_function()

# 尝试在函数外部访问局部变量x
# 这将导致NameError，因为x只在my_function内部有定义
try:
    # 尝试访问不存在的变量x
    print(f"函数外部访问x: {x}")
except NameError as e:
    # 捕获NameError异常
    print(f"错误: {e}")
    # 预期输出: 错误: name 'x' is not defined


# 定义另一个函数来演示局部变量的独立性
def another_function():
    # 在另一个函数中定义同名变量x
    x = 20
    # 打印这个函数中的x值
    print(f"另一个函数中的x: {x}")
    # 预期输出: 另一个函数中的x: 20


# 调用另一个函数
another_function()

# 定义一个函数来演示局部变量的生命周期
def variable_lifecycle():
    # 在函数开始时定义局部变量
    local_var = "我是局部变量"
    print(f"函数开始时: {local_var}")

    # 修改局部变量
    local_var = "我被修改了"
    print(f"函数中间: {local_var}")

    # 函数结束时，局部变量会被销毁
    print("函数即将结束，局部变量将被销毁")


# 调用函数
variable_lifecycle()
# 函数执行完毕后，局部变量不再存在
print("函数执行完毕")





# 定义一个外层函数outer_function
def outer_function():
    # 在外层函数中定义一个变量y，并赋值为20
    y = 20
    print(f"外层函数中的y: {y}")

    # 在外层函数内部定义一个内层函数inner_function
    def inner_function():
        # 内层函数可以访问外层函数的变量y
        print(f"内层函数访问外层变量y: {y}")
        # 预期输出: 内层函数访问外层变量y: 20

    # 调用内层函数
    inner_function()

    # 在外层函数中再次打印y
    print(f"外层函数中y的值: {y}")


# 调用外层函数
outer_function()



def outer():
    x = 100

    def middle():
        y = 200

        def inner():
            # 依次查找x、y
            print(f"x: {x}, y: {y}")

        inner()

    middle()


outer()
# 输出: x: 100, y: 200


def outer():
    num = 10  # 外层变量

    def inner():
        # 尝试直接修改外层变量，会报错
        try:
            # num += 1  # 内层函数会认为num是自己的局部变量
            # 如果这样直接改的话，会认为num是一个当前函数的局部变量
            num = num + 1
        except UnboundLocalError as e:
            # 错误: cannot access local variable 'num' where it is not associated with a value
            print(f"错误: {e}")

    inner()
    print(f"最终num: {num}")


outer()
# 输出: 错误: local variable 'num' referenced before assignment
#      最终num: 10



# 在函数外部定义一个全局变量z，并赋值为30
z = 30
print(f"模块级别访问全局变量z: {z}")


# 定义一个名为another_function的函数
def another_function():
    # 在函数内部访问全局变量z
    print(f"函数内部访问全局变量z: {z}")
    # 预期输出: 函数内部访问全局变量z: 30


# 调用another_function函数
another_function()

# 在函数外部再次访问全局变量z
print(f"函数外部再次访问全局变量z: {z}")
# 预期输出: 函数外部再次访问全局变量z: 30


# 定义多个函数来演示全局变量的共享
def function_one():
    # 访问全局变量
    print(f"函数1访问全局变量z: {z}")


def function_two():
    # 访问全局变量
    print(f"函数2访问全局变量z: {z}")


# 调用两个函数
function_one()
function_two()


# 全局作用域下定义变量
global_var = 100


def modify_global():
    # 声明要使用外部的全局变量
    global global_var
    # 修改全局变量
    global_var += 20
    print(f"函数内部修改后的global_var: {global_var}")


modify_global()
print(f"函数外部查看global_var: {global_var}")
# 预期输出:
# 函数内部修改后的global_var: 120
# 函数外部查看global_var: 120


# 使用Python内置函数len()计算字符串的长度
# len()函数属于内置作用域
text = "Hello, World!"
length = len(text)
print(f"字符串'{text}'的长度: {length}")
# 预期输出: 字符串'Hello, World!'的长度: 13

# 使用其他内置函数
numbers = [1, 2, 3, 4, 5]
# 使用内置函数sum()计算列表元素的和
total = sum(numbers)
print(f"列表{numbers}的和: {total}")
# 预期输出: 列表[1, 2, 3, 4, 5]的和: 15

# 使用内置函数max()和min()
maximum = max(numbers)
minimum = min(numbers)
print(f"列表{numbers}的最大值: {maximum}")
print(f"列表{numbers}的最小值: {minimum}")
# 预期输出: 列表[1, 2, 3, 4, 5]的最大值: 5
#         列表[1, 2, 3, 4, 5]的最小值: 1

# 使用内置函数str()进行类型转换
number = 42
string_number = str(number)
print(f"数字{number}转换为字符串: '{string_number}'")
# 预期输出: 数字42转换为字符串: '42'


def outer_function():
    b = 50
    print(f"外层函数的初始值:{b}")

    def inner_function():
        # 声明b是一个非局部变量
        nonlocal b
        b += 60
        print(f"内层函数修改后b变成了{b}")

    inner_function()
    print(f"外层函数的变量b={b}")


outer_function()



# 定义一个更复杂的嵌套函数示例
def complex_outer():
    # 外层函数的变量
    outer_var = "外层变量"
    counter = 0

    def middle_function():
        # 中层函数的变量
        middle_var = "中层变量"

        def inner_function():
            # 使用nonlocal关键字修改外层函数的变量
            nonlocal outer_var, counter
            # 修改外层函数的变量
            outer_var = "被内层函数修改"
            counter += 1
            print(f"内层函数修改外层变量: {outer_var}")
            print(f"内层函数修改计数器: {counter}")

        # 调用内层函数
        inner_function()

        # 检查中层函数中的变量
        print(f"中层函数检查中层变量: {middle_var}")

    # 调用中层函数
    middle_function()

    # 检查外层函数的变量是否被修改
    print(f"外层函数检查外层变量: {outer_var}")
    print(f"外层函数检查计数器: {counter}")


# 调用复杂的外层函数
complex_outer()

# 定义一个全局变量
conflict_var = "全局变量"
print(f"初始全局变量: {conflict_var}")


# 定义一个函数来演示变量名冲突
def conflict_demo():
    # 在函数内部定义同名变量
    # 全局的变量，内部声明nonlocal，可以访问到吗 No binding for nonlocal "conflict_var" found
    # conflict_var = conflict_var  不可以 原理是一样的，它样写会找局部变量
    # conflict_var = conflict_var
    temp = conflict_var
    conflict_var = temp
    # global conflict_var
    # conflict_var = "局部变量"
    print(f"函数内部局部变量: {conflict_var}")

    # 如果要访问全局变量，需要使用global关键字
    # "conflict_var" is assigned before global declaration

    print(f"使用global后的全局变量: {conflict_var}")


# 调用函数
conflict_demo()

# 检查全局变量
print(f"函数外部全局变量: {conflict_var}")



# 定义一个函数来演示嵌套作用域冲突
def nested_conflict():
    # 外层函数的变量
    shared_var = "外层变量"
    print(f"外层函数初始变量: {shared_var}")

    def inner_function():
        # 内层函数定义同名变量
        nonlocal shared_var
        shared_var = "内层变量"
        print(f"内层函数局部变量: {shared_var}")

        # 如果要修改外层函数的变量，需要使用nonlocal关键字
        # "shared_var" is assigned before nonlocal declaration

        shared_var = "被内层函数修改"
        print(f"使用nonlocal后的变量: {shared_var}")

    # 调用内层函数
    inner_function()

    # 检查外层函数的变量
    print(f"外层函数最终变量: {shared_var}")


# 调用函数
nested_conflict()

"""


# compose函数组件
def compose(*funcs):
    def composed(*args, **kwargs):
        result = funcs[-1](*args, **kwargs)
        for func in reversed(funcs[:-1]):
            result = func(result)
        return result

    return composed


def add_one(x, y, z):
    return x + y + z + 1


def multiply_by_two(x):
    return x * 2


def square(x):
    return x**2


composed_func = compose(square, multiply_by_two, add_one)
result = composed_func(3, 4, 5)
print(result)
