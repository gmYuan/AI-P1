"""


# 定义一个可以处理不同类型参数的函数
def dynamic_print(data):
    # 打印传入的数据及其类型
    print(f"数据: {data}, 类型: {type(data)}")


# 调用函数传入整数
dynamic_print(10)
# 输出: 数据: 10, 类型: <class 'int'>

# 调用函数传入字符串
dynamic_print("hello")
# 输出: 数据: hello, 类型: <class 'str'>

# 调用函数传入列表
dynamic_print([1, 2, 3])
# 输出: 数据: [1, 2, 3], 类型: <class 'list'>

# 调用函数传入字典
dynamic_print({"name": "Alice", "age": 30})
# 输出: 数据: {'name': 'Alice', 'age': 30}, 类型: <class 'dict'>

# 调用函数传入浮点数
dynamic_print(3.14)
# 输出: 数据: 3.14, 类型: <class 'float'>



# 定义一个可以处理多种数值类型的数学函数
def calculate_area(length, width):
    # 检查参数是否为数值类型
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        # 如果不是数值类型，抛出异常
        raise TypeError("参数必须是数值类型")

    # 计算面积
    area = length * width
    # 打印计算结果
    print(f"长度: {length}, 宽度: {width}, 面积: {area}")
    return area


# 使用整数参数
calculate_area(5, 3)
# 输出: 长度: 5, 宽度: 3, 面积: 15

# 使用浮点数参数
calculate_area(2.5, 4.0)
# 输出: 长度: 2.5, 宽度: 4.0, 面积: 10.0

# 使用混合类型参数
calculate_area(3, 2.5)
# 输出: 长度: 3, 宽度: 2.5, 面积: 7.5

# 尝试使用非数值类型（会抛出异常）
try:
    calculate_area("5", 3)
except TypeError as e:
    print(f"错误: {e}")



# 定义一个带有默认参数的问候函数
def greet(name, greeting="Hello"):
    # 打印问候语和名字
    print(f"{greeting}, {name}!")


# 调用greet函数，只提供名字，使用默认问候语
greet("Alice")
# 输出: Hello, Alice!

# 调用greet函数，提供名字和自定义问候语
greet("Bob", "Hi")
# 输出: Hi, Bob!

# 调用greet函数，使用关键字参数
greet("Charlie", greeting="Good morning")
# 输出: Good morning, Charlie!


# 定义更复杂的默认参数函数
def create_user(name, age=18, email=None, is_active=True):
    # 创建用户信息字典
    user_info = {"name": name, "age": age, "email": email, "is_active": is_active}
    # 打印用户信息
    print(f"创建用户: {user_info}")
    return user_info


# 只提供必需参数
user1 = create_user("Alice")
# 输出: 创建用户: {'name': 'Alice', 'age': 18, 'email': None, 'is_active': True}

# 提供部分可选参数
user2 = create_user("Bob", 25)
# 输出: 创建用户: {'name': 'Bob', 'age': 25, 'email': None, 'is_active': True}

# 提供所有参数
user3 = create_user("Charlie", 30, "charlie@example.com", False)
# 输出: 创建用户: {'name': 'Charlie', 'age': 30, 'email': 'charlie@example.com', 'is_active': False}

# 使用关键字参数（顺序可以改变）
user4 = create_user("David", email="david@example.com", age=28)
# 输出: 创建用户: {'name': 'David', 'age': 28, 'email': 'david@example.com', 'is_active': True}
"""


# 注意：默认参数的值在函数定义时计算，而不是在调用时
def add_item(item, target_list=[]):
    # 将项目添加到目标列表
    target_list.append(item)
    # 打印列表内容
    print(f"列表内容: {target_list}")
    return target_list


# 第一次调用
list1 = add_item("apple")
# 输出: 列表内容: ['apple']

# 第二次调用（注意：会保留之前的内容）
list2 = add_item("banana")
# 输出: 列表内容: ['apple', 'banana']


# 正确的做法：使用None作为默认值
def add_item_correct(item, target_list=None):
    # 如果target_list为None，创建新列表
    if target_list is None:
        target_list = []
    # 将项目添加到目标列表
    target_list.append(item)
    # 打印列表内容
    print(f"列表内容: {target_list}")
    return target_list


# 第一次调用
list3 = add_item_correct("apple")
# 输出: 列表内容: ['apple']

# 第二次调用（不会保留之前的内容）
list4 = add_item_correct("banana")
# 输出: 列表内容: ['banana']

# 显式传递列表
existing_list = ["orange"]
list5 = add_item_correct("grape", existing_list)
# 输出: 列表内容: ['orange', 'grape']
