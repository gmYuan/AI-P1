
# ----------------------------------------------------------------

class Node:
    def __init__(self, a):
        self.a = a


node1 = Node(1)
print(hasattr(node1, "a"))  # True
print(node1.a)              # 1


dict1 = {"a": 5}
# AttributeError: 'dict' object has no attribute 'a'
# print(dict1.a)
print(hasattr(dict1, "a"))    # False

# 字典的取值用方括号或者 get
print(dict1["a"])              # 5
print(dict1.get("a"))          # 5


# 类的实例也就是对象的取值用.或者 getattr
print(node1.a)                         # 1
# print(node1["a"])#TypeError: 'Node' object is not subscriptable
print(node1.__dict__["a"])             # 1
print(getattr(node1, "a"))             # 1


# tuple1 = (1, 2, 3)
# print(hasattr(tuple1, 1))



# ----------------------------------------------------------------
numbers = ["a", "b", "c"]
dict1 = {item: item for item in numbers}
print(dict1)



s = "['a', 11, 'b', 12, 'c', 13]"
lst1 = eval(s)
print(lst1)

lst = ["a", 1, "b", 2, "c", 3]
dct = {}
for i in range(0, len(lst), 2):
    dct[lst[i]] = lst[i + 1]
print(dct)
