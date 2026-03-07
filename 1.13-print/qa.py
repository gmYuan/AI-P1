

"""
# -------------------------------------------------------------------------------
1.13-1.1  todo



"""



class Person:
    def __str__(self):
        return f"学生"


p = Person()
# <__main__.Person object at 0x0000020D4C074590>
print(p)


from collections import namedtuple

# 定义一个Person具名元组类，包含4个字段：name, age, city, job
Person = namedtuple("Person", ["name", "age", "city", "job"])
person = Person("Alice", 25, "New York", "Engineer")
#'Person' object does not support item assignment
# person[0] = "Bob"
# AttributeError: can't set attribute
# person.age = 35
new_person = person._replace(age=35, name="Bob")
print(new_person)
print(person)





text_with_whitespace = "apple   orange\tbanana\ncherry"
space_split = text_with_whitespace.split(" ")
print("指定空格分割:", space_split)

# 3个连续空格，第一个视为分割符，没了，
# 第二个是被分割的保留了，
# 那为啥第三个为什么没有被视为分隔符，而是被保留了，

text_with_whitespace = "apple,,,orange\tbanana\ncherry"
space_split = text_with_whitespace.split(",")
print("指定,分割:", space_split)

print(",".join("a,b,c".split(",")))


print(",a,,,b".split(","))  # ['', 'a', '', '', 'b']

