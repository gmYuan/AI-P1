"""

# 定义两个列表，它们的值相同但不是同一个对象
list_a = [1, 2, 3]
list_b = [1, 2, 3]
# 定义两个整数，它们的值不同
int_c = 5
int_d = 6

# 比较 list_a 和 list_b 的值是否不相等
# 预期输出：False，因为它们的值是相等的
print(f"list_a != list_b: {list_a != list_b}")

# 比较 list_a 和 list_b 是否是同一个对象
# 预期输出：False，因为它们在内存中是两个不同的列表对象
print(f"list_a is list_b: {list_a is list_b}")

# 比较 int_c 和 int_d 的值是否不相等
# 预期输出：True，因为5和6的值不相等
print(f"int_c != int_d: {int_c != int_d}")

# 比较 int_c 和 int_d 是否是同一个对象
# 预期输出：False，因为它们是不同的整数对象
print(f"int_c is int_d: {int_c is int_d}")

# 定义一个列表和一个元组，它们的值看起来相似但类型不同
mixed_e = [1, 2, 3]
mixed_f = (1, 2, 3)

# 比较 mixed_e 和 mixed_f 的值是否不相等
# 预期输出：True，因为列表和元组是不同的类型，即使内容相似，值比较也可能不同
print(f"mixed_e != mixed_f: {mixed_e != mixed_f}")


# 定义两个列表，它们的值相同但不是同一个对象
obj_x = [10, 20]
obj_y = [10, 20]

# 比较 obj_x 和 obj_y 是否不是同一个对象
# 预期输出：True，因为它们是两个独立的列表对象，内存地址不同
print(f"obj_x is not obj_y: {obj_x is not obj_y}")

# 定义一个列表，并让另一个变量引用它
obj_p = [30, 40]
obj_q = obj_p  # obj_q 引用了 obj_p 所指向的同一个对象

# 比较 obj_p 和 obj_q 是否不是同一个对象
# 预期输出：False，因为它们引用的是内存中的同一个列表对象
print(f"obj_p is not obj_q: {obj_p is not obj_q}")

# 比较 obj_p 和 obj_q 的值是否不相等
# 预期输出：False，因为它们引用的是同一个对象，值当然相等
print(f"obj_p != obj_q: {obj_p != obj_q}")


# 定义一个变量，初始值为 None
my_variable = None
print(id(my_variable))

# 检查 my_variable 是否不是 None
# 预期输出：Variable is None，因为 my_variable 当前是 None
if my_variable is not None:
    # 如果 my_variable 不是 None，则打印此消息
    print("Variable is not None")
else:
    # 如果 my_variable 是 None，则打印此消息
    print("Variable is None")

# 重新赋值 my_variable 为一个字符串
my_variable = "Hello"

# 再次检查 my_variable 是否不是 None
# 预期输出：Variable is not None，因为 my_variable 现在是一个字符串
if my_variable is not None:
    # 如果 my_variable 不是 None，则打印此消息
    print("Variable is not None")
else:
    # 如果 my_variable 是 None，则打印此消息
    print("Variable is None")

# 错误示范：使用 != None 进行比较
# 尽管在大多数情况下结果相同，但这不是推荐的做法，因为某些自定义对象可能重载 != 运算符
# 预期输出：Variable is not None (通常情况下)
if my_variable != None:
    # 如果 my_variable 不等于 None，则打印此消息
    print("Variable is not None (using != None)")

# 定义两个短字符串，它们可能被缓存
str1_cached = "hello"
str2_cached = "hello"
print(id(str1_cached))
print(id(str2_cached))
# 比较 str1_cached 和 str2_cached 是否是同一个对象
# 预期输出：True，因为短字符串通常会被缓存，它们引用的是同一个对象
print(f"str1_cached is str2_cached: {str1_cached == str2_cached}")
# 比较 str1_cached 和 str2_cached 是否不是同一个对象
# 预期输出：False
print(f"str1_cached is not str2_cached: {str1_cached != str2_cached}")

# 定义两个长字符串或动态生成的字符串，通常不会被缓存
str1_uncached = "hello" * 1000000
str2_uncached = "hello" * 1000000
print(id(str1_uncached))
print(id(str2_uncached))
# 比较 str1_uncached 和 str2_uncached 是否是同一个对象
# 预期输出：False，因为长字符串通常不会被缓存，它们是两个不同的对象
print(f"str1_uncached is str2_uncached: {str1_uncached == str2_uncached}")
# 比较 str1_uncached 和 str2_uncached 是否不是同一个对象
# 预期输出：True
print(f"str1_uncached is not str2_uncached: {str1_uncached != str2_uncached}")


str = "h" * 1000000
# python None js null undefined
# python == js  == ===


class Person:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):  # 都是系统自定义的魔术方法
        return self.id == other.id


p1 = Person("1")
p2 = Person("1")
print(p1 == p2)
print(p1.__eq__(p2))

print(p1 is p2)
print(id(p1) == id(p2))



class Person:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):  # 都是系统自定义的魔术方法
        return True


p1 = Person("1")
print(id(p1))  # 2138489439632
print(id(None))  # 140709736205120
if p1 is None:
    print("p1 is None")
if p1 == None:
    print("p1 == None")



# 那如果把self.id赋值去掉，同时去掉eq方法，那p1会==p2吗
class Person:
    def __init__(self):
        pass


p1 = Person()
p2 = Person()
print(p1 == p2)
print(p1 is p2)
"""

s1 = "a" * 10000000
s2 = "a" * 10000000
print(s1 == s2)
