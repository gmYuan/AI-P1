"""

# 导入 cProfile 模块，用于性能分析
import cProfile

# 导入 re 模块，用于正则表达式操作
import re

# 导入 random 模块，用于生成随机数
import random


def fibonacci(n):
    # 定义一个函数，用于计算斐波那契数列的第n项
    # n 是要计算的项数
    if n <= 1:
        # 如果n小于等于1
        return n
        # 返回n
    else:
        # 如果n大于1
        return fibonacci(n - 1) + fibonacci(n - 2)
        # 递归计算前两项的和


def process_data(data):
    # 定义一个函数，用于处理数据
    # data 是要处理的数据列表
    result = []
    # 初始化结果列表
    for item in data:
        # 遍历数据列表
        if isinstance(item, str):
            # 如果项是字符串
            # 使用正则表达式匹配数字
            if re.match(r"\d+", item):
                # 如果匹配到数字
                result.append(int(item))
                # 将字符串转换为整数并添加到结果列表
            else:
                # 如果没有匹配到数字
                result.append(len(item))
                # 将字符串长度添加到结果列表
        else:
            # 如果项不是字符串
            result.append(item * 2)
            # 将项乘以2并添加到结果列表
    return result
    # 返回结果列表


def main():
    # 定义一个主函数，用于演示性能分析
    # 生成测试数据
    test_data = [str(random.randint(1, 100)) for _ in range(100)]
    # 创建包含100个随机数字字符串的列表

    # 处理数据
    processed_data = process_data(test_data)
    # 调用process_data函数处理测试数据

    # 计算斐波那契数列
    fib_result = fibonacci(20)
    # 计算第20项斐波那契数

    print(f"处理后的数据: {processed_data[:5]}...")
    # 打印处理后的数据（前5个）
    print(f"斐波那契数列第20项: {fib_result}")
    # 打印斐波那契数列第20项


# 使用 cProfile 分析 main 函数的性能
# cProfile.run() 会执行传入的字符串作为代码，并打印详细的性能报告
cProfile.run("main()")

# 也可以将性能分析结果保存到文件
# cProfile.run('main()', 'profile_output.prof')
# 这行代码会将性能分析结果保存到 profile_output.prof 文件中






# 导入time模块，用于时间测量
import time

# 导入random模块，用于生成随机数
import random


# 定义函数：冒泡排序算法
def bubble_sort(arr):
    # 获取数组长度
    n = len(arr)
    # 外层循环遍历数组每一个元素
    for i in range(n):
        # 内层循环，直到排好剩余未排序部分
        for j in range(0, n - i - 1):
            # 如果当前位置元素大于下一个元素，交换它们
            if arr[j] > arr[j + 1]:
                # 交换两个元素的位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # 返回排序后的数组
    return arr


# 定义函数：快速排序算法
def quick_sort(arr):
    # 如果数组长度小于等于1，则直接返回数组
    if len(arr) <= 1:
        return arr
    else:
        # 选择中间元素作为基准
        pivot = arr[len(arr) // 2]
        # 所有小于基准的元素
        left = [x for x in arr if x < pivot]
        # 所有等于基准的元素
        middle = [x for x in arr if x == pivot]
        # 所有大于基准的元素
        right = [x for x in arr if x > pivot]
        # 递归地对左边和右边进行排序，并合并最后结果
        return quick_sort(left) + middle + quick_sort(right)


# 定义函数：用于测量两种排序算法的性能
def measure_sorting_performance():
    # 生成包含1000个随机整数的测试数据
    test_data = [random.randint(1, 1000) for _ in range(1000)]

    # 测试冒泡排序性能
    data_copy = test_data.copy()
    # 记录开始时间
    start_time = time.time()
    # 对数据进行冒泡排序
    bubble_sort(data_copy)
    # 记录结束时间
    end_time = time.time()
    # 计算冒泡排序执行时间
    bubble_time = end_time - start_time
    # 输出冒泡排序的用时
    print(f"冒泡排序执行时间: {bubble_time:.4f}秒")

    # 测试快速排序性能
    data_copy = test_data.copy()
    # 记录开始时间
    start_time = time.time()
    # 对数据进行快速排序
    quick_sort(data_copy)
    # 记录结束时间
    end_time = time.time()
    # 计算快速排序执行时间
    quick_time = end_time - start_time
    # 输出快速排序的用时
    print(f"快速排序执行时间: {quick_time:.4f}秒")

    # 计算快速排序相对于冒泡排序的性能提升
    if bubble_time > 0:
        # 计算性能提升的倍率
        improvement = bubble_time / quick_time
        # 输出性能提升结果
        print(f"快速排序比冒泡排序快 {improvement:.2f} 倍")


# 定义装饰器：用于测量函数执行时间
def timing_decorator(func):
    # 定义包装函数
    def wrapper(*args, **kwargs):
        # 记录函数开始时间
        start_time = time.time()
        # 执行被装饰的函数
        result = func(*args, **kwargs)
        # 记录函数结束时间
        end_time = time.time()
        # 计算执行时长
        execution_time = end_time - start_time
        # 输出函数执行时间信息
        print(f"{func.__name__} 执行时间: {execution_time:.4f}秒")
        # 返回原函数运行结果
        return result

    # 返回包装后的函数
    return wrapper


# 使用上面定义的timing_decorator来装饰expensive_operation函数
@timing_decorator
def expensive_operation():
    # 初始化返回结果
    result = 0
    # 累加从0到999999的每个数的平方
    for i in range(1000000):
        result += i**2
    # 返回累加的结果
    return result


# 如果当前文件作为主程序执行，则运行以下代码
if __name__ == "__main__":
    # 调用函数，测试排序性能
    measure_sorting_performance()
    # 执行耗时操作并输出其耗时
    expensive_operation()


# 安装 line_profiler 工具
# pip install line_profiler
# 实际运行前，需要使用 kernprof -l your_script.py 命令
# 导入 line_profiler 模块的 profile 装饰器
from line_profiler import profile

# 导入 random 模块用于生成随机数
import random


# 使用 @profile 装饰器以便逐行分析该函数
@profile
# 定义一个数据处理函数
def data_processing_function():
    # 生成包含10000个随机整数的列表，每个随机数在1到100之间
    data = [random.randint(1, 100) for _ in range(10000)]

    # 初始化一个空列表用于存放过滤后数据
    filtered_data = []
    # 遍历原始数据列表
    for item in data:
        # 当该数据大于50时
        if item > 50:
            # 将其添加到过滤后数据列表中
            filtered_data.append(item)

    # 初始化一个空列表用于存放转换后数据
    transformed_data = []
    # 遍历过滤后的数据列表
    for item in filtered_data:
        # 将每个数据乘以2后添加到转换后数据列表
        transformed_data.append(item * 2)

    # 初始化总和变量
    total = 0
    # 遍历转换后数据列表
    for item in transformed_data:
        # 将每项加到总和上
        total += item

    # 返回处理得到的总和
    return total


# 使用 @profile 装饰器分析优化版本函数
@profile
# 定义一个优化版的数据处理函数
def optimized_data_processing_function():
    # 生成包含10000个随机整数的列表，每个随机数在1到100之间
    data = [random.randint(1, 100) for _ in range(10000)]

    # 使用列表推导式同时过滤和转换数据：选择大于50的项，乘2后添加到列表
    filtered_and_transformed = [item * 2 for item in data if item > 50]

    # 使用内置 sum 函数对列表所有项求和
    total = sum(filtered_and_transformed)

    # 返回处理得到的总和
    return total


# 判断是否作为主程序运行
if __name__ == "__main__":
    # 打印运行原始版本的提示信息
    print("运行原始版本:")
    # 调用原始数据处理函数并获得结果
    result1 = data_processing_function()
    # 打印原始版本的结果
    print(f"结果: {result1}")

    # 打印运行优化版本的提示信息
    print("\n运行优化版本:")
    # 调用优化后的数据处理函数并获得结果
    result2 = optimized_data_processing_function()
    # 打印优化版本的结果
    print(f"结果: {result2}")


# 注意：在实际运行前，需要通过 python -m memory_profiler your_script.py 命令来执行
# 导入 memory_profiler 模块中的 profile 装饰器
from memory_profiler import profile

# 导入 random 模块，用于生成随机数
import random


@profile
# 使用 @profile 装饰器标记函数
# 这表示 memory_profiler 将会逐行分析此函数的内存使用情况
def memory_intensive_function():
    # 定义一个内存密集型函数
    # 创建大列表
    large_list = []
    # 初始化大列表
    for i in range(100000):
        # 遍历100000次
        large_list.append(i)
        # 将i添加到列表中

    # 创建大字典
    large_dict = {}
    # 初始化大字典
    for i in range(100000):
        # 遍历100000次
        large_dict[i] = i * 2
        # 将i和i*2作为键值对添加到字典中

    # 创建大字符串
    large_string = ""
    # 初始化大字符串
    for i in range(10000):
        # 遍历10000次
        large_string += str(i)
        # 将i转换为字符串并拼接到大字符串中

    # 计算总和
    total = sum(large_list)
    # 计算大列表中所有元素的和

    return total
    # 返回总和


@profile
# 使用 @profile 装饰器标记函数
def memory_optimized_function():
    # 定义一个内存优化函数
    # 使用生成器表达式而不是列表
    large_generator = (i for i in range(100000))
    # 创建生成器表达式

    # 使用字典推导式
    large_dict = {i: i * 2 for i in range(100000)}
    # 使用字典推导式创建字典

    # 使用join方法而不是字符串拼接
    large_string = "".join(str(i) for i in range(10000))
    # 使用join方法创建大字符串

    # 计算总和
    total = sum(large_generator)
    # 计算生成器中所有元素的和

    return total
    # 返回总和


@profile
# 使用 @profile 装饰器标记函数
def list_vs_generator_comparison():
    # 定义一个函数，用于比较列表和生成器的内存使用
    # 使用列表
    list_data = [i**2 for i in range(100000)]
    # 创建包含100000个平方数的列表
    list_sum = sum(list_data)
    # 计算列表中所有元素的和

    # 使用生成器
    generator_data = (i**2 for i in range(100000))
    # 创建包含100000个平方数的生成器
    generator_sum = sum(generator_data)
    # 计算生成器中所有元素的和

    return list_sum, generator_sum
    # 返回两个和


# 当脚本作为主程序运行时，调用被装饰的函数
if __name__ == "__main__":
    # 如果当前模块是主模块
    print("运行内存密集型函数:")
    # 打印运行内存密集型函数信息
    result1 = memory_intensive_function()
    # 调用内存密集型函数
    print(f"结果: {result1}")
    # 打印结果

    print("\n运行内存优化函数:")
    # 打印运行内存优化函数信息
    result2 = memory_optimized_function()
    # 调用内存优化函数
    print(f"结果: {result2}")
    # 打印结果

    print("\n运行列表vs生成器比较:")
    # 打印运行列表vs生成器比较信息
    result3 = list_vs_generator_comparison()
    # 调用列表vs生成器比较函数
    print(f"结果: {result3}")
    # 打印结果


# 导入time模块，用于时间测量
import time

# 导入random模块，用于生成随机数
import random

# 导入numpy模块，用于数值计算
import numpy as np

# 导入pandas模块，用于数据分析
import pandas as pd


# 定义纯Python矩阵乘法函数
def pure_python_matrix_multiply(A, B):
    # 计算矩阵A的行数
    rows_A = len(A)
    # 计算矩阵A的列数
    cols_A = len(A[0])
    # 计算矩阵B的列数
    cols_B = len(B[0])
    # 创建结果矩阵C，初始值为0
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    # 遍历矩阵A的每一行
    for i in range(rows_A):
        # 遍历矩阵B的每一列
        for j in range(cols_B):
            # 遍历A的每一列
            for k in range(cols_A):
                # 累加A[i][k]与B[k][j]的乘积到C[i][j]
                C[i][j] += A[i][k] * B[k][j]
    # 返回结果矩阵C
    return C


# 定义NumPy版本的矩阵乘法函数
def numpy_matrix_multiply(A, B):
    # 使用NumPy的dot函数进行矩阵乘法
    return np.dot(A, B)


# 定义纯Python数据处理函数
def pure_python_data_processing(data):
    # 创建结果列表
    result = []
    # 遍历数据中的每一项
    for item in data:
        # 判断item是否大于50
        if item > 50:
            # 如果大于50，将其乘2后加入结果列表
            result.append(item * 2)
    # 返回结果列表
    return result


# 定义Pandas数据处理函数
def pandas_data_processing(data):
    # 用data创建一个DataFrame对象
    df = pd.DataFrame({"values": data})
    # 过滤出大于50的行
    filtered_df = df[df["values"] > 50]
    # 将筛选出的值乘以2
    filtered_df["values"] = filtered_df["values"] * 2
    # 转换为Python列表并返回
    return filtered_df["values"].tolist()


# 定义性能对比函数
def performance_comparison():
    # 打印矩阵乘法性能比较标题
    print("--- 矩阵乘法性能比较 ---")
    # 设置测试矩阵的大小
    size = 100
    # 随机生成Python列表格式的矩阵A
    A_python = [[random.random() for _ in range(size)] for _ in range(size)]
    # 随机生成Python列表格式的矩阵B
    B_python = [[random.random() for _ in range(size)] for _ in range(size)]
    # 将A_python转为NumPy数组
    A_numpy = np.array(A_python)
    # 将B_python转为NumPy数组
    B_numpy = np.array(B_python)
    # 测试纯Python矩阵乘法所用时间
    start_time = time.time()
    result_python = pure_python_matrix_multiply(A_python, B_python)
    end_time = time.time()
    python_time = end_time - start_time
    # 打印纯Python执行时间
    print(f"纯Python版本执行时间: {python_time:.4f}秒")
    # 测试NumPy矩阵乘法所用时间
    start_time = time.time()
    result_numpy = numpy_matrix_multiply(A_numpy, B_numpy)
    end_time = time.time()
    numpy_time = end_time - start_time
    # 打印NumPy执行时间
    print(f"NumPy版本执行时间: {numpy_time:.4f}秒")
    # 计算NumPy相对纯Python的加速比
    if python_time > 0:
        improvement = python_time / numpy_time
        # 打印性能提升比例
        print(f"NumPy比纯Python快 {improvement:.2f} 倍")
    # 打印数据处理性能比较标题
    print("\n--- 数据处理性能比较 ---")
    # 生成包含100000个1-100之间随机整数的测试数据
    test_data = [random.randint(1, 100) for _ in range(100000)]
    # 测试纯Python数据处理所用时间
    start_time = time.time()
    result_python = pure_python_data_processing(test_data)
    end_time = time.time()
    python_time = end_time - start_time
    # 打印纯Python执行时间
    print(f"纯Python版本执行时间: {python_time:.4f}秒")
    # 测试Pandas数据处理所用时间
    start_time = time.time()
    result_pandas = pandas_data_processing(test_data)
    end_time = time.time()
    pandas_time = end_time - start_time
    # 打印Pandas执行时间
    print(f"Pandas版本执行时间: {pandas_time:.4f}秒")
    # 计算Pandas相对纯Python的加速比
    if python_time > 0:
        improvement = python_time / pandas_time
        # 打印性能提升比例
        print(f"Pandas比纯Python快 {improvement:.2f} 倍")


# 判断是否作为主模块运行
if __name__ == "__main__":
    # 调用性能比较函数
    performance_comparison()

"""

# 导入 time 模块，用于时间测量
import time

# 导入 random 模块，用于生成随机数
import random

# 导入 collections 模块，用于双端队列
from collections import deque


# 定义一个低效的线性搜索函数
def inefficient_search(data, target):
    # 遍历数据中的每个元素及其索引
    for i, item in enumerate(data):
        # 判断当前元素是否等于目标值
        if item == target:
            # 找到目标值时返回索引
            return i
    # 未找到目标值时返回 -1
    return -1


# 定义一个高效的二分查找函数
def efficient_search(data, target):
    # 初始化查找的左边界和右边界
    left, right = 0, len(data) - 1
    # 当左边界不大于右边界时循环
    while left <= right:
        # 计算中间元素的索引
        mid = (left + right) // 2
        # 判断中间元素是否等于目标值
        if data[mid] == target:
            # 找到目标值时返回索引
            return mid
        # 如果中间元素小于目标值，则缩小查找区间到右半部分
        elif data[mid] < target:
            left = mid + 1
        # 如果中间元素大于目标值，则缩小查找区间到左半部分
        else:
            right = mid - 1
    # 未找到目标值时返回 -1
    return -1


# 定义一个低效的列表操作函数
def inefficient_list_operations():
    # 初始化一个空列表 data
    data = []
    # 向列表头部插入 1000 个元素
    for i in range(1000):
        data.insert(0, i)
    # 逐步从列表头部弹出所有元素
    while data:
        data.pop(0)
    # 返回当前列表长度
    return len(data)


# 定义一个高效的双端队列操作函数
def efficient_deque_operations():
    # 初始化一个空的双端队列 data
    data = deque()
    # 向双端队列左侧插入 1000 个元素
    for i in range(1000):
        data.appendleft(i)
    # 逐步从双端队列左侧弹出所有元素
    while data:
        data.popleft()
    # 返回当前双端队列长度
    return len(data)


# 定义一个低效的字符串拼接函数
def inefficient_string_concatenation():
    # 初始化一个空字符串 result
    result = ""
    # 拼接 10000 次字符串
    for i in range(10000):
        result += str(i)
    # 返回拼接后字符串的长度
    return len(result)


# 定义一个高效的字符串拼接函数
def efficient_string_concatenation():
    # 初始化一个空列表 result
    result = []
    # 将 10000 个字符串添加到列表
    for i in range(10000):
        result.append(str(i))
    # 使用 join 拼接列表中的所有字符串并返回长度
    return len("".join(result))


# 定义一个算法性能测试函数
def algorithm_performance_test():
    # 打印搜索算法性能比较标题
    print("--- 搜索算法性能比较 ---")
    # 初始化随机的测试数据，升序排列
    data = sorted([random.randint(1, 100000) for _ in range(100000)])
    # 随机挑选一个目标元素
    target = random.choice(data)
    # 记录线性搜索的开始时间
    start_time = time.time()
    # 执行线性搜索
    result1 = inefficient_search(data, target)
    # 记录结束时间
    end_time = time.time()
    # 计算线性搜索所用时间
    linear_time = end_time - start_time
    # 打印线性搜索的用时
    print(f"线性搜索执行时间: {linear_time:.4f}秒")
    # 记录二分搜索的开始时间
    start_time = time.time()
    # 执行二分搜索
    result2 = efficient_search(data, target)
    # 记录结束时间
    end_time = time.time()
    # 计算二分搜索所用时间
    binary_time = end_time - start_time
    # 打印二分搜索的用时
    print(f"二分搜索执行时间: {binary_time:.4f}秒")
    # 如果二分搜索用时大于0，计算提升倍数
    if binary_time > 0:
        improvement = linear_time / binary_time
        # 打印二分搜索相较线性搜索的提升倍数
        print(f"二分搜索比线性搜索快 {improvement:.2f} 倍")
    # 打印数据结构性能比较标题
    print("\n--- 数据结构性能比较 ---")
    # 记录列表操作的开始时间
    start_time = time.time()
    # 执行低效的列表操作
    result1 = inefficient_list_operations()
    # 记录结束时间
    end_time = time.time()
    # 计算列表操作所用时间
    list_time = end_time - start_time
    # 打印低效列表操作的用时
    print(f"列表操作执行时间: {list_time:.4f}秒")
    # 记录双端队列操作的开始时间
    start_time = time.time()
    # 执行高效的双端队列操作
    result2 = efficient_deque_operations()
    # 记录结束时间
    end_time = time.time()
    # 计算双端队列操作所用时间
    deque_time = end_time - start_time
    # 打印高效双端队列操作的用时
    print(f"双端队列操作执行时间: {deque_time:.4f}秒")
    # 如果高效操作用时大于0，计算性能提升倍数
    if deque_time > 0:
        improvement = list_time / deque_time
        # 打印高效双端队列相较低效列表的提升倍数
        print(f"双端队列比列表快 {improvement:.2f} 倍")
    # 打印字符串拼接性能比较标题
    print("\n--- 字符串拼接性能比较 ---")
    # 记录低效字符串拼接的开始时间
    start_time = time.time()
    # 执行低效字符串拼接
    result1 = inefficient_string_concatenation()
    # 记录结束时间
    end_time = time.time()
    # 计算低效字符串拼接用时
    inefficient_time = end_time - start_time
    # 打印低效字符串拼接的用时
    print(f"低效字符串拼接执行时间: {inefficient_time:.4f}秒")
    # 记录高效字符串拼接的开始时间
    start_time = time.time()
    # 执行高效字符串拼接
    result2 = efficient_string_concatenation()
    # 记录结束时间
    end_time = time.time()
    # 计算高效字符串拼接的用时
    efficient_time = end_time - start_time
    # 打印高效字符串拼接的用时
    print(f"高效字符串拼接执行时间: {efficient_time:.4f}秒")
    # 如果高效字符串拼接用时大于 0，计算提升倍数
    if efficient_time > 0:
        improvement = inefficient_time / efficient_time
        # 打印高效字符串拼接相较低效方法的提升倍数
        print(f"高效字符串拼接比低效方法快 {improvement:.2f} 倍")


# 判断当前是否为主模块
if __name__ == "__main__":
    # 运行算法性能测试函数
    algorithm_performance_test()
