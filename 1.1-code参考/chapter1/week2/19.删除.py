"""

# 示例列表，用于演示各种删除操作
my_list_original = [1, 2, 3, 4, 2, 5]

# 演示 remove()
# 创建一个新的列表副本，以确保每次操作都在原始状态下进行
my_list_remove = list(my_list_original)
# 打印操作前的列表状态
print(f"操作前列表: {my_list_remove}")
# 从列表中删除第一个匹配到的值 "2"
# ValueError: list.remove(x): x not in list
my_list_remove.remove(2)
# 打印操作后的列表状态
print(f"操作后列表: {my_list_remove}")
# 预期输出: [1, 3, 4, 2, 5]

# 演示 del 语句
# 创建一个新的列表副本
my_list_del = list(my_list_original)
# 打印操作前的列表状态
print(f"操作前列表: {my_list_del}")
# 删除索引为 2 的元素 (即值 3)
# del my_list_del[2]
# 打印操作后的列表状态
# print(f"操作后列表: {my_list_del}")
# 预期输出: [1, 2, 4, 2, 5]
# print("\n")
# del my_list_del[2:4]
# print(f"del操作前列表: {my_list_del}")
# NameError: name 'my_list_del' is not defined
# del my_list_del
print(f"del操作前列表: {my_list_del}")

# 演示 pop()
# 创建一个新的列表副本
my_list_pop = list(my_list_original)
# 打印操作前的列表状态
print(f"操作前列表: {my_list_pop}")
# 删除并返回索引为 1 的元素 (即值 2)
removed_element = my_list_pop.pop(1)
# 打印操作后的列表状态
print(f"操作后列表: {my_list_pop}")
# 打印被删除的元素
print(f"被删除的元素: {removed_element}")
# 预期输出: 列表: [1, 3, 4, 2, 5], 被删除元素: 2
print("\n")

# 演示 pop() 不带索引
# 创建一个新的列表副本
my_list_pop_no_index = [10, 20, 30]
# 打印操作前的列表状态
print(f"操作前列表: {my_list_pop_no_index}")
# 删除并返回列表中的最后一个元素 (即值 30)
last_element = my_list_pop_no_index.pop()
# 打印操作后的列表状态
print(f"操作后列表: {my_list_pop_no_index}")
# 打印被删除的元素
print(f"被删除的元素: {last_element}")
# 预期输出: 列表: [10, 20], 被删除元素: 30


# 演示 del 切片删除
# 创建一个新的列表副本
my_list_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 打印操作前的列表状态
print(f"操作前列表: {my_list_slice}")
# 删除索引 2 到 5 之间的元素（不包括索引 5）
del my_list_slice[2:5]
# 打印操作后的列表状态
print(f"操作后列表: {my_list_slice}")
# 预期输出: [1, 2, 6, 7, 8, 9]
print("\n")

# 演示异常处理
# 创建一个空列表用于演示异常情况
empty_list = []
# 使用 try-except 处理可能的异常
try:
    # 尝试从空列表中删除元素
    empty_list.remove(1)
except ValueError as e:
    # 捕获并打印 ValueError 异常
    print(f"remove() 异常: {e}")

try:
    # 尝试从空列表中弹出元素
    empty_list.pop()
except IndexError as e:
    # 捕获并打印 IndexError 异常
    print(f"pop() 异常: {e}")

try:
    # 尝试删除不存在的索引
    del empty_list[0]
except IndexError as e:
    # 捕获并打印 IndexError 异常
    print(f"del 异常: {e}")


# 从用户输入中收集的数据
user_data = [1, 2, None, 3, 4, None, 5, 6, None, 7]
print(f"原始数据: {user_data}")

# 使用 remove() 删除所有 None 值（需要循环处理）
cleaned_data_remove = list(user_data)
while None in cleaned_data_remove:
    # 删除第一个 None 值
    cleaned_data_remove.remove(None)
print(f"使用 remove() 清理后: {cleaned_data_remove}")

# 使用列表推导式更高效地清理数据
cleaned_data_comprehension = [x for x in user_data if x is not None]
print(f"使用列表推导式清理后: {cleaned_data_comprehension}")


"""


# 定义一个简单的栈类
class SimpleStack:
    # 初始化方法，创建一个空列表用于存储栈元素
    def __init__(self):
        self.items = []

    # 入栈方法，将元素添加到栈顶
    def push(self, item):
        self.items.append(item)

    # 出栈方法，弹出并返回栈顶元素
    def pop(self):
        # 如果栈不为空，则弹出并返回栈顶元素
        if not self.is_empty():
            return self.items.pop()
        else:
            # 如果栈为空，则返回None
            return None

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return len(self.items) == 0

    # 查看栈顶元素但不弹出
    def peek(self):
        # 如果栈不为空，返回栈顶元素
        if not self.is_empty():
            return self.items[-1]
        # 如果栈为空，返回None
        return None


# (1+1)+((2+3
# 定义用于检查括号是否匹配的函数
def is_balanced_parentheses(expression):
    # 创建栈对象
    stack = SimpleStack()
    # 定义括号的对应关系字典
    pairs = {"(": ")", "[": "]", "{": "}"}

    # 遍历表达式中的每一个字符
    for char in expression:
        # 如果字符是左括号，则入栈
        if char in pairs:
            stack.push(char)
        # 如果字符是右括号
        elif char in pairs.values():
            # 如果栈为空或者括号不匹配，则返回False
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False

    # 如果最终栈为空，则括号匹配，返回True，否则返回False
    return stack.is_empty()


# 定义用于测试的括号表达式列表
# test_expressions = ["()", "()[]{}", "(]", "([)]", "{[]}"]
# test_expressions = ["{[()]}"]
test_expressions = ["([)]"]
# 遍历测试用例
for expr in test_expressions:
    # 输出每一个表达式的匹配结果
    print(f"'{expr}' 是否平衡: {is_balanced_parentheses(expr)}")

# 每次往栈中存key，然后从栈中弹出作为key去字典中查找value，拿这个值和下一个字符去匹配，如果匹配成功就继续向下匹配，如果不成功则直接返回false
# 如果匹配则栈为空，如果不匹配则返回false
