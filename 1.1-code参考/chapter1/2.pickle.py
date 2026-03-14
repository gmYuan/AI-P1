"""
import pickle

data = {"name": "Alice", "age": 25, "is_student": True}
# with open("data.pickle", "wb") as f:
# dump的意思是把data转成字节流写入文件
#    pickle.dump(data, f)

# dumps的意思是把data转化成字节串，而不是直接写入文件
serialized_data = pickle.dumps(data)
print(serialized_data)
print(f"序列化后的数据长度:{len(serialized_data)}字节")
print(f"序列化后的数据类型:{type(serialized_data)}")

deserialized_data = pickle.loads(serialized_data)
print(deserialized_data)


if True:
    a = 1
print(a)

import pickle


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Person(name='{self.name}')"


person = Person("Alice", 25, "Alice@qq.com")
print(person)
with open("person.pickle", "wb") as f:
    pickle.dump(person, f)

with open("person.pickle", "rb") as f:
    loaded_person = pickle.load(f)
print(loaded_person)

import pickle

with open("data.pickle", "rb") as f:
    data = pickle.load(f)

print(data)
print(f"数据类型:{type(data)}")
print(f"name:{type(data['name'])}")
print(f"age:{type(data['age'])}")
print(f"is_student:{type(data['is_student'])}")
# 导入pickle模块
import pickle


# 定义一个简单的函数
def greet(name):
    # 返回问候语
    return f"Hello, {name}!"


# 定义一个简单的类
class Calculator:
    # 定义加法方法
    def add(self, a, b):
        # 返回两个数的和
        return a + b

    # 定义乘法方法
    def multiply(self, a, b):
        # 返回两个数的乘积
        return a * b


# 创建Calculator实例
calc = Calculator()

# 序列化函数和类实例
data_to_serialize = {"function": greet, "calculator": calc, "message": "This is a test"}

# 将包含函数和类的对象序列化
with open("complex_data.pickle", "wb") as f:
    # 序列化包含函数和类的复杂对象
    pickle.dump(data_to_serialize, f)

# 反序列化包含函数和类的对象
with open("complex_data.pickle", "rb") as f:
    # 反序列化复杂对象
    loaded_data = pickle.load(f)
# dump和load是一组，是直接写入文件和读取文件的
# dumps和loads是一组，是转字节串的
# 使用反序列化的函数
# 调用反序列化的greet函数
greeting = loaded_data["function"]("Python")
print(f"函数调用结果: {greeting}")
# 输出: Hello, Python!

# 使用反序列化的类实例
# 调用反序列化的Calculator实例的方法
result_add = loaded_data["calculator"].add(5, 3)
result_multiply = loaded_data["calculator"].multiply(4, 6)
print(f"加法结果: {result_add}")
print(f"乘法结果: {result_multiply}")
# 输出: 加法结果: 8
#       乘法结果: 24
# 导入pickle模块
import pickle

# 定义一个包含不可序列化对象的字典
problematic_data = {
    "name": "Alice",
    "file": open("nonexistent.txt", "r"),  # 文件对象通常不可序列化
    "age": 25,
}

try:
    # 尝试序列化包含文件对象的字典
    # serialized = pickle.dumps(problematic_data)
    print("序列化成功")
except (pickle.PicklingError, TypeError) as e:
    # 捕获序列化错误
    print(f"序列化失败: {e}")
    # 输出: 序列化失败: cannot pickle '_io.TextIOWrapper' objects

# 处理文件不存在的情况
try:
    # 尝试打开不存在的pickle文件
    with open("nonexistent.pickle", "rb") as f:
        data = pickle.load(f)
except FileNotFoundError:
    # 捕获文件不存在错误
    print("文件不存在，无法进行反序列化")
except pickle.UnpicklingError as e:
    # 捕获反序列化错误
    print(f"反序列化失败: {e}")
except Exception as e:
    # 捕获其他未知错误
    print(f"发生未知错误: {e}")
# 导入pickle模块
import pickle

# 创建一个损坏的pickle文件
corrupted_data = b"This is not a valid pickle file"
# 写入损坏的数据到文件
with open("corrupted.pickle", "wb") as f:
    f.write(corrupted_data)

try:
    # 尝试读取损坏的pickle文件
    with open("corrupted.pickle", "rb") as f:
        data = pickle.load(f)
    print("反序列化成功")
except pickle.UnpicklingError as e:
    # 捕获反序列化错误
    print(f"无法反序列化损坏的文件: {e}")
    # 输出: 无法反序列化损坏的文件: invalid load key, '\x54'.
except Exception as e:
    # 捕获其他错误
    print(f"发生其他错误: {e}")
# 导入pickle模块
import pickle


# 警告：以下代码仅用于演示安全风险，不要在生产环境中使用
# 定义一个恶意类，在反序列化时会执行代码
class MaliciousClass:
    # 定义__reduce__方法，在反序列化时会被调用
    def __reduce__(self):
        # 返回一个元组：(函数, 参数)
        # 这里返回os.system函数和要执行的命令
        import os

        return (os.system, ('echo "This is a security risk!"',))


# 创建恶意对象
malicious_obj = MaliciousClass()

# 序列化恶意对象
with open("malicious.txt", "wb") as f:
    pickle.dump(malicious_obj, f)

print("恶意对象已序列化")
print("警告：不要加载来自不可信源的pickle文件！")

# 在实际应用中，永远不要加载来自不可信源的pickle文件
# 因为pickle可以执行任意代码，存在严重的安全风险
import pickle
import hashlib
import os


def safe_pick_dump(data, filename):
    try:
        # 检查文件路径是否安全避免路径攻击 .. /
        if ".." in filename or "/" in filename:
            raise ValueError("不安全的路径")
        # 序列化数据
        serialized_data = pickle.dumps(data)
        # 计算数据的哈希值
        data_hash = hashlib.sha256(serialized_data).hexdigest()
        with open(filename, "wb") as f:
            f.write(data_hash.encode() + b"\n")
            f.write(serialized_data)
        return True

    except Exception as e:
        print(f"序列化失败:{e}")
        return False


def safe_pick_load(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"文件{filename}不存在")
        with open(filename, "rb") as file:
            hash_line = file.readline().strip()
            # 指的是从当前位置读到末尾
            serialized_data = file.read()
        calculated_hash = hashlib.sha256(serialized_data).hexdigest()
        if calculated_hash != hash_line.decode():
            raise ValueError(f"数据的完整性验证失败")
        data = pickle.loads(serialized_data)
        return data

    except Exception as e:
        print(f"反序列化失败:{e}")
        return None


test_data = {"name": "Alice", "age": 25}
safe_pick_dump(test_data, "safe_data.pickle")
loaded_data = safe_pick_load("safe_data.pickle")
print(loaded_data)
# 导入必要的模块
import pickle
import json

# 定义一个包含基本数据类型的字典
basic_data = {"name": "Alice", "age": 25, "is_student": True}

# 使用pickle序列化
print("--- Pickle序列化 ---")
# 序列化为字节字符串
pickle_data = pickle.dumps(basic_data)
print(f"Pickle数据长度: {len(pickle_data)} 字节")
print(f"Pickle数据类型: {type(pickle_data)}")

# 使用JSON序列化
print("\n--- JSON序列化 ---")
# 序列化为JSON字符串
json_data = json.dumps(basic_data)
print(f"JSON数据长度: {len(json_data)} 字节")
print(f"JSON数据类型: {type(json_data)}")
print(f"JSON数据内容: {json_data}")

# 反序列化对比
print("\n--- 反序列化对比 ---")
# Pickle反序列化
pickle_loaded = pickle.loads(pickle_data)
print(f"Pickle反序列化结果: {pickle_loaded}")

# JSON反序列化
json_loaded = json.loads(json_data)
print(f"JSON反序列化结果: {json_loaded}")

# 复杂对象序列化对比
print("\n--- 复杂对象序列化对比 ---")


def multi(a):
    return a * 2


# 定义一个包含函数的对象
complex_data = {"name": "Alice", "func": multi, "age": 25}  # 函数对象

# 尝试用pickle序列化
try:
    pickle_complex = pickle.dumps(complex_data)
    print("Pickle可以序列化包含函数的对象")
except Exception as e:
    print(f"Pickle序列化失败: {e}")

# 尝试用JSON序列化
try:
    json_complex = json.dumps(complex_data)
    print("JSON可以序列化包含函数的对象")
except Exception as e:
    print(f"JSON序列化失败: {e}")
    # 输出: JSON序列化失败: Object of type function is not JSON serializable
# pickle json
# pickle dump load 操作文件的   dumps loads 字节串
# json   dump load 操作文件的   dumps loads 字符串
# 带S是操作内存的，不带S是操作文件
def add_numbers(a, b):
    return a + b


def greet_user(name):
    return f"hello,{name}"


def main():
    num1 = 10
    num2 = 20
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is :{result}")


if __name__ == "__main__":
    main()

"""
