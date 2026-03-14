"""
# 定义一个名为Dog的类
class Dog:
    # 定义Dog类的一个方法speak
    def speak(self):
        # 返回字符串"Woof!"
        return "Woof!"


# 定义一个新的函数new_speak，它将替换Dog类的speak方法
# 注意：由于它将作为实例方法被调用，所以需要接受self参数
def new_speak(self):
    # 返回字符串"Meow!"
    return "Meow!"


# 创建Dog类的一个实例对象
dog = Dog()

# 调用dog对象的原始speak方法并打印结果
# 预期输出: Woof!
print(dog.speak())

# 执行猴子补丁：将Dog类的speak方法替换为new_speak函数
# 此时，所有Dog的实例（包括dog）的speak方法都将指向new_speak
Dog.speak = new_speak

# 再次调用dog对象的speak方法并打印结果
# 由于已经进行了猴子补丁，现在它会调用new_speak函数
# 预期输出: Meow!
print(dog.speak())



# 定义一个简单的类
class Calculator:
    # 定义add方法，用于加法运算
    def add(self, a, b):
        # 返回a和b的和
        return a + b

    # 定义multiply方法，用于乘法运算
    def multiply(self, a, b):
        # 返回a和b的乘积
        return a * b


# 创建一个Calculator实例
calc = Calculator()

# 调用原始方法
print("原始add方法结果:", calc.add(2, 3))
print("原始multiply方法结果:", calc.multiply(2, 3))


# 定义一个新的add方法，用于替换原始方法
def new_add(self, a, b):
    # 返回a和b的和的平方
    return (a + b) ** 2


# 定义一个新的multiply方法，用于替换原始方法
def new_multiply(self, a, b):
    # 返回a和b的乘积加上10
    return a * b + 10


# 执行猴子补丁：替换Calculator类的方法
Calculator.add = new_add
Calculator.multiply = new_multiply

# 调用修改后的方法
print("修改后add方法结果:", calc.add(2, 3))
print("修改后multiply方法结果:", calc.multiply(2, 3))


# 模拟一个第三方库的模块
class ThirdPartyLibrary:
    # 定义第三方库的方法
    def process_data(self, data):
        # 原始处理逻辑：简单返回数据
        return f"Processed: {data}"

    # 定义另一个方法
    def validate_input(self, input_data):
        # 原始验证逻辑：总是返回True
        return True


# 创建第三方库实例
lib = ThirdPartyLibrary()

# 调用原始方法
print("原始process_data结果:", lib.process_data("test"))
print("原始validate_input结果:", lib.validate_input("invalid"))


# 定义新的处理函数
def enhanced_process_data(self, data):
    # 增强的处理逻辑：添加时间戳
    import datetime

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] Enhanced: {data.upper()}"


# 定义新的验证函数
def strict_validate_input(self, input_data):
    # 严格的验证逻辑：检查输入长度
    return len(input_data) > 0 and isinstance(input_data, str)


# 执行猴子补丁：替换第三方库的方法
ThirdPartyLibrary.process_data = enhanced_process_data
ThirdPartyLibrary.validate_input = strict_validate_input

# 调用修改后的方法
print("修改后process_data结果:", lib.process_data("test"))
print("修改后validate_input结果:", lib.validate_input("valid"))
print("修改后validate_input结果:", lib.validate_input(""))


# 定义一个简单的类
class Person:
    # 定义构造函数
    def __init__(self, name):
        # 初始化name属性
        self.name = name


# 创建Person实例
person = Person("Alice")

# 打印原始属性
print("原始name属性:", person.name)

# 动态添加新属性
person.age = 25
person.email = "alice@example.com"

# 打印新添加的属性
print("动态添加的age属性:", person.age)
print("动态添加的email属性:", person.email)


# 动态添加新方法
def introduce(self):
    # 返回自我介绍
    return f"Hi, I'm {self.name}, {self.age} years old, email: {self.email}"


# 将方法绑定到实例 __get__
person.introduce = introduce.__get__(person, Person)

# 调用动态添加的方法
print("动态添加的方法结果:", person.introduce())


# 定义一个简单的类
class MathUtils:
    # 定义静态方法
    @staticmethod
    def add(a, b):
        # 返回a和b的和
        return a + b


# 创建MathUtils实例
math = MathUtils()

# 调用原始方法
print("原始add方法结果:", math.add(2, 3))


# 动态添加新方法到类
def subtract(self, a, b):
    # 返回a和b的差
    return a - b


def multiply(self, a, b):
    # 返回a和b的乘积
    return a * b


# 执行猴子补丁：添加新方法到类
MathUtils.subtract = subtract
MathUtils.multiply = multiply

# 调用新添加的方法
print("动态添加的subtract方法结果:", math.subtract(5, 3))
print("动态添加的multiply方法结果:", math.multiply(2, 3))




# 模拟一个需要快速修复的bug
class BuggyService:
    # 定义有bug的方法
    def calculate_tax(self, amount):
        # 原始实现有bug：税率计算错误
        return amount * 0.1  # 应该是0.15

    # 定义另一个方法
    def format_currency(self, amount):
        # 原始实现有bug：格式不正确
        return f"${amount}"  # 应该是f"${amount:.2f}"


# 创建服务实例
service = BuggyService()

# 调用有bug的方法
print("原始calculate_tax结果:", service.calculate_tax(100))
print("原始format_currency结果:", service.format_currency(100.5))


# 定义修复后的方法
def fixed_calculate_tax(self, amount):
    # 修复后的税率计算：使用正确的税率0.15
    return amount * 0.15


def fixed_format_currency(self, amount):
    # 修复后的货币格式：保留两位小数
    return f"${amount:.2f}"


# 执行猴子补丁：快速修复bug
BuggyService.calculate_tax = fixed_calculate_tax
BuggyService.format_currency = fixed_format_currency

# 调用修复后的方法
print("修复后calculate_tax结果:", service.calculate_tax(100))
print("修复后format_currency结果:", service.format_currency(100.5))



# 模拟猴子补丁可能带来的问题
class OriginalClass:
    # 定义原始方法
    def process(self, data):
        # 原始处理逻辑
        return f"Original: {data}"


# 创建实例
obj = OriginalClass()

# 调用原始方法
print("原始process结果:", obj.process("test"))


# 定义第一个补丁
def patch1_process(self, data):
    # 第一个补丁：添加前缀
    return f"Patch1: {data}"


# 应用第一个补丁
OriginalClass.process = patch1_process
print("第一个补丁后process结果:", obj.process("test"))


# 定义第二个补丁
def patch2_process(self, data):
    # 第二个补丁：添加后缀
    return f"Patch2: {data}"


# 应用第二个补丁（覆盖第一个）
OriginalClass.process = patch2_process
print("第二个补丁后process结果:", obj.process("test"))

# 问题：第一个补丁被覆盖了，这可能导致意外的行为
# 这就是猴子补丁的一个缺点：难以追踪和调试
"""
