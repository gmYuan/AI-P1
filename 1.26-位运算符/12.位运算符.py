

"""
# ---------------------------------------------------------------------------
# 1.26-1.1 按位与- 基本用法

# 示例1: 基本按位与运算
# 定义两个数字，二进制分别为 1100 (十进制 12) 和 1010 (十进制 10)
num1 = 0b1100  # 12
num2 = 0b1010  # 10

# 执行按位与操作
# 1100 & 1010 = 1000 (十进制 8)
# 1100
# 1010
# 1000
result = num1 & num2

# 打印结果，二进制为 1000 (十进制 8)
print(f"0b{bin(num1)[2:]} & 0b{bin(num2)[2:]} = 0b{bin(result)[2:]} (十进制: {result})")

# 示例2: 使用十进制数进行按位与运算
# 定义两个十进制数
a = 12
b = 10
# 执行按位与操作
result_decimal = a & b
# 打印结果
print(f"{a} & {b} = {result_decimal}")  # 12 & 10 = 8


# 示例3: 按位与运算的真值表
print("\n按位与运算真值表:")
print("0 & 0 = 0")  # 0 & 0 = 0
print("0 & 1 = 0")  # 0 & 1 = 0
print("1 & 0 = 0")  # 1 & 0 = 0
print("1 & 1 = 1")  # 1 & 1 = 1


# 示例4: 多个数的按位与运算
# 定义三个数字
x = 15  # 1111
y = 12  # 1100
z = 10  # 1010
        # 1000

# 执行多个数的按位与运算
result_multi = x & y & z
# 打印结果
print(f"\n{x} & {y} & {z} = {result_multi}")  # 15 & 12 & 10 = 8
print(
    f"二进制: {bin(x)[2:]} & {bin(y)[2:]} & {bin(z)[2:]} = {bin(result_multi)[2:]}"
)  # 二进制: 1111 & 1100 & 1010 = 1000


"""



"""
# ---------------------------------------------------------------------------
# 1.26-1.2 按位或- 基本用法

# 示例1: 基本按位或运算
# 定义两个数字，二进制分别为 1100 (十进制 12) 和 1010 (十进制 10)
num1 = 0b1100  # 12
num2 = 0b1010  # 10

# 执行按位或操作
# 1100 | 1010 = 1110 (十进制 14) 8+4+2=14
result = num1 | num2

# 打印结果，二进制为 1110 (十进制 14)
print(f"0b{bin(num1)[2:]} | 0b{bin(num2)[2:]} = 0b{bin(result)[2:]} (十进制: {result})")

# 示例2: 使用十进制数进行按位或运算
# 定义两个十进制数
a = 12
b = 10
# 执行按位或操作
result_decimal = a | b
# 打印结果
print(f"{a} | {b} = {result_decimal}")

# 示例3: 按位或运算的真值表
print("\n按位或运算真值表:")
print("0 | 0 = 0")
print("0 | 1 = 1")
print("1 | 0 = 1")
print("1 | 1 = 1")

# 示例4: 多个数的按位或运算
# 定义三个数字
x = 5  #  0101
y = 12  # 1100
z = 10  # 1010

# 执行多个数的按位或运算
result_multi = x | y | z
# 打印结果
print(f"\n{x} | {y} | {z} = {result_multi}")
print(f"二进制: {bin(x)[2:]} | {bin(y)[2:]} | {bin(z)[2:]} = {bin(result_multi)[2:]}")

"""



"""
# ---------------------------------------------------------------------------
# 1.26-1.3 按位异或- 基本用法

# 示例1: 基本按位异或运算
# 定义两个数字，二进制分别为 1100 (十进制 12) 和 1010 (十进制 10)
num1 = 0b1100  # 12
num2 = 0b1010  # 10

# 执行按位异或操作
# 1100
# 1010
# 0110
# 1100 ^ 1010 = 0110 (十进制 6)
result = num1 ^ num2

# 打印结果，二进制为 0110 (十进制 6)
print(
    f"0b{bin(num1)[2:]} ^ 0b{bin(num2)[2:]} = 0b{bin(result)[2:]} (十进制: {result})"
)  # 0b1100 ^ 0b1010 = 0b110 (十进制: 6)

# 示例2: 使用十进制数进行按位异或运算
# 定义两个十进制数
a = 12
b = 10
# 执行按位异或操作
result_decimal = a ^ b
# 打印结果
print(f"{a} ^ {b} = {result_decimal}")  # 12 ^ 10 = 6


# 示例3: 按位异或运算的真值表
print("\n按位异或运算真值表:")
print("0 ^ 0 = 0")  # 0 ^ 0 = 0
print("0 ^ 1 = 1")  # 0 ^ 1 = 1
print("1 ^ 0 = 1")  # 1 ^ 0 = 1
print("1 ^ 1 = 0")  # 1 ^ 1 = 0


# 示例4: 异或运算的特殊性质
# 任何数与0异或都等于它本身
# 1010
# 0000
# 1010
x = 15
zero_xor = x ^ 0
print(f"\n{x} ^ 0 = {zero_xor}")  # 15 ^ 0 = 15


# 任何数与自身异或都等于0
# 1010
# 1010
# 0000
self_xor = x ^ x
print(f"{x} ^ {x} = {self_xor}")  # 15 ^ 15 = 0


# 异或运算满足交换律
a, b, c = 5, 12, 10
result1 = a ^ b ^ c
result2 = c ^ b ^ a
print(f"({a} ^ {b} ^ {c}) = {result1}")  # (5 ^ 12 ^ 10) = 3
print(f"({c} ^ {b} ^ {a}) = {result2}")  # (10 ^ 12 ^ 5) = 3
print(f"交换律验证: {result1 == result2}")  # 交换律验证: True

## 异或运算满足结合律
result3 = (a ^ b) ^ c
result4 = a ^ (b ^ c)
print(f"(({a} ^ {b}) ^ {c}) = {result3}")  # ((5 ^ 12) ^ 10) = 3
print(f"({a} ^ ({b} ^ {c})) = {result4}")  # (5 ^ (12 ^ 10)) = 3
print(f"结合律验证: {result3 == result4}")  # 结合律验证: True

# 异或运算的性质总结：
# 1. 任何数与0异或都等于它本身
# 2. 任何数与自身异或都等于0
# 3. 异或运算满足交换律
# 4. 异或运算满足结合律

"""



"""
# ---------------------------------------------------------------------------
# 1.26-1.4 按位取反- 基本用法

# 示例1: 基本按位取反运算
# 定义一个数字，二进制表示为 1100 (十进制 12)
num = 0b1100  # 12

# 执行按位取反操作
# ~1100 = -13 (在Python中，~x 等价于 -x-1)
result = ~num

# 打印结果，十进制为 -13
print(f"~0b{bin(num)[2:]} (十进制: {num}) = {result}")

# 验证等价性：-num - 1
print(f"验证等价性: -{num} - 1 = {-num - 1}")


# 示例2: 不同数字的按位取反
# 测试不同的数字
test_numbers = [0, 1, 5, 10, 15, 255]

print("\n不同数字的按位取反:")
for n in test_numbers:
    result = ~n
    print(f"~{n} = {result} (验证: -{n}-1 = {-n-1})")


# 示例3: 按位取反运算的二进制表示
# 定义一个较小的数字以便观察二进制变化
small_num = 5  # 101
result_small = ~small_num

print(f"\n二进制表示:")
print(f"原始数字: {small_num} = 0b{bin(small_num)[2:]}")
print(f"取反结果: {result_small} = 0b{bin(result_small & 0xFF)[2:]}")  # 使用掩码显示8位


# 示例4: 按位取反的实际应用
# 用于快速求负数
def quick_negative(x):
    return ~x


# 测试快速求负数
test_value = 20
negative_result = quick_negative(test_value)
print(f"\n快速求负数: ~{test_value} = {negative_result}")
print(f"验证: -{test_value} - 1 = {-test_value - 1}")

"""




"""
# ---------------------------------------------------------------------------
# 1.26-1.5 左移运算- 基本用法

# 示例1: 基本左移运算
# 定义一个数字，二进制表示为 1100 (十进制 12)
num = 0b1100  # 12

# 将 num 左移 2 位，相当于 num 乘以 2 的 2 次方 (即 4)
shift_amount = 2
result = num << shift_amount

# 0001 1
# 0010 2
# 0100 4

# 打印结果，二进制为 110000 (十进制 48)
print(f"0b{bin(num)[2:]} << {shift_amount} = 0b{bin(result)[2:]} (十进制: {result})")

# 验证乘法结果
print(f"验证乘法: {num} * (2**{shift_amount}) = {num * (2**shift_amount)}")


# 示例2: 不同左移位数的效果
# 测试不同的左移位数
original = 5  # 0101

print(f"\n数字 {original} 的不同左移效果:")
for shift in range(1, 6):
    result = original << shift
    print(f"{original} << {shift} = {result} (二进制: {bin(result)[2:]})")


# 示例3: 左移运算的数学意义
# 左移 n 位相当于乘以 2^n
base_number = 3
print(f"\n左移运算的数学意义 (以 {base_number} 为例):")
for n in range(1, 5):
    shifted = base_number << n
    multiplied = base_number * (2**n)
    print(f"{base_number} << {n} = {shifted}, {base_number} * 2^{n} = {multiplied}")

# 3 << 1 = 6, 3 * 2^1 = 6
# 3 << 2 = 12, 3 * 2^2 = 12
# 3 << 3 = 24, 3 * 2^3 = 24
# 3 << 4 = 48, 3 * 2^4 = 48


# 示例4: 左移运算的实际应用
# 用于快速计算2的幂
def power_of_two(n):
    return 1 << n

# 测试计算2的幂
print(f"\n使用左移计算2的幂:")
for i in range(0, 8):
    result = power_of_two(i)
    print(f"2^{i} = {result}")

"""



"""
# ---------------------------------------------------------------------------
# 1.26-1.6 右移运算- 基本用法

# 示例1: 基本右移运算
# 定义一个数字，二进制表示为 1100 (十进制 12)
num = 0b1100  # 12

# 将 num 右移 2 位，相当于 num 除以 2 的 2 次方 (即 4)
shift_amount = 2
result = num >> shift_amount

# 打印结果，二进制为 0011 (十进制 3)
print(f"0b{bin(num)[2:]} >> {shift_amount} = 0b{bin(result)[2:]} (十进制: {result})")

# 验证除法结果 (整数除法)
print(f"验证除法: {num} // (2**{shift_amount}) = {num // (2**shift_amount)}")


# 示例2: 不同右移位数的效果
# 测试不同的右移位数
original = 48  # 110000

print(f"\n数字 {original} 的不同右移效果:")
for shift in range(1, 6):
    result = original >> shift
    print(f"{original} >> {shift} = {result} (二进制: {bin(result)[2:]})")

# 48 >> 1 = 24 (二进制: 11000)
# 48 >> 2 = 12 (二进制: 1100)
# 48 >> 3 = 6 (二进制: 110)
# 48 >> 4 = 3 (二进制: 11)
# 48 >> 5 = 1 (二进制: 1)


# 示例3: 右移运算的数学意义
# 右移 n 位相当于除以 2^n (整数除法)
base_number = 48
print(f"\n右移运算的数学意义 (以 {base_number} 为例):")
for n in range(1, 5):
    shifted = base_number >> n
    divided = base_number // (2**n)
    print(f"{base_number} >> {n} = {shifted}, {base_number} // 2^{n} = {divided}")

# 48 >> 1 = 24, 48 // 2^1 = 24
# 48 >> 2 = 12, 48 // 2^2 = 12
# 48 >> 3 = 6, 48 // 2^3 = 6
# 48 >> 4 = 3, 48 // 2^4 = 3


# 示例4: 负数右移运算
# 测试负数的右移运算
negative_num = -12
print(f"\n负数右移运算:")
for shift in range(1, 4):
    result = negative_num >> shift
    print(f"{negative_num} >> {shift} = {result}")
# -12 >> 1 = -6
# -12 >> 2 = -3
# -12 >> 3 = -2


# 示例5: 右移运算的实际应用
# 用于快速整数除法
def fast_divide_by_power_of_two(x, n):
    return x >> n


# 测试快速除法
test_number = 100
print(f"\n使用右移进行快速除法 (以 {test_number} 为例):")
for i in range(1, 5):
    result = fast_divide_by_power_of_two(test_number, i)
    print(
        f"{test_number} >> {i} = {result}, {test_number} // 2^{i} = {test_number // (2**i)}"
    )

# 100 >> 1 = 50, 100 // 2^1 = 50
# 100 >> 2 = 25, 100 // 2^2 = 25
# 100 >> 3 = 12, 100 // 2^3 = 12
# 100 >> 4 = 6, 100 // 2^4 = 6

"""




"""
# ---------------------------------------------------------------------------
# 1.26-2.1 实际使用1- 权限判断

# 示例1: 权限管理系统
class PermissionManager:
    def __init__(self):
        # rwxrwxrwx
        # r=read； w=write； x=execute

        # 定义权限常量
        self.READ = 1      # 0001    1
        self.WRITE = 2     # 0010    2
        self.EXECUTE = 4   # 0100    4
        self.DELETE = 8    # 1000    8

        # 权限名称映射
        self.permission_names = {
            self.READ: "READ",
            self.WRITE: "WRITE",
            self.EXECUTE: "EXECUTE",
            self.DELETE: "DELETE",
        }

    def add_permission(self, current_permissions, permission):
        # 使用 按位或运算 添加权限
        return current_permissions | permission

    def remove_permission(self, current_permissions, permission):
        # 使用 按位与运算+取反运算  移除权限
        return current_permissions & ~permission

    def has_permission(self, current_permissions, permission):
        # 使用 按位与运算 检查权限
        return (current_permissions & permission) == permission

    def get_permissions(self, current_permissions):
        # 获取所以权限列表
        permissions = []
        for perm, name in self.permission_names.items():
            if self.has_permission(current_permissions, perm):
                permissions.append(name)
        return permissions


# 测试权限管理系统
pm = PermissionManager()

# 初始权限
user_permissions = 0  # 0000

print("权限管理测试:")
print(f"初始权限: {pm.get_permissions(user_permissions)}")

# 添加权限
user_permissions = pm.add_permission(user_permissions, pm.READ)
print(f"添加READ权限后: {pm.get_permissions(user_permissions)}")

user_permissions = pm.add_permission(user_permissions, pm.WRITE)
print(f"添加WRITE权限后: {pm.get_permissions(user_permissions)}")

user_permissions = pm.add_permission(user_permissions, pm.EXECUTE)
print(f"添加EXECUTE权限后: {pm.get_permissions(user_permissions)}")

# 检查权限
print(f"是否有READ权限: {pm.has_permission(user_permissions, pm.READ)}")
print(f"是否有DELETE权限: {pm.has_permission(user_permissions, pm.DELETE)}")

# 移除权限
user_permissions = pm.remove_permission(user_permissions, pm.WRITE)
print(f"移除WRITE权限后: {pm.get_permissions(user_permissions)}")

"""




"""
# ---------------------------------------------------------------------------
# 1.26-2.2 实际使用2- 文件读写模式

# 定义一个文件模式管理类，用于模拟Python的文件打开模式管理
class FileModeManager:
    # 初始化方法，定义各个文件模式的标志位
    def __init__(self):
        # 读模式标志
        self.READ = 1  # 读模式 (0001)
        # 写模式标志
        self.WRITE = 2  # 写模式 (0010)
        # 追加模式标志
        self.APPEND = 4  # 追加模式 (0100)
        # 二进制模式标志
        self.BINARY = 8  # 二进制模式 (1000)
        # 读写模式标志
        self.PLUS = 16  # 读写模式 (10000)
        # 文本模式标志
        self.TEXT = 32  # 文本模式 (100000)

    # 设置某个文件模式标志位
    def set_mode(self, mode, flag):
        # 使用 或运算 添加标志位
        return mode | flag

    # 清除某个文件模式标志位
    def clear_mode(self, mode, flag):
        # 使用 与运算+按位取反 移除标志位
        return mode & ~flag

    # 切换某个文件模式标志位
    def toggle_mode(self, mode, flag):
        # 使用 异或运算 切换标志位
        return mode ^ flag

    # 判断是否包含某个文件模式标志位
    def has_mode(self, mode, flag):
        # 使用 与运算 检测标志位是否存在
        return (mode & flag) != 0

    # 根据当前标志位生成文件打开模式字符串
    def get_mode_string(self, mode):
        # 初始化模式字符串
        mode_str = ""

        # 判断是"r+"模式（读写），优先级最高
        if self.has_mode(mode, self.READ) and self.has_mode(mode, self.WRITE):
            mode_str += "r+"
        # 判断只读模式
        elif self.has_mode(mode, self.READ):
            mode_str += "r"
        # 判断写模式（w 或 a）
        elif self.has_mode(mode, self.WRITE):
            # 如果追加标志也存在，则用"a"
            if self.has_mode(mode, self.APPEND):
                mode_str += "a"
            # 否则为"w"
            else:
                mode_str += "w"
        # 只有追加模式
        elif self.has_mode(mode, self.APPEND):
            mode_str += "a"

        # 判断是否需要加"+"（如r+、w+、a+）
        if self.has_mode(mode, self.PLUS):
            # 如果是"r"，改为"r+"
            if mode_str == "r":
                mode_str = "r+"
            # 如果是"w"，改为"w+"
            elif mode_str == "w":
                mode_str = "w+"
            # 如果是"a"，改为"a+"
            elif mode_str == "a":
                mode_str = "a+"

        # 判断是否为二进制，或文本模式，拼接对应后缀
        if self.has_mode(mode, self.BINARY):
            mode_str += "b"
        elif self.has_mode(mode, self.TEXT):
            mode_str += "t"

        # 若没有任何模式，则返回"无模式"
        return mode_str if mode_str else "无模式"

    # 获取当前模式的中文描述
    def get_mode_description(self, mode):
        # 初始化描述列表
        descriptions = []

        # 检查含有的各类模式，依次加入描述
        if self.has_mode(mode, self.READ):
            descriptions.append("读")
        if self.has_mode(mode, self.WRITE):
            descriptions.append("写")
        if self.has_mode(mode, self.APPEND):
            descriptions.append("追加")
        if self.has_mode(mode, self.BINARY):
            descriptions.append("二进制")
        if self.has_mode(mode, self.PLUS):
            descriptions.append("读写")
        if self.has_mode(mode, self.TEXT):
            descriptions.append("文本")

        # 若描述列表不为空则用+号拼接，否则返回"无模式"
        return " + ".join(descriptions) if descriptions else "无模式"


# 创建FileModeManager对象，用于文件模式操作测试
fm = FileModeManager()
# 初始化模式为0，表示什么都没有
mode = 0  # 初始无模式

# 打印文件读写模式管理测试开始
print(f"\n文件读写模式管理测试:")
# 打印初始模式字符串和描述
print(f"初始模式: {fm.get_mode_string(mode)} ({fm.get_mode_description(mode)})")

# 设置读模式
mode = fm.set_mode(mode, fm.READ)
# 打印设置读模式后的结果
print(f"设置读模式后: {fm.get_mode_string(mode)} ({fm.get_mode_description(mode)})")

# 添加写模式
mode = fm.set_mode(mode, fm.WRITE)
# 打印添加写模式后的结果
print(f"添加写模式后: {fm.get_mode_string(mode)} ({fm.get_mode_description(mode)})")

# 添加二进制模式
mode = fm.set_mode(mode, fm.BINARY)
# 打印添加二进制模式后的结果
print(f"添加二进制模式后: {fm.get_mode_string(mode)} ({fm.get_mode_description(mode)})")

# 清除读模式
mode = fm.clear_mode(mode, fm.READ)
# 打印清除读模式后的结果
print(f"清除读模式后: {fm.get_mode_string(mode)} ({fm.get_mode_description(mode)})")

# 切换追加模式
mode = fm.toggle_mode(mode, fm.APPEND)
# 打印切换追加模式后的结果
print(f"切换追加模式后: {fm.get_mode_string(mode)} ({fm.get_mode_description(mode)})")

# 打印最终的文件模式字符串
print(f"\n最终模式: {fm.get_mode_string(mode)}")
# 打印最终的模式描述
print(f"模式描述: {fm.get_mode_description(mode)}")
# 打印十进制数值
print(f"十进制值: {mode}")

# 开始演示常见的文件模式组合
print(f"\n常见文件模式组合:")
# 定义常见的文件模式组合及其名称
common_modes = {
    "只读": fm.READ,
    "只写": fm.WRITE,
    "追加": fm.WRITE | fm.APPEND,
    "读写": fm.READ | fm.WRITE,
    "只读二进制": fm.READ | fm.BINARY,
    "只写二进制": fm.WRITE | fm.BINARY,
    "追加二进制": fm.WRITE | fm.APPEND | fm.BINARY,
    "读写二进制": fm.READ | fm.WRITE | fm.BINARY,
    "读写追加": fm.READ | fm.WRITE | fm.APPEND,
}
# 遍历每一种常见模式组合，打印名称、模式字符串和描述
for name, mode_val in common_modes.items():
    print(
        f"  {name}: {fm.get_mode_string(mode_val)} ({fm.get_mode_description(mode_val)})"
    )

# 用'r'模式打开test.txt文件，打印文件内容
with open("./test.txt", "r") as file:
    print(file.read())

"""




# ---------------------------------------------------------------------------
# 1.26-2.3 实际使用3- Unicode 字符 → UTF-8 字节


# Unicode 字符 → UTF-8 字节
字符 = "中"
utf8_bytes = 字符.encode("utf-8")
print(utf8_bytes)  # b'\xe4\xb8\xad'
print(utf8_bytes.hex())  # 'e4b8ad'

# UTF-8 字节 → Unicode 字符
原字符 = utf8_bytes.decode("utf-8")
print(原字符)  # '中'

# 获取 Unicode 码点
码点 = ord("中")
print(f"U+{码点:04X}")  # U+4E2D
print(码点)  # 20013

# 从码点创建字符
字符 = chr(0x4E2D)
print(字符)  # '中'



# 定义函数，将Unicode码点转为UTF-8字节序列
def unicode_to_utf8(codepoint):
    """
    将 Unicode 码点转换为 UTF-8 字节序列
    参数：
        codepoint: Unicode 码点（整数）
    返回：
        bytes: UTF-8 编码的字节序列

    """
    # 检查码点是否在有效范围内
    if codepoint < 0 or codepoint > 0x10FFFF:
        raise ValueError(f"无效的 Unicode 码点: {codepoint}")

    # 如果码点小于等于0x7F，用1字节表示（ASCII）
    if codepoint <= 0x7F:
        # 构造单字节
        return bytes([codepoint])

    # 如果码点小于等于0x7FF，用2字节表示
    elif codepoint <= 0x7FF:
        # 构造第1字节（110xxxxx）
        byte1 = 0b11000000 | (codepoint >> 6)
        # 构造第2字节（10xxxxxx）
        byte2 = 0b10000000 | (codepoint & 0b00111111)
        # 返回组合后的2字节
        return bytes([byte1, byte2])

    # 如果码点小于等于0xFFFF，用3字节表示
    elif codepoint <= 0xFFFF:
        # 构造第1字节（1110xxxx）
        byte1 = 0b11100000 | (codepoint >> 12)
        # 构造第2字节（10xxxxxx）
        byte2 = 0b10000000 | ((codepoint >> 6) & 0b00111111)
        # 构造第3字节（10xxxxxx）
        byte3 = 0b10000000 | (codepoint & 0b00111111)
        # 返回组合后的3字节
        return bytes([byte1, byte2, byte3])

    # 其它情况，用4字节表示
    else:
        # 构造第1字节（11110xxx）
        byte1 = 0b11110000 | (codepoint >> 18)
        # 构造第2字节（10xxxxxx）
        byte2 = 0b10000000 | ((codepoint >> 12) & 0b00111111)
        # 构造第3字节（10xxxxxx）
        byte3 = 0b10000000 | ((codepoint >> 6) & 0b00111111)
        # 构造第4字节（10xxxxxx）
        byte4 = 0b10000000 | (codepoint & 0b00111111)
        # 返回组合后的4字节
        return bytes([byte1, byte2, byte3, byte4])


# 定义函数，将UTF-8字节序列转换为Unicode码点
def utf8_to_unicode(utf8_bytes):
    """
    将 UTF-8 字节序列转换为 Unicode 码点（反向转换）
    参数：utf8_bytes: UTF-8 编码的字节序列
    返回：int: Unicode 码点
    """
    # 检查输入是否为空
    if not utf8_bytes:
        raise ValueError("空字节序列")

    # 获取首字节
    first_byte = utf8_bytes[0]

    # 1字节编码情况：0xxxxxxx
    if (first_byte & 0b10000000) == 0:
        return first_byte

    # 2字节编码情况：110xxxxx 10xxxxxx
    elif (first_byte & 0b11100000) == 0b11000000:
        # 检查字节长度是否充足
        if len(utf8_bytes) < 2:
            raise ValueError("不完整的 UTF-8 序列")
        # 取高5位+低6位，拼出码点
        codepoint = ((first_byte & 0b00011111) << 6) | (utf8_bytes[1] & 0b00111111)
        return codepoint

    # 3字节编码情况：1110xxxx 10xxxxxx 10xxxxxx
    elif (first_byte & 0b11110000) == 0b11100000:
        # 检查字节长度是否充足
        if len(utf8_bytes) < 3:
            raise ValueError("不完整的 UTF-8 序列")
        # 拼接高4位、中间6位和低6位得码点
        codepoint = (
            ((first_byte & 0b00001111) << 12)
            | ((utf8_bytes[1] & 0b00111111) << 6)
            | (utf8_bytes[2] & 0b00111111)
        )
        return codepoint

    # 4字节编码情况：11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
    elif (first_byte & 0b11111000) == 0b11110000:
        # 检查字节长度是否充足
        if len(utf8_bytes) < 4:
            raise ValueError("不完整的 UTF-8 序列")
        # 拼接高3位、次高6位、次低6位和低6位得码点
        codepoint = (
            ((first_byte & 0b00000111) << 18)
            | ((utf8_bytes[1] & 0b00111111) << 12)
            | ((utf8_bytes[2] & 0b00111111) << 6)
            | (utf8_bytes[3] & 0b00111111)
        )
        return codepoint

    # 非法的UTF-8首字节
    else:
        raise ValueError("无效的 UTF-8 首字节")


# 测试代码：定义要测试的字符列表
test_chars = ["A", "中", "😀"]
# 遍历每个字符
for char in test_chars:
    # 取出字符对应的Unicode码点
    codepoint = ord(char)

    # 手动将码点转为UTF-8字节序列
    utf8_manual = unicode_to_utf8(codepoint)

    # 用Python内置方法编码
    utf8_builtin = char.encode("utf-8")

    # 打印字符及转码信息
    print(f"\n字符: '{char}'")
    print(f"  Unicode码点: U+{codepoint:04X} ({codepoint})")
    print(f"  UTF-8字节: {utf8_manual.hex().upper()}")
    print(f"  字节数: {len(utf8_manual)}")
    print(f"  验证: {'正确' if utf8_manual == utf8_builtin else '错误'}")

    # 用自定义方法解码回码点
    decoded = utf8_to_unicode(utf8_manual)
    # 再转回字符
    decoded_char = chr(decoded)
    print(f"  反向解码: '{decoded_char}' (U+{decoded:04X})")

