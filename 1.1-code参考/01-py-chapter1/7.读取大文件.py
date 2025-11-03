"""
# 导入 os 模块，用于文件操作
import os

# 导入 time 模块，用于时间测量
import time


def process_line(line):
    # 定义一个函数，用于处理每一行数据
    # line 是要处理的行数据
    return line.strip().upper()
    # 去除行首尾空白字符并转换为大写


def read_file_line_by_line(filename):
    # 定义一个函数，用于逐行读取文件
    # filename 是要读取的文件名
    processed_lines = []
    # 初始化处理后的行列表
    line_count = 0
    # 初始化行计数器

    with open(filename, "r", encoding="utf-8") as file:
        # 打开文件进行读取
        for line in file:
            # 遍历文件的每一行
            processed_line = process_line(line)
            # 处理当前行
            processed_lines.append(processed_line)
            # 将处理后的行添加到列表
            line_count += 1
            # 行计数器递增

            # 每处理1000行打印一次进度
            if line_count % 1000 == 0:
                # 如果行数是1000的倍数
                print(f"已处理 {line_count} 行")
                # 打印处理进度

    return processed_lines, line_count
    # 返回处理后的行列表和总行数


def read_file_line_by_line_generator(filename):
    # 定义一个生成器函数，用于逐行读取文件（内存优化版本）
    # filename 是要读取的文件名
    with open(filename, "r", encoding="utf-8") as file:
        # 打开文件进行读取
        for line in file:
            # 遍历文件的每一行
            yield process_line(line)
            # 生成处理后的行


def create_large_test_file(filename, size_mb=10):
    # 定义一个函数，用于创建大型测试文件
    # filename 是要创建的文件名
    # size_mb 是文件大小（MB）
    print(f"正在创建 {size_mb}MB 的测试文件...")
    # 打印创建文件信息

    with open(filename, "w", encoding="utf-8") as file:
        # 打开文件进行写入
        for i in range(size_mb * 1024 * 10):  # 假设每行约100字节
            # 循环写入数据
            file.write(f"这是第 {i} 行数据，包含一些测试内容用于演示大文件读取\n")
            # 写入测试数据

    print(f"测试文件 {filename} 创建完成")
    # 打印文件创建完成信息


# 创建测试文件
test_filename = "large_test_file.txt"
# 设置测试文件名
create_large_test_file(test_filename, 5)
# 创建5MB的测试文件

# 测试逐行读取
print("\n--- 逐行读取测试 ---")
# 打印逐行读取测试标题
start_time = time.time()
# 记录开始时间
processed_data, total_lines = read_file_line_by_line(test_filename)
# 逐行读取文件
end_time = time.time()
# 记录结束时间
print(f"逐行读取完成，共处理 {total_lines} 行，耗时 {end_time - start_time:.2f} 秒")
# 打印处理结果

# 测试生成器版本（内存优化）
print("\n--- 生成器版本测试 ---")
# 打印生成器版本测试标题
start_time = time.time()
# 记录开始时间
line_count = 0
# 初始化行计数器
for processed_line in read_file_line_by_line_generator(test_filename):
    # 遍历生成器
    line_count += 1
    # 行计数器递增
    if line_count % 1000 == 0:
        # 如果行数是1000的倍数
        print(f"已处理 {line_count} 行")
        # 打印处理进度
end_time = time.time()
# 记录结束时间
print(f"生成器版本完成，共处理 {line_count} 行，耗时 {end_time - start_time:.2f} 秒")
# 打印处理结果

# 清理测试文件
# os.remove(test_filename)
# 删除测试文件
print(f"测试文件 {test_filename} 已删除")
# 打印文件删除信息
"""

# 导入os模块，用于文件操作
import os

# 导入hashlib模块，用于计算哈希值
import hashlib


# 定义生成器函数，实现文件分块读取
def read_in_chunks(file_object, chunk_size=1024):
    # 无限循环持续读取
    while True:
        # 读取指定大小的数据块
        data = file_object.read(chunk_size)
        # 如果数据读取完毕，跳出循环
        if not data:
            break
        # 通过yield返回当前数据块
        yield data


# 处理单个数据块
def process_chunk(chunk):
    # 返回数据块长度
    return len(chunk)


# 计算文件的MD5哈希值，默认按8192字节分块
def calculate_file_hash(filename, chunk_size=8192):
    # 创建MD5哈希对象
    hash_md5 = hashlib.md5()
    # 以二进制读模式打开文件
    with open(filename, "rb") as file:
        # 按指定分块大小循环读取
        for chunk in read_in_chunks(file, chunk_size):
            # 用读到的块更新哈希值 计算文件哈希值时，通过分块读取并增量更新的方式
            hash_md5.update(chunk)
    # 返回哈希值的十六进制字符串形式
    return hash_md5.hexdigest()


# 复制大文件，支持分块读写
def copy_large_file(source, destination, chunk_size=8192):
    # 以二进制读模式打开源文件
    with open(source, "rb") as src_file:
        # 以二进制写模式打开目标文件
        with open(destination, "wb") as dst_file:
            # 循环读取源文件
            for chunk in read_in_chunks(src_file, chunk_size):
                # 写入目标文件
                dst_file.write(chunk)


# 创建指定大小（MB）的二进制测试文件
def create_large_binary_file(filename, size_mb=10):
    # 输出创建文件提示信息
    print(f"正在创建 {size_mb}MB 的二进制测试文件...")
    # 以二进制写模式打开文件
    with open(filename, "wb") as file:
        # 设置块大小为1024字节
        chunk_size = 1024
        # 根据文件大小计算要写入的块数
        total_chunks = (size_mb * 1024 * 1024) // chunk_size
        # 遍历所有块
        for i in range(total_chunks):
            # 构造内容为重复字节的数据块
            data = bytes([i % 256] * chunk_size)
            # 写入当前块到文件
            file.write(data)
    # 输出创建完成信息
    print(f"二进制测试文件 {filename} 创建完成")


# 定义测试文件名
test_filename = "large_binary_file.dat"
# 创建5MB测试文件
create_large_binary_file(test_filename, 5)

# 输出分块读取测试标题
print("\n--- 分块读取测试 ---")
# 总字节数初始化为0
total_bytes = 0
# 块计数初始化为0
chunk_count = 0

# 以二进制读模式打开测试文件
with open(test_filename, "rb") as file:
    # 用8K分块循环读取
    for chunk in read_in_chunks(file, 1024 * 8):
        # 累加本块长度到总字节数
        total_bytes += len(chunk)
        # 块计数加1
        chunk_count += 1
        # 可选处理数据块（这里只调用长度）
        process_chunk(chunk)

# 输出最终处理结果统计
print(f"分块读取完成，共处理 {chunk_count} 个块，{total_bytes} 字节")

# 输出哈希计算测试标题
print("\n--- 文件哈希计算测试 ---")
# 计算测试文件MD5值
file_hash = calculate_file_hash(test_filename)
# 输出文件哈希值
print(f"文件哈希值: {file_hash}")

# 输出文件复制测试标题
print("\n--- 文件复制测试 ---")
# 定义复制文件名
copy_filename = "copy_of_large_file.dat"
# 调用大文件复制函数
copy_large_file(test_filename, copy_filename)
# 输出复制完成信息
print("文件复制完成")

# 计算原文件哈希
original_hash = calculate_file_hash(test_filename)
# 计算复制文件哈希
copy_hash = calculate_file_hash(copy_filename)
# 输出原文件哈希
print(f"原文件哈希: {original_hash}")
# 输出复制文件哈希
print(f"复制文件哈希: {copy_hash}")
# 比较哈希验证复制正确与否
print(f"文件复制验证: {'成功' if original_hash == copy_hash else '失败'}")

# 删除原测试文件
# os.remove(test_filename)
# 删除复制文件
# os.remove(copy_filename)
# 输出清理提示
print("测试文件已清理")
