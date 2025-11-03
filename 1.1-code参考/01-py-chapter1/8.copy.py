"""
import copy

a = [1, 2, [3, 4]]
b = copy.copy(a)  # 浅拷贝
c = copy.deepcopy(a)  # 深拷贝

# 修改嵌套对象
a[2][0] = 999

print("a:", a)  # [1, 2, [999, 4]]
print("b:", b)  # [1, 2, [999, 4]]  # 受影响（嵌套对象共享）
print("c:", c)  # [1, 2, [3, 4]]    # 不受影响（嵌套对象已复制）


lst1 = [[1], [2, 3]]
lst2 = lst1[:]  # 等价于 copy.copy(lst1)
lst3 = lst1.copy()
lst4 = copy.copy(lst1)
lst1[0][0] = 99
print(lst2)  # [[99], [2, 3]]
print(lst3)
print(lst4)

dict1 = dict()
dict1.copy()
set1 = set()
set1.copy()


import copy

# 创建一个更复杂的嵌套结构
original_data = {
    "name": "张三",
    "age": 25,
    "hobbies": ["读书", "游泳", "编程"],
    "address": {"city": "北京", "district": "朝阳区"},
    "scores": [85, 92, 78],
}

# 执行浅拷贝
shallow_copy = copy.copy(original_data)

# 执行深拷贝
deep_copy = copy.deepcopy(original_data)

print("=== 修改前的状态 ===")
print("原始数据:", original_data)
print("浅拷贝:", shallow_copy)
print("深拷贝:", deep_copy)

# 修改原始数据中的嵌套对象
original_data["hobbies"].append("音乐")
original_data["address"]["city"] = "上海"
original_data["scores"][0] = 95

print("\n=== 修改后的状态 ===")
print("原始数据:", original_data)
print("浅拷贝:", shallow_copy)
print("深拷贝:", deep_copy)

# 检查对象身份
print("\n=== 对象身份检查 ===")
print("原始hobbies id:", id(original_data["hobbies"]))
print("浅拷贝hobbies id:", id(shallow_copy["hobbies"]))
print("深拷贝hobbies id:", id(deep_copy["hobbies"]))
print(
    "原始和浅拷贝hobbies是否相同:", original_data["hobbies"] is shallow_copy["hobbies"]
)
print("原始和深拷贝hobbies是否相同:", original_data["hobbies"] is deep_copy["hobbies"])


import copy


class Person:
    def __init__(self, name, age, hobbies):
        # 初始化Person对象
        self.name = name
        self.age = age
        self.hobbies = hobbies  # 这是一个可变列表

    def __repr__(self):
        # 定义对象的字符串表示
        return f"Person(name='{self.name}', age={self.age}, hobbies={self.hobbies})"


# 创建Person对象
person1 = Person("李四", 30, ["读书", "游泳"])

# 执行浅拷贝
shallow_person = copy.copy(person1)

# 执行深拷贝
deep_person = copy.deepcopy(person1)

print("=== 修改前的状态 ===")
print("原始对象:", person1)
print("浅拷贝对象:", shallow_person)
print("深拷贝对象:", deep_person)

# 修改原始对象的属性
person1.name = "王五"
person1.age = 35
person1.hobbies.append("音乐")

print("\n=== 修改后的状态 ===")
print("原始对象:", person1)
print("浅拷贝对象:", shallow_person)
print("深拷贝对象:", deep_person)

# 检查hobbies列表的身份
print("\n=== hobbies列表身份检查 ===")
print("原始hobbies id:", id(person1.hobbies))
print("浅拷贝hobbies id:", id(shallow_person.hobbies))
print("深拷贝hobbies id:", id(deep_person.hobbies))


import copy


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


root = Node("根节点")
child1 = Node("子节点1")
child2 = Node("子节点2")
root.add_child(child1)
root.add_child(child2)
print(root.children)
print(child1.parent.value)

try:
    deep_copy = copy.deepcopy(root)
    print(deep_copy.children)
    print(deep_copy.children[0].parent.value)
except Exception as e:
    print("拷贝失败")



def shallow_copy(obj):
    # 如果对象是列表，则返回一个新的列表，元素为原有元素的值的拷贝或者引用的拷贝
    if isinstance(obj, list):
        return [item for item in obj]
    elif isinstance(obj, tuple):
        return tuple(item for item in obj)
    elif isinstance(obj, dict):
        return {key: value for key, value in obj.items()}
    elif isinstance(obj, set):
        return {item for item in obj}
    else:
        return obj


def deep_copy(obj):
    # 如果对象是列表，则返回一个新的列表，元素为原有元素的值的拷贝或者引用的拷贝
    if isinstance(obj, list):
        return [deep_copy(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(deep_copy(item) for item in obj)
    elif isinstance(obj, dict):
        return {key: deep_copy(value) for key, value in obj.items()}
    elif isinstance(obj, set):
        return {deep_copy(item) for item in obj}
    else:
        return obj


a = [1, 2, [3, 4]]
b = shallow_copy(a)
c = deep_copy(a)
print("原始数据")
print(a)
print(b)
print(c)
a[2][0] = 100
print("修改后")
print(a)
print(b)
print(c)

print(id(a[2]))
print(id(b[2]))
print(id(c[2]))

"""


def deepCopy(obj):
    # 如果对象是列表，则返回一个新的列表，元素为原有元素的值的拷贝或者引用的拷贝
    if isinstance(obj, list):
        return [deepCopy(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(deepCopy(item) for item in obj)
    elif isinstance(obj, dict):
        return {key: deepCopy(value) for key, value in obj.items()}
    elif isinstance(obj, set):
        return {deepCopy(item) for item in obj}
    else:
        return obj


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def __deepcopy__():
        return "深拷贝对象"


root = Node("根节点")
child1 = Node("子节点1")
child2 = Node("子节点2")
root.add_child(child1)
root.add_child(child2)
print(root.children)
print(child1.parent.value)

try:
    deep_copy = deepCopy(root)
    print(id(root))
    print(id(deep_copy))
    print(deep_copy.children)
    print(deep_copy.children[0].parent.value)
except Exception as e:
    print("拷贝失败")
    # list set dict .copy
