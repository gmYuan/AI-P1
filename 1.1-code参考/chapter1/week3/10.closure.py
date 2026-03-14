"""


# 定义一个外部函数，接受参数x
def outer_function(x):
    # 定义一个内部函数，接受参数y
    def inner_function(y):
        # 内部函数返回x和y的和
        # 注意：这里引用了外部函数的变量x
        return x + y

    # 外部函数返回内部函数
    return inner_function


# 调用外部函数，传入参数10，得到闭包函数
closure_func = outer_function(10)
# 调用闭包函数，传入参数5
result = closure_func(5)
# 打印结果
print(f"闭包函数调用结果: {result}")

# 验证闭包函数仍然可以访问外部变量
print(f"闭包函数类型: {type(closure_func)}")
print(f"闭包函数名称: {closure_func.__name__}")

# 创建多个不同的闭包函数
closure_func_20 = outer_function(20)
closure_func_30 = outer_function(30)

# 测试不同的闭包函数
print(f"闭包函数(20)调用结果: {closure_func_20(5)}")
print(f"闭包函数(30)调用结果: {closure_func_30(5)}")

# 验证每个闭包函数都有独立的状态
print(f"闭包函数(10)和闭包函数(20)是否相同: {closure_func is closure_func_20}")



# 定义一个外部函数，接受参数x
def outer_function(x):
    z = 200
    e = 300
    print(e)

    # 定义一个内部函数，接受参数y
    def inner_function(y):
        # 内部函数返回x和y的和
        # 注意：这里引用了外部函数的变量x
        return x + y + z

    # 外部函数返回内部函数
    return inner_function


# 继续上面的 outer_function 应用
f = outer_function(100)
print(f"f(7) = {f(7)}")  # 输出: 107

# 查看内部函数的 __closure__ 属性
print("闭包的 __closure__ 属性:", f.__closure__)
#__closure__ 属性是一个包含 cell 对象的元组，每个 cell 存储一个被“捕获”的外部变量。
# (<cell at 0x000001AE22C35CC0: int object at 0x00007FF916A2B0D8>, <cell at 0x000001AE22C35DB0: int object at 0x00007FF916A2BD58>)
print("闭包绑定的自由变量:", [cell.cell_contents for cell in f.__closure__])



def make_accumulator(base=0):
    total = base

    def add(num):
        nonlocal total  # 声明 total 是外部（但非全局）变量
        total += num
        return total

    return add


acc = make_accumulator(10)
print(acc(1))  # 11
print(acc(5))  # 16
print(acc(-3))  # 13



# 示例1：乘法器工厂
def make_multiplier(n):
    # 外部函数创建乘法器
    def multiplier(x):
        # 内部函数实现乘法运算
        return x * n

    # 返回内部函数
    return multiplier


# 创建不同的乘法器
times3 = make_multiplier(3)
times5 = make_multiplier(5)
times10 = make_multiplier(10)

# 测试乘法器
print(f"3乘以9: {times3(9)}")
print(f"5乘以7: {times5(7)}")
print(f"10乘以4: {times10(4)}")


# 示例2：幂运算工厂
def make_power(exponent):
    # 外部函数创建幂运算函数
    def power_function(base):
        # 内部函数实现幂运算
        return base**exponent

    # 返回内部函数
    return power_function


# 创建不同的幂运算函数
square = make_power(2)
cube = make_power(3)
fourth_power = make_power(4)

# 测试幂运算函数
print(f"5的平方: {square(5)}")
print(f"3的立方: {cube(3)}")
print(f"2的4次方: {fourth_power(2)}")


# 示例3：字符串处理工厂
def make_string_processor(prefix, suffix):
    # 外部函数创建字符串处理函数
    def process_string(text):
        # 内部函数处理字符串
        return f"{prefix}{text}{suffix}"

    # 返回内部函数
    return process_string


# 创建不同的字符串处理器
html_wrapper = make_string_processor("<div>", "</div>")
bold_wrapper = make_string_processor("**", "**")
quote_wrapper = make_string_processor('"', '"')

# 测试字符串处理器
print(f"HTML包装: {html_wrapper('Hello')}")
print(f"粗体包装: {bold_wrapper('World')}")
print(f"引号包装: {quote_wrapper('Python')}")


# 示例：配置管理器
def create_config_manager():
    # 外部函数创建配置管理器
    config = {}

    def set_config(key, value):
        # 设置配置项
        config[key] = value
        return f"配置项 {key} 已设置为 {value}"

    def get_config(key):
        # 获取配置项
        return config.get(key, None)

    def get_all_config():
        # 获取所有配置项
        return config.copy()

    def update_config(updates):
        # 批量更新配置项
        config.update(updates)
        return f"已更新 {len(updates)} 个配置项"

    def clear_config():
        # 清空配置项
        config.clear()
        return "配置已清空"

    # 返回配置管理函数
    return {
        "set": set_config,
        "get": get_config,
        "get_all": get_all_config,
        "update": update_config,
        "clear": clear_config,
    }


# 创建配置管理器
config_manager = create_config_manager()

# 测试配置管理器
print("配置管理器测试:")
print(config_manager["set"]("database_url", "localhost:5432"))
print(config_manager["set"]("debug_mode", True))
print(config_manager["set"]("max_connections", 100))

print(f"\n获取数据库URL: {config_manager['get']('database_url')}")
print(f"获取调试模式: {config_manager['get']('debug_mode')}")
print(f"获取最大连接数: {config_manager['get']('max_connections')}")

print(f"\n所有配置: {config_manager['get_all']()}")

# 批量更新配置
updates = {"timeout": 30, "retry_count": 3}
print(config_manager["update"](updates))
print(f"更新后配置: {config_manager['get_all']()}")

# 验证数据封装
print(f"\n配置管理器类型: {type(config_manager)}")
print(f"配置管理器方法: {list(config_manager.keys())}")



# 定义一个闭包函数
def outer_function(x):
    # 外部函数定义变量x
    def inner_function(y):
        # 内部函数引用外部变量x
        return x + y

    # 返回内部函数
    return inner_function


# 创建闭包函数
closure_func = outer_function(10)

# 访问闭包的__closure__属性
print(f"闭包函数: {closure_func}")
print(f"闭包属性: {closure_func.__closure__}")
print(f"闭包属性类型: {type(closure_func.__closure__)}")

# 访问cell对象
if closure_func.__closure__:
    print(f"Cell对象数量: {len(closure_func.__closure__)}")
    for i, cell in enumerate(closure_func.__closure__):
        print(f"Cell {i}: {cell}")
        print(f"Cell {i} 内容: {cell.cell_contents}")
        print(f"Cell {i} 类型: {type(cell.cell_contents)}")

# 创建多个闭包函数
closure_func_20 = outer_function(20)
closure_func_30 = outer_function(30)

# 比较不同闭包函数的cell对象
print(f"\n闭包函数(10)的cell内容: {closure_func.__closure__[0].cell_contents}")
print(f"闭包函数(20)的cell内容: {closure_func_20.__closure__[0].cell_contents}")
print(f"闭包函数(30)的cell内容: {closure_func_30.__closure__[0].cell_contents}")

# 验证cell对象的独立性
print(
    f"\n闭包函数(10)和闭包函数(20)的cell对象是否相同: {closure_func.__closure__[0] is closure_func_20.__closure__[0]}"
)


cache = {}
# 示例1：延迟计算工厂
def create_lazy_calculator():
    # 外部函数创建延迟计算器
    cache = {}

    def lazy_calculate(operation, *args):
        # 内部函数实现延迟计算
        key = (operation, args)

        if key not in cache:
            # 如果缓存中没有结果，进行计算
            if operation == "add":
                result = sum(args)
            elif operation == "multiply":
                result = 1
                for arg in args:
                    result *= arg
            elif operation == "power":
                result = args[0] ** args[1]
            else:
                result = None

            # 将结果存入缓存
            cache[key] = result
            print(f"计算 {operation}{args} = {result}")
        else:
            # 如果缓存中有结果，直接返回
            print(f"从缓存获取 {operation}{args} = {cache[key]}")

        return cache[key]

    def get_cache():
        # 获取缓存内容
        return cache

    def clear_cache():
        # 清空缓存
        cache.clear()
        return "缓存已清空"

    # 返回延迟计算函数
    return lazy_calculate, get_cache, clear_cache


# 创建延迟计算器
calc, get_cache, clear_cache = create_lazy_calculator()

# 测试延迟计算
print("延迟计算测试:")
result1 = calc("add", 1, 2, 3, 4, 5)
result2 = calc("multiply", 2, 3, 4)
result3 = calc("power", 2, 10)

# 重复计算（从缓存获取）
result4 = calc("add", 1, 2, 3, 4, 5)
result5 = calc("multiply", 2, 3, 4)

print(f"\n缓存内容: {get_cache()}")
"""
