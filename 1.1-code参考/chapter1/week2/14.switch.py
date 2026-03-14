"""
def switch_if_elif(case):

    使用 if-elif-else 结构实现 switch 功能
    适合简单的条件判断场景

    # 根据不同的 case 值返回相应的结果
    if case == "A":
        return "Case A"
    elif case == "B":
        return "Case B"
    elif case == "C":
        return "Case C"
    else:
        return "Default case"


# 测试 if-elif-else 方法
result = switch_if_elif("A")
print(f"if-elif-else 结果: {result}")
# 输出: Case A

result = switch_if_elif("D")
print(f"if-elif-else 结果: {result}")
# 输出: Default case



def switch_dict(case):

    使用字典映射实现 switch 功能
    这是最推荐的方法，性能好且代码简洁

    # 定义映射字典
    switcher = {"A": "Case A", "B": "Case B", "C": "Case C"}
    # 使用 get 方法获取值，如果不存在则返回默认值
    return switcher.get(case, "Default case")


# 测试字典映射方法
result = switch_dict("B")
print(f"字典映射结果: {result}")
# 输出: Case B

result = switch_dict("X")
print(f"字典映射结果: {result}")
# 输出: Default case



def case_a():
    return "Action for case A"


def case_b():
    return "Action for case B"


def case_default():
    return "Default action"


def switch_function_dict(case):
    # 定义函数映射字典
    switcher = {"A": case_a, "B": case_b}
    # 获取对应的函数，如果不存在则使用默认函数
    func = switcher.get(case, case_default)
    # 调用函数并返回结果
    return func()


# 测试函数字典方法
result = switch_function_dict("A")
print(f"函数字典结果: {result}")
# 输出: Action for case A

result = switch_function_dict("Z")
print(f"函数字典结果: {result}")
# 输出: Default action




def switch_match(case):
    # 使用 match 语句进行模式匹配
    # switch var
    match case:
        case "A":
            return "Case A"
        case "B":
            return "Case B"
        case "C":
            return "Case C"
        case _:  # 默认情况  default:
            return "Default case"


# 测试 match 语句方法
result = switch_match("C")
print(f"match 语句结果: {result}")
# 输出: Case C

result = switch_match("Unknown")
print(f"match 语句结果: {result}")
# 输出: Default case



def grade_evaluator(score):
    '''
    使用字典映射实现成绩等级评估
    演示如何处理数值范围的情况
    '''
    # 定义成绩等级映射
    grade_map = {
        range(90, 101): "A",  #  >=90 and <100=  [90,91,..95,.100]
        range(80, 90): "B",
        range(70, 80): "C",
        range(60, 70): "D",
    }

    # 遍历字典查找匹配的范围
    for score_range, grade in grade_map.items():
        if score in score_range:
            return grade

    # 默认返回 F 等级
    return "F"


# 测试成绩评估
scores = [95, 85, 75, 65, 55]
for score in scores:
    # 打印每个分数对应的等级
    grade = grade_evaluator(score)
    print(f"分数 {score} 对应等级: {grade}")


def process_user_input(user_input):

    # 使用 match 语句处理不同类型的输入
    match user_input:
        case "help" | "h" | "?":
            return "显示帮助信息"
        case "quit" | "exit" | "q":
            return "退出程序"
        case "save" | "s":
            return "保存文件"
        case "load" | "l":
            return "加载文件"
        case int() if user_input > 0:
            return f"处理正整数: {user_input}"
        case str() if len(user_input) > 10:
            return f"处理长字符串: {user_input[:10]}..."
        case _:
            return f"未知命令: {user_input}"


# 测试多条件匹配
test_inputs = ["help", "quit", "save", 42, "这是一个很长的字符串", "unknown"]
for inp in test_inputs:
    # 打印每个输入的处理结果
    result = process_user_input(inp)
    print(f"输入 '{inp}' -> {result}")


if True or True:
    print("True")

# TypeError: unsupported operand type(s) for |: 'str' and 'str'
if "help" | "h":
    print("help")


class TrafficLight:

    交通灯状态机实现
    演示如何使用 switch 模式实现状态转换


    def __init__(self):
        # 初始化交通灯状态
        self.state = "RED"
        # 定义状态转换规则
        self.transitions = {"RED": "GREEN", "GREEN": "YELLOW", "YELLOW": "RED"}

    def change_state(self):

        改变交通灯状态

        # 使用字典映射获取下一个状态
        self.state = self.transitions.get(self.state, "RED")
        return self.state

    def get_action(self):

        根据当前状态获取相应的动作

        # 定义状态对应的动作
        actions = {"RED": "停车等待", "GREEN": "可以通行", "YELLOW": "准备停车"}
        return actions.get(self.state, "未知状态")


# 测试交通灯状态机
traffic_light = TrafficLight()
print(f"初始状态: {traffic_light.state} - {traffic_light.get_action()}")

# 模拟几个状态变化周期
for i in range(6):
    # 改变状态
    new_state = traffic_light.change_state()
    # 获取对应的动作
    action = traffic_light.get_action()
    print(f"第 {i+1} 次变化: {new_state} - {action}")

"""

# 在Python中重载操作符 |


class MyClass:
    def __init__(self, value):
        self.value = value

    # 你可以认为这人__or__对应的数字的位运算中的或，而不等同于逻辑运算中的or
    # 重载|操作符 对象在操作符左侧时调用
    def __or__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value | other.value)
        elif isinstance(other, int):
            return MyClass(self.value | other)
        else:
            NotImplemented

    # 重载|操作符 对象在右侧时调用 r right
    def __ror__(self, other):
        return self.__or__(other)

    # representation 表示（最常用）：如 Python 中的 __repr__ 方法译为「表示方法」，用于返回对象的字符串表示
    def __repr__(self):
        return f"MyClass({self.value})"

    def __str__(self):
        return f"MyClass({self.value})"


a = MyClass(5)  # 101
b = MyClass(3)  # 011
# TypeError: unsupported operand type(s) for |: 'MyClass' and 'MyClass'
result1 = a | b
print(result1)
result2 = a | 3
print(result2)

# 1010
# 0101
# 1111
result3 = 10 | a
print(result3)
