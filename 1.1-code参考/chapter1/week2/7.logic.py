"""


is_admin = True
is_active = False

# 示例1: True and False
# 左侧为True，继续评估右侧，右侧为False，所以返回False
print(f"True and False 的结果是: {True and False}")  # 输出: False

# 示例2: True and True
# 左侧为True，继续评估右侧，右侧为True，所以返回True
print(f"True and True 的结果是: {True and True}")  # 输出: True

# 示例3: False and True
# 左侧为False，直接返回False，右侧不评估
print(f"False and True 的结果是: {False and True}")  # 输出: False

# 示例4: False and False
# 左侧为False，直接返回False，右侧不评估
print(f"False and False 的结果是: {False and False}")  # 输出: False

# 示例5: 变量组合
# is_admin为True，is_active为False，结果为False
print(f"is_admin and is_active 的结果是: {is_admin and is_active}")  # 输出: False

# 示例6: 多个条件组合
age = 25
has_license = True
is_insured = True
# 所有条件都为True时，结果为True
can_drive = age >= 18 and has_license and is_insured
print(f"可以驾驶: {can_drive}")  # 输出: True


# 定义两个布尔值用于演示
has_permission = True
is_guest = False

# 示例1: True or False
# 左侧为True，直接返回True，右侧不评估
print(f"True or False 的结果是: {True or False}")  # 输出: True

# 示例2: False or False
# 左侧为False，继续评估右侧，右侧为False，所以返回False
print(f"False or False 的结果是: {False or False}")  # 输出: False

# 示例3: False or True
# 左侧为False，继续评估右侧，右侧为True，所以返回True
print(f"False or True 的结果是: {False or True}")  # 输出: True

# 示例4: True or True
# 左侧为True，直接返回True，右侧不评估
print(f"True or True 的结果是: {True or True}")  # 输出: True

# 示例5: 变量组合
# has_permission为True，is_guest为False，结果为True
print(
    f"has_permission or is_guest 的结果是: {has_permission or is_guest}"
)  # 输出: True

# 示例6: 多个条件组合
is_weekend = True
is_holiday = False
is_vacation = False
# 只要有一个条件为True，结果为True
can_relax = is_weekend or is_holiday or is_vacation
print(f"可以休息: {can_relax}")  # 输出: True


# 定义一个布尔值用于演示
is_logged_in = True

# 示例1: not True
# 对True取反，结果为False
print(f"not True 的结果是: {not True}")  # 输出: False

# 示例2: not False
# 对False取反，结果为True
print(f"not False 的结果是: {not False}")  # 输出: True

# 示例3: 变量取反
# is_logged_in为True，取反后为False
print(f"not is_logged_in 的结果是: {not is_logged_in}")  # 输出: False

# 示例4: 复杂条件取反
age = 17
is_adult = age >= 18
is_minor = not is_adult
print(f"年龄: {age}")
print(f"是成年人: {is_adult}")
print(f"是未成年人: {is_minor}")  # 输出: True

# 示例5: 双重否定
original_value = True
double_negation = not not original_value
print(f"原始值: {original_value}")
print(f"双重否定后: {double_negation}")  # 输出: True


# 成员运算符in，not in，如果某个类的继承父类的话，子类上没有，会往父类上去查找？


class Parent:
    def __contains__(self, item):
        print("Parent __contains__", item)
        return item == "2"


class Child(Parent):
    pass


child = Child()
child.__contains__("2")
# 因为 in 会自动调取 __contains__方法的返回值
print("2" in child)

# js和python 都可以 1 < a < 3


a = 2
print(1 < a and a < 3)
print(1 < a < 3)



# 被认为是 False 的对象
print("被认为是 False 的对象:")
print(f"bool(None): {bool(None)}")  # 输出: False
print(f"bool(False): {bool(False)}")  # 输出: False
print(f"bool(0): {bool(0)}")  # 输出: False
print(f"bool(0.0): {bool(0.0)}")  # 输出: False
print(f"bool(0j): {bool(0j)}")  # 输出: False
print(f"bool(''): {bool('')}")  # 输出: False

print(f"bool([]): {bool([])}")  # 输出: False
print(f"bool(()): {bool(())}")  # 输出: False
print(f"bool({{}}): {bool({})}")  # 输出: False
print(f"bool(set()): {bool(set())}")  # 输出: False

# 被认为是 True 的对象
print("\n被认为是 True 的对象:")
print(f"bool(1): {bool(1)}")  # 输出: True
print(f"bool(3.14): {bool(3.14)}")  # 输出: True
print(f"bool('hello'): {bool('hello')}")  # 输出: True
print(f"bool([1, 2]): {bool([1, 2])}")  # 输出: True
print(f"bool((1, 2)): {bool((1, 2))}")  # 输出: True
print(f"bool({{'a': 1}}): {bool({'a': 1})}")  # 输出: True
print(f"bool({{1, 2}}): {bool({1, 2})}")  # 输出: True


print(int(True))
print(int(False))


## int float str bool set list tuple
obj = {}
print(len(obj.keys()) == 0)



def len():
    print("len")


len()



# 定义一个空类 Class1
class Class1:
    pass


# 定义一个类 Class2，实现了 __len__ 方法，总返回 0
class Class2:
    def __len__(self):
        return 0


# 定义一个类 Class3，实现了 __bool__ 方法，总返回 False
class Class3:
    def __bool__(self):
        return False


# 创建 Class1 的实例
class1 = Class1()
# 创建 Class2 的实例
class2 = Class2()
# 创建 Class3 的实例
class3 = Class3()

# 打印 class1 的布尔值，预期 True
print(f"bool(class1): {bool(class1)}")  # 输出: True
# 打印 class2 的布尔值，由于 __len__ 返回 0，预期 False
print(f"bool(class2): {bool(class2)}")  # 输出: False
# 打印 class3 的布尔值，由于 __bool__ 返回 False，预期 False
print(f"bool(class3): {bool(class3)}")  # 输出: False


# and 运算符的短路特性
print("and 运算符的短路特性:")
# 示例1: False and (1/0)
# 第一个操作数 False 已经决定了结果，所以不会执行 1/0，避免了 ZeroDivisionError
result_and = False and (1 / 0)
print(f"False and (1/0) 的结果是: {result_and}")  # 输出: False

# 示例2: True and (1/0)
# 第一个操作数为 True，会继续评估第二个操作数，这里会引发 ZeroDivisionError
try:
    result_and2 = True and (1 / 0)
except ZeroDivisionError:
    print("True and (1/0) 引发了 ZeroDivisionError")

# or 运算符的短路特性
# 示例1: True or (1/0)
# 第一个操作数 True 已经决定了结果，所以不会执行 1/0，避免了 ZeroDivisionError
result_or = True or (1 / 0)
print(f"True or (1/0) 的结果是: {result_or}")  # 输出: True

# 示例2: False or (1/0)
# 第一个操作数为 False，会继续评估第二个操作数，这里会引发 ZeroDivisionError
try:
    result_or2 = False or (1 / 0)
except ZeroDivisionError:
    print("False or (1/0) 引发了 ZeroDivisionError")

and 运算符遵循以下规则：

从左到右依次判断
遇到第一个假值（False）就停止，并返回这个假值
如果所有值都为真，返回最后一个值

# 示例1: 1 and 2
# 1 是真值，继续评估 2，返回 2
print(f"1 and 2 的结果是: {1 and 2}")  # 输出: 2

# 示例2: 0 and 5
# 0 是假值，直接返回 0
print(f"0 and 5 的结果是: {0 and 5}")  # 输出: 0

# 示例3: 'hello' and []
# 'hello' 是真值，继续评估 []，返回 []
print(f"'hello' and [] 的结果是: {'hello' and []}")  # 输出: []

# 示例4: [] and 'world'
# [] 是假值，直接返回 []
print(f"[] and 'world' 的结果是: {[] and 'world'}")  # 输出: []

# 示例5: None and 'test'
# None 是假值，直接返回 None
print(f"None and 'test' 的结果是: {None and 'test'}")  # 输出: None

# 示例6: 'test' and None
# 'test' 是真值，继续评估 None，返回 None
print(f"'test' and None 的结果是: {'test' and None}")  # 输出: None


or 运算符遵循以下规则：

从左到右依次判断
遇到第一个真值（True）就停止，并返回这个真值
如果所有值都为假，返回最后一个值

# 示例1: 0 or 3
# 0 是假值，继续评估 3，返回 3
print(f"0 or 3 的结果是: {0 or 3}")  # 输出: 3

# 示例2: 10 or 20
# 10 是真值，直接返回 10
print(f"10 or 20 的结果是: {10 or 20}")  # 输出: 10

# 示例3: '' or 'world'
# '' 是假值，继续评估 'world'，返回 'world'
print(f"'' or 'world' 的结果是: {'' or 'world'}")  # 输出: world

# 示例4: 'hello' or 'world'
# 'hello' 是真值，直接返回 'hello'
print(f"'hello' or 'world' 的结果是: {'hello' or 'world'}")  # 输出: hello

# 示例5: None or 'test'
# None 是假值，继续评估 'test'，返回 'test'
print(f"None or 'test' 的结果是: {None or 'test'}")  # 输出: test

# 示例6: 'test' or None
# 'test' 是真值，直接返回 'test'
print(f"'test' or None 的结果是: {'test' or None}")  # 输出: test
"""

# not 运算符总是返回布尔值 True 或 False
print("not 运算符总是返回布尔值:")

# 示例1: not 0
# 0 是假值，取反后返回 True
print(f"not 0 的结果是: {not 0}")  # 输出: True

# 示例2: not 1
# 1 是真值，取反后返回 False
print(f"not 1 的结果是: {not 1}")  # 输出: False

# 示例3: not 'Python'
# 'Python' 是真值，取反后返回 False
print(f"not 'Python' 的结果是: {not 'Python'}")  # 输出: False

# 示例4: not ''
# '' 是假值，取反后返回 True
print(f"not '' 的结果是: {not ''}")  # 输出: True

# 示例5: not []
# [] 是假值，取反后返回 True
print(f"not [] 的结果是: {not []}")  # 输出: True

# 示例6: not [1, 2, 3]
# [1, 2, 3] 是真值，取反后返回 False
print(f"not [1, 2, 3] 的结果是: {not [1, 2, 3]}")  # 输出: False
