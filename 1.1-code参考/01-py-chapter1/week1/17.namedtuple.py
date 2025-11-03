from collections import namedtuple

"""
# 这是一个名为Point的具名元组类
Point = namedtuple("Point", ["x", "y"])

p = Point(10, 20)
print(p)
print(p.x, p.y)
print(p[0], p[1])


Person1 = namedtuple("Person", ["name", "age", "city"])
person1 = Person1("Alice", 25, "New York")
print(f"方式1 列表定义:{person1}")

Person2 = namedtuple("Person", "name age city")
person2 = Person2("Alice", 25, "New York")
print(f"方式2 用空格分割的字符串:{person2}")

Person3 = namedtuple("Person", "name,age,city")
person3 = Person3("Alice", 25, "New York")
print(f"方式3 用逗号分割的字符串:{person3}")

Person4 = namedtuple("Person", ("name", "age", "city"))
person4 = Person4("Alice", 25, "New York")
print(f"方式4 元组定义:{person4}")


# 导入namedtuple，用于定义具名元组
from collections import namedtuple

# 打印 "普通元组方式:" 的标题
print("1. 普通元组方式:")

# 创建一个普通元组，包含姓名、年龄、城市、职业
person_tuple = ("Alice", 25, "New York", "Engineer")

# 打印整个普通元组
print(f"   person_tuple = {person_tuple}")

# 通过索引访问元组中的第一个元素（姓名）并打印
print(f"   姓名: {person_tuple[0]}")

# 通过索引访问元组中的第二个元素（年龄）并打印
print(f"   年龄: {person_tuple[1]}")

# 通过索引访问元组中的第三个元素（城市）并打印
print(f"   城市: {person_tuple[2]}")

# 通过索引访问元组中的第四个元素（职业）并打印
print(f"   职业: {person_tuple[3]}")

# 打印空行和 "namedtuple方式:" 的标题
print("\n2. namedtuple方式:")

# 定义一个具名元组类型Person，包含四个字段：name, age, city, job
Person = namedtuple("Person", ["name", "age", "city", "job"])

# 创建一个Person类型的实例，赋值给person_named
person_named = Person("Alice", 25, "New York", "Engineer")

# 打印整个Person具名元组实例
print(f"   person_named = {person_named}")

# 通过属性名访问person_named的姓名并打印
print(f"   姓名: {person_named.name}")

# 通过属性名访问person_named的年龄并打印
print(f"   年龄: {person_named.age}")

# 通过属性名访问person_named的城市并打印
print(f"   城市: {person_named.city}")

# 通过属性名访问person_named的职业并打印
print(f"   职业: {person_named.job}")

"""


# 导入namedtuple，可以创建带字段名的元组类型
from collections import namedtuple

# 定义一个Person具名元组类，包含4个字段：name, age, city, job
Person = namedtuple("Person", ["name", "age", "city", "job"])

# 功能1：获取字段信息
print("1. 字段信息:")
# 打印Person类型的所有字段名
print(f"   字段名: {Person._fields}")
# 打印字段数量（长度）
print(f"   字段数量: {len(Person._fields)}")

# 功能2：转换为字典
print("\n2. 转换为字典:")
# 创建一个Person实例，包含姓名、年龄、城市和职业
person = Person("Alice", 25, "New York", "Engineer")
# 将Person实例转换为字典
person_dict = person._asdict()
# 打印原始Person对象
print(f"   原始对象: {person}")
# 打印转换后的字典
print(f"   转换后字典: {person_dict}")

# 功能3：替换字段值
print(f"   原始对象: {person}")
# 使用_replace方法，替换age和city字段，生成新的Person对象
new_person = person._replace(age=26, city="Boston")
# 打印替换字段后的新对象
print(f"   替换后对象: {new_person}")

# 功能4：从字典创建
print("\n4. 从字典创建:")
# 定义一个字典，包含Person的所有字段信息
person_data = {"name": "Bob", "age": 30, "city": "London", "job": "Designer"}
# 使用**运算符，把字典内容作为参数传递，创建Person对象
person_from_dict = Person(**person_data)
# 打印从字典创建的Person对象
print(f"   从字典创建: {person_from_dict}")

# 功能5：解包操作
print("\n5. 解包操作:")
# 对person对象进行解包，分别赋值给name, age, city, job变量
name, age, city, job = person
# 打印解包后的结果
print(f"   解包结果: name={name}, age={age}, city={city}, job={job}")

# 功能6：迭代操作
print("\n6. 迭代操作:")
print("   迭代结果:", end=" ")
for field in person:
    print(field, end=" ")
# 打印换行
print()

# 功能7：类型检查
print("\n7. 类型检查:")
# 打印person对象的实际类型
print(f"   对象类型: {type(person)}")
# 检查person是否属于内置tuple类型
print(f"   是否为元组: {isinstance(person, tuple)}")
# 检查person是否属于Person类型
print(f"   是否为Person类型: {isinstance(person, Person)}")
