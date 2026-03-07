

"""
# -------------------------------------------------------------------------------
1.8-1.2 创建元组

print(int(True))    # 1
print(int(False))   # 0

print(bool(1))     # True
print(bool(0))     # False



# 元组作为 key
t = (1, 1)
d1 = {t: 1}   # 合法
# list set dict 都不能作为字典的key或者字典的属性
l = []  # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d2 = {l: 1}
"""



"""
# ------------------------------------------------------------------------
1.8-1.3 创建集合

# 一般来说创建空的容器类实例都有两种方式
l1 = []
l2 = list()

t1 = ()
t2 = tuple()

# s1 = {}
s2 = set()

d1 = {}
d2 = dict()


my_list = [1, 2, 2, 3, 3, 4]
unique_set = set(my_list)
print(unique_set)  # {1, 2, 3, 4}

# unique_set.remove(5)   # 5在set里不存在，该方法 会报错
unique_set.discard(5)    # 5在set里不存在，但是该方法 不会报错

"""
