
# ----------------------------------------------------------------
import copy

l1 = [1, 2, 3]
l2 = l1.copy()
print(l2)

# 元组没有copy方法， dict set list 有copy方法
t1 = (1, 2, 3)
# t2 = t1.copy()
t3 = copy.copy(t1)  # t1和 t3内存地址是一样的

t4 = t1[:]

print(id(t1))
print(id(t3))
print(id(t4))  # 切片拷贝 也是一样的


t5 = (1, 2, [3, 4])
print(t5)
t5[2][0] = 100
print(t5)



list1 = [1, 2, 3]
list2 = list1[:]
print(id(list1))
print(id(list2))



# ----------------------------------------------------------------

dict1 = {"a": 1, "b": 2}
print(dict1)


class Person:
    def __init__(self):
        self.name = "张三"
        self.age = 30


person = Person()
# 判断person上有没有__dict__
print(hasattr(person, "__dict__"))
print(getattr(person, "__dict__"))

# print(setattr(person.__dict__, "name", "value"))
setattr(person, "name", "123")

print(person.__dict__)

for attr, value in person.__dict__.items():
    print(attr, value)




# ----------------------------------------------------------------

class Person:
    def __init__(self):
        pass

p = Person()
cls = type(p)
print(cls)

p2 = Person.__new__(Person)
print(p2)



# --------------------
class Person:
    def __init__(self):
        self.age = 30

cls = type(Person())
result2 = cls()             # 这样写等于 new + init()
print(result2.age)

result = cls.__new__(cls)   # 这样写等于 new，不会调用 init==> 会构造一个干净的空对象
print(result.age)



# ----------------------------------------------------------------------------------------------
class Node:
    def __init__(self):
        pass

    def add_friend(self, friend):
        self.friend = friend


node1 = Node()
node2 = Node()
node1.add_friend(node2)
node2.add_friend(node1)



# ---------------------------------------------------------
list1 = []
list2 = []
list1[0] = list2
list2[0] = list1