class SimpleVM:
    # 类里的初始化函数，当创建一个新的类的实例的时候就会调用此函数初始化实例对象
    # 相同于js 中的constructor
    # 第一个参数定死的，自动传入，不需要用户传，指的是当前类的实例 self相当于js中类的this
    def __init__(self):
        # 初始化操作数栈 用来临时保存操作数
        self.stack = []
        # 初始化局部变量字典 python字典类似于js中的对象，里面存的是key value
        self.locals = {}
        # 实始化全局变量字典 存储全局变量 python中也有变量 作用域 作用域链 闭包 垃圾回收机制
        self.globals = {}

    def load_const(self, const):
        # 将常量加入到栈顶 把数字字符串等常量放到栈顶
        self.stack.append(const)
        print(f"加载常量:{const}->栈:{self.stack}")

    # 将操作数栈顶的值存储到指定变量， 把栈顶的值取出来，存储到指定的变量中
    def store_name(self, name):
        if not self.stack:  # !true
            raise RuntimeError("栈为空")  # js throw new RunnerError("栈为空")
        # 取出栈顶的元素 其实就是弹出列表的最后一个元素并返回 js arr.pop()
        value = self.stack.pop()
        # 存储局部变量字段中 python中也有作用域的概念
        self.locals[name] = value
        print(f"存储变量:{name}={value}->栈:{self.stack}")

    # 加载变量的值到操作栈中， 根据变量名找到对应的值，放到栈顶
    def load_name(self, name):
        # 如果变量名在局部变量字典中
        if name in self.locals:
            # python的字典中 不能通过通过.取值的
            value = self.locals[name]
        # 如果在当前的局部作用域内没有找到此变量的值，则会找全局作用域
        elif name in self.globals:
            value = self.globals[name]
        else:
            raise NameError(f"name {name} is not defined")  # 类似于js中的模板字符串
        # 把取出的变量值添加到栈顶
        self.stack.append(value)
        print(f"加载变量:{name}={value},栈:{self.stack}")

    # 执行加法操作 从栈顶取出最近的2个数，相加后再把结果放到栈顶
    def binary_add(self):
        if len(self.stack) < 2:
            raise RuntimeError("栈中的元素不足")
        b = self.stack.pop()
        a = self.stack.pop()
        result = a + b
        self.stack.append(result)
        print(f"加法:{a}+{b}={result},栈:{self.stack}")

    def return_value(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        print(f"返回值:{value}")
        return value


# 字节码相当于英语 不同的操作系统相同于不同的国家的翻译 不同的国家对应不同的操作系统
def vm_execution():
    # 创建PVM虚拟机的实例
    vm = SimpleVM()
    # 这是执行的代码
    print("执行代码: a=10;b=20;c=a+b")
    # 构造指令序列
    instructions = [
        #  这是元组类型，元组就是不可变数组，这个JS里没有，但是python是有的
        ("LOAD_CONST", 10),  # 加载常量10
        ("STORE_NAME", "a"),  # 存储到变量a
        ("LOAD_CONST", 20),  # 加载常量20
        ("STORE_NAME", "b"),  # 存储到变量b
        ("LOAD_NAME", "a"),  # 加载变量a
        ("LOAD_NAME", "b"),  # 加载变量b
        ("BINARY_ADD",),  # 执行加法
        ("STORE_NAME", "c"),  # 存储到变量c
        ("LOAD_NAME", "c"),  # 加载变量c
        ("RETURN_VALUE",),  # 返回值
    ]
    for instruction in instructions:
        # 取出操作码
        op = instruction[0]
        # 取出操作参数 这是一个三元运算符 js =  if condition? true:false| pyton  true if condition false
        # instruction[1:] = instruction.slice(1)
        args = instruction[1:] if len(instruction) > 1 else ()
        # 根据操作码分发指令
        if op == "LOAD_CONST":
            vm.load_const(args[0])
        elif op == "STORE_NAME":
            vm.store_name(args[0])
        elif op == "LOAD_NAME":
            vm.load_name(args[0])
        elif op == "BINARY_ADD":
            vm.binary_add()
        elif op == "RETURN_VALUE":
            result = vm.return_value()
            break
    print(f"最终的结果为:c={result}")


vm_execution()
