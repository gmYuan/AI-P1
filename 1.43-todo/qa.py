
# ----------------------------------------------------------------




"""

class Node:
    def __init__(self):
        pass

    def add_friend(self, friend):
        self.friend = friend


node1 = Node()
node2 = Node()
node1.add_friend(node2)
node2.add_friend(node1)

list1 = []
list2 = []
list1[0] = list2
list2[0] = list1



class Node:
    def __init__(self, a):
        self.a = a


node1 = Node(1)
print(hasattr(node1, "a"))
print(node1.a)

dict1 = {"a": 1}
# AttributeError: 'dict' object has no attribute 'a'
# print(dict1.a)
print(hasattr(dict1, "a"))
# 字典的取值用方括号或者 get
print(dict1["a"])
print(dict1.get("a"))
# 类的实例也就是对象的取值用.或者 getattr
print(node1.a)
# print(node1["a"])#TypeError: 'Node' object is not subscriptable
print(node1.__dict__["a"])
print(getattr(node1, "a"))

# tuple1 = (1, 2, 3)
# print(hasattr(tuple1, 1))
"""



"""
numbers = ["a", "b", "c"]
dict1 = {item: item for item in numbers}
print(dict1)


# s = "['a', 1, 'b', 2, 'c', 3]"
# lst = eval(s)

lst = ["a", 1, "b", 2, "c", 3]
dct = {}
for i in range(0, len(lst), 2):
    dct[lst[i]] = lst[i + 1]
print(dct)


message = "用户 {} 登录成功 {} "
args = ("Alice", "2")
print(message.format(*args))


def wrapper(*args, **kwargs):
    pass


def register():
    print("register")


wrapper.register = register

wrapper.register()
"""