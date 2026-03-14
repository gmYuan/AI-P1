


# -------------------------------------------------------------------------------
# 1.15-1.1 具名元组的 _replace方法注意点

from collections import namedtuple

# 定义一个Person具名元组类，包含4个字段：name, age, city, job
Person = namedtuple("Person", ["name", "age", "city", "job"])
person = Person("Alice", 25, "New York", "Engineer")

#'Person' object does not support item assignment
# person[0] = "Bob"

# AttributeError: can't set attribute
# person.age = 35

new_person = person._replace(age=35, name="Bob")
# 会创建一个新的 具名元组: Person(name='Bob', age=35, city='New York', job='Engineer')
print(new_person)
# 不会影响旧的 具名元组: Person(name='Alice', age=25, city='New York', job='Engineer')
print(person)
