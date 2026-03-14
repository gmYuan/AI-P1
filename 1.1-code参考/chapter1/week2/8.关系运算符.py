"""
# 基本字符串比较
print("apple" == "apple")  # True
print("apple" != "banana")  # True
print("apple" < "banana")  # True，因'a' < 'b'
print("grape" > "apple")  # True，因'g' > 'a'

# 区分大小写
print("Apple" < "apple")  # True，因'A'(65) < 'a'(97)
print("abc" < "abd")  # True，因'c' < 'd'
print("abc" < "ab")  # False，短串排序靠前

# 空字符串比较
print("" < "a")  # True

# 实际场景应用：排序
fruits = ["banana", "apple", "cherry"]
print(sorted(fruits))  # ['apple', 'banana', 'cherry']

print("1" > 1)  # TypeError: '>' not supported between instances of 'str' and 'int'


# 定义列表变量
list1 = [1, 2, 3]
list2 = [1, 2, 4]
list3 = [1, 2, 3]
list4 = [1, 2]

# 列表比较（按元素逐个比较）
print(f"{list1} < {list2}: {list1 < list2}")  # [1, 2, 3] < [1, 2, 4]: True
print(f"{list1} > {list2}: {list1 > list2}")  # [1, 2, 3] > [1, 2, 4]: False
print(f"{list1} == {list3}: {list1 == list3}")  # [1, 2, 3] == [1, 2, 3]: True
print(f"{list1} != {list2}: {list1 != list2}")  # [1, 2, 3] != [1, 2, 4]: True

# 长度不同的列表比较
print(f"{list1} > {list4}: {list1 > list4}")  # [1, 2, 3] > [1, 2]: True
print(f"{list4} < {list1}: {list4 < list1}")  # [1, 2] < [1, 2, 3]: True

# 嵌套列表比较
print("\n=== 嵌套列表比较 ===")
nested_list1 = [[1, 2], [3, 4]]
nested_list2 = [[1, 2], [3, 5]]
print(f"{nested_list1} < {nested_list2}: {nested_list1 < nested_list2}")

# 混合类型列表比较
print("\n=== 混合类型列表比较 ===")
mixed_list1 = [1, "hello", 3.14]
mixed_list2 = ["1", "world", 3.14]
print(f"{mixed_list1} < {mixed_list2}: {mixed_list1 < mixed_list2}")


v1 = "3.9.1".split(".")  # ["3","9","1"]
v2 = "3.10.0".split(".")  # ["3","10","0"]
print([int(x) for x in v1] < [int(x) for x in v2])  # True


x, y, z = 3, 7, 12

print(1 < x < 10)  # True   相当于(1 < x and x < 10)
print(x < y < z)  # True   相当于(x < y and y < z)
print(x == 3 != y)  # True   相当于(x == 3 and 3 != y)
print(x < y > 5)  # True   相当于(x < y and y > 5)
print(5 < x > 1)  # False  因为x=3不大于5


print(x < 2 < 9)


# 判断一个数是否位于指定范围内
score = 76
if 60 <= score < 90:
    print("成绩良好")

# 判断多个递增量
a, b, c, d = 1, 2, 3, 4
if a < b < c < d:
    print("严格递增")

# 判断日期是否在有效区间
year = 2023
if 2000 <= year <= 2099:
    print("本世纪内")

# 两个列表大于小于判断有啥意义吗

print(5 == "5")
print(5 != "5")

print(10 < 20)  # True，同类型比较
print(3.0 < 5)  # True，float 与 int 比较
print("abc" < "bcd")  # True，字符串按字典序

print(42 == 42.0)  # True，数字类型允许==比较
print("3.14" == 3.14)  # False，字符串和数字不等价

# print(2 < '4')  # TypeError, int 和 str 不能用<比较

a = [1, 2]
b = [1, 3]
print(a < b)  # True，列表按元素依次比较

# 不同容器类型不能直接用关系比较符号
# print([1, 2] < (1, 2))  # TypeError
# TypeError: '<' not supported between instances of 'list' and 'tuple'

# 集合和字典只支持==和!=比较
print({1, 2} == {2, 1})  # True，元素相同无序
print({"x": 1} == {"x": 1})  # True，字典内容完全相同


print(int("1") > 1)
print("1" > str(1))

set1 = {1}
set2 = {2}
print(set1 < set2)
print(set1 > set2)
print(set1 == set2)
print(set1 != set2)


# 导入math模块
import math

# 定义两个浮点数
a = 0.1 * 3
b = 0.3
c = 0.1 + 0.2
# 错误的方式，可能为False
print(a == b)  # False，因为浮点数存在精度误差
print(b == c)
# 正确方式1：用abs()判断是否足够接近
print(abs(a - b) < 1e-9)  # True，差距小于指定容差，认为相等

# 正确方式2：用math.isclose()，推荐方式
print(math.isclose(a, b))  # True，默认容差设置适用大多数场景

# math.isclose可以自定义容差
print(math.isclose(a, b, rel_tol=1e-12))  # True，可以调整容差要求



a = {1,2}
b = {1,2,3}
print(a<b) # True


# == 和is not使用场景有什么区别

str1 = ["abc"]
str2 = ["abc"]
print(id(str1), id(str2))
print(str1 == str2)
print(str1 is str2)


# === 嵌套列表的比较 ===
nested_list1 = [[1, 2], [3, 4]]
nested_list2 = [[1, 2], [3, 5]]

# 比较嵌套列表内容是否小于
print(nested_list1 < nested_list2)  # True，因为最后的4 < 5

# === 嵌套字典的比较 ===
dict1 = {"a": 1, "b": {"x": 2, "y": 3}}
dict2 = {"a": 1, "b": {"x": 2, "y": 3}}
dict3 = {"a": 1, "b": {"x": 2, "y": 4}}

print(dict1 == dict2)  # True，所有内容相同
print(dict1 == dict3)  # False，b.y 值不同

# === 复杂嵌套结构的真实场景应用 ===

# 比较两个多层嵌套配置是否一致
config1 = {"name": "服务A", "params": {"debug": True, "level": 3, "nodes": [1, 2, 3]}}
config2 = {"name": "服务A", "params": {"debug": True, "level": 3, "nodes": [1, 2, 3]}}
print(config1 == config2)  # True，全部一致

# 如果配置略有不同
config3 = {
    "name": "服务A",
    "params": {"debug": False, "level": 3, "nodes": [1, 2, 3]},  # 注意这里不同
}
print(config1 == config3)  # False

# === 混合类型复杂结构 ===
mixed1 = [1, {"a": [2, 3]}, (4, 5)]
mixed2 = [1, {"a": [2, 3]}, (4, 5)]
print(mixed1 == mixed2)  # True

mixed3 = [1, {"a": [2, 4]}, (4, 5)]
# TypeError 不能比较字典的大小
print(
    mixed1 < mixed3
)  # TypeError: '<' not supported between instances of 'dict' and 'dict'




# 定义一个Person类，支持自定义比较
class Person:
    def __init__(self, name, age, salary):
        # 初始化对象属性
        self.name = name
        self.age = age
        self.salary = salary

    def __eq__(self, other):  # a ==b
        # 相等比较：姓名和年龄都相同即为相等
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __lt__(self, other):  # < 关系运算符的重构
        # 小于比较：按年龄进行比较
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __le__(self, other):  # <=
        # 小于等于比较
        if isinstance(other, Person):
            return self.age <= other.age
        return NotImplemented

    def __gt__(self, other):  # >
        # 大于比较
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __ge__(self, other):  # >=
        # 大于等于比较
        if isinstance(other, Person):
            return self.age >= other.age
        return NotImplemented

    def __ne__(self, other):  # !=
        # 不等于比较
        return not self.__eq__(other)

    def __repr__(self):
        # 定义对象的字符串表现形式
        return f"Person(name='{self.name}', age={self.age}, salary={self.salary})"


# 创建一些Person对象进行比较
person1 = Person("Alice", 25, 50000)
person2 = Person("Bob", 30, 60000)
person3 = Person("Alice", 25, 55000)

# 按自定义规则比较
print(person1 == person3)  # True，名字与年龄都相同
print(person1 == person2)  # False，名字或年龄不同
print(person1 < person2)  # True，因为25 < 30
print(person2 > person1)  # True，因为30 > 25
print(person2 != person3)  # True

# 实际开发：自定义对象排序
person_list = [person2, person1, person3]
print(sorted(person_list))  # 将依据年龄完成排序

# 实际开发场景：
# 1. 排序员工信息、学生成绩单、自定义数据对象等
# 2. 实现业务逻辑中的自定义比较需求（如唯一性判定、分组、筛选）


# 定义变量
x = 15
y = 20
z = 25

# 基本布尔运算
print("基本布尔运算:")
print(f"x > 10 and x < 20: {x > 10 and x < 20}")  # True
print(f"y > 15 or y < 10: {y > 15 or y < 10}")  # True
print(f"not (z > 30): {not (z > 30)}")  # True

# 复杂条件判断
print("\n复杂条件判断:")
# 检查x是否在10到20之间
if 10 < x < 20:
    print(f"{x} 在 10 到 20 之间")
else:
    print(f"{x} 不在 10 到 20 之间")

# 检查y是否小于15或大于25
if y < 15 or y > 25:
    print(f"{y} 小于 15 或大于 25")
else:
    print(f"{y} 在 15 到 25 之间")

# 检查z是否不在20到30之间
if not (20 <= z <= 30):
    print(f"{z} 不在 20 到 30 之间")
else:
    print(f"{z} 在 20 到 30 之间")

"""


# 应用1：用户输入验证
def validate_user_input(age, score, name):
    """验证用户输入"""
    errors = []

    # 年龄验证
    if not (18 <= age <= 65):
        errors.append("年龄必须在18到65之间")

    # 分数验证
    if not (0 <= score <= 100):
        errors.append("分数必须在0到100之间")

    # 姓名验证
    if not (2 <= len(name) <= 20):
        errors.append("姓名长度必须在2到20个字符之间")

    if errors:
        return f"验证失败: {', '.join(errors)}"
    else:
        return "验证成功"


# 测试用户输入验证
test_cases = [
    (25, 85, "Alice"),
    (17, 85, "Alice"),
    (25, 105, "Alice"),
    (25, 85, "A"),
    (25, 85, "A" * 25),
]

for age, score, name in test_cases:
    result = validate_user_input(age, score, name)
    print(f"年龄: {age}, 分数: {score}, 姓名: '{name}' -> {result}")


# 应用2：数据范围检查
def check_data_range(data, min_val, max_val):
    """检查数据是否在指定范围内"""
    if min_val <= data <= max_val:
        return f"数据 {data} 在范围 [{min_val}, {max_val}] 内"
    else:
        return f"数据 {data} 超出范围 [{min_val}, {max_val}]"


# 测试数据范围检查
data_points = [5, 15, 25, 35, 45]
min_range = 10
max_range = 40

print(f"\n检查数据是否在 {min_range} 到 {max_range} 范围内:")
for data in data_points:
    result = check_data_range(data, min_range, max_range)
    print(result)


# 应用3：条件筛选
def filter_data(data_list, min_val, max_val):
    """筛选在指定范围内的数据"""
    filtered = [x for x in data_list if min_val <= x <= max_val]
    return filtered


# 测试数据筛选
test_data = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
filtered_data = filter_data(test_data, 15, 35)
print(f"\n原始数据: {test_data}")
print(f"筛选后数据 (15-35): {filtered_data}")
