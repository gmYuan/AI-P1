"""
# range(5) [0,1,2,3,4]
# 定义一个包含整数的列表
my_list = [10, 20, 30, 40, 50]

# 使用正索引访问元素
# 访问第一个元素（索引0）
print("第一个元素（正索引0）:", my_list[0])
# 访问最后一个元素（正索引4）
print("最后一个元素（正索引4）:", my_list[4])

# 使用负索引访问元素
# 使用负索引-1访问列表的最后一个元素
print("最后一个元素（负索引-1）:", my_list[-1])
# 使用负索引-2访问列表的倒数第二个元素
print("倒数第二个元素（负索引-2）:", my_list[-2])
# 使用负索引-3访问列表的倒数第三个元素
print("倒数第三个元素（负索引-3）:", my_list[-3])

# 比较正索引和负索引的对应关系
print("\n正索引与负索引的对应关系:")
# 遍历列表并显示正索引和负索引的对应关系
for i in range(len(my_list)):
    # 计算对应的负索引
    negative_index = i - len(my_list)
    # 打印正索引、负索引和对应的值
    print(f"正索引 {i} = 负索引 {negative_index} = 值 {my_list[i]}")


# 负索引在元组中的使用
# 定义一个包含整数的元组
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 使用负索引访问元组元素
# 访问元组的最后一个元素
print("元组最后一个元素:", my_tuple[-1])
# 访问元组的倒数第二个元素
print("元组倒数第二个元素:", my_tuple[-2])
# 访问元组的倒数第三个元素
print("元组倒数第三个元素:", my_tuple[-3])

# 负索引在字符串中的使用
# 定义一个字符串
my_string = "Hello, Python World!"

# 使用负索引访问字符串中的字符
# 访问字符串的最后一个字符
print("字符串最后一个字符:", my_string[-1])
# 访问字符串的倒数第二个字符
print("字符串倒数第二个字符:", my_string[-2])
# 访问字符串的倒数第六个字符
print("字符串倒数第六个字符:", my_string[-6])


# 负索引在字节串中的使用
# Non-ASCII character not allowed in bytes string literal
# ASCII编码里 字符集也是编码集
# 定义一个字节串 中
my_bytes = b"Python Programming"

# 使用负索引访问字节串中的字节
# 访问字节串的最后一个字节
print("字节串最后一个字节:", my_bytes[-1])  # 103
# 访问字节串的倒数第二个字节
print("字节串倒数第二个字节:", my_bytes[-2])  # 110
# __or__ 和 __ror__都是 类内置的魔术方法吗？是的
# 这个字节串 中
str = b"abc123\xe4\xb8\xad"


# 定义一个列表用于演示
data = ["A", "B", "C", "D", "E", "F", "G"]

print("=== 正负索引对比演示 ===")
print(f"列表内容: {data}")
print(f"列表长度: {len(data)}")

# 使用正索引访问
print("\n使用正索引访问:")
# 遍历所有正索引
for i in range(len(data)):
    # 打印正索引和对应的值
    print(f"data[{i}] = '{data[i]}'")

# 使用负索引访问
print("\n使用负索引访问:")
# 遍历所有负索引
for i in range(-1, -len(data) - 1, -1):
    # 打印负索引和对应的值
    print(f"data[{i}] = '{data[i]}'")

# 正负索引的对应关系
print("\n正负索引对应关系:")
# 遍历列表并显示对应关系
for i in range(len(data)):
    # 计算对应的负索引
    neg_i = i - len(data)
    # 打印对应关系
    print(f"正索引 {i} 对应 负索引 {neg_i}，值都是 '{data[i]}'")



# 定义一个较长的列表用于切片演示

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"原始列表: {numbers}")

# 使用正索引切片
print("\n使用正索引切片:")
# 从索引2开始到索引8结束（不包含8）
slice1 = numbers[2:8]
print(f"numbers[2:8] = {slice1}")

# 使用负索引切片
print("\n使用负索引切片:")
# 从倒数第8个元素开始到倒数第2个元素结束（不包含倒数第2个）
slice2 = numbers[-8:-2]
print(f"numbers[-8:-2] = {slice2}")

# 混合使用正负索引
print("\n混合使用正负索引:")
# 从索引2开始到倒数第2个元素结束
slice3 = numbers[2:-2]
print(f"numbers[2:-2] = {slice3}")

# 从倒数第5个元素开始到索引8结束
slice4 = numbers[-5:8]
print(f"numbers[-5:8] = {slice4}")

# 使用负索引获取最后几个元素
print("\n获取最后几个元素:")
# 获取最后3个元素
last_three = numbers[-3:]
print(f"最后3个元素 numbers[-3:] = {last_three}")
# 获取最后5个元素
last_five = numbers[-5:]
print(f"最后5个元素 numbers[-5:] = {last_five}")

# 使用负索引排除最后几个元素
print("\n排除最后几个元素:")
# 排除最后2个元素
exclude_last_two = numbers[:-2]
print(f"排除最后2个元素 numbers[:-2] = {exclude_last_two}")
# 排除最后4个元素
exclude_last_four = numbers[:-4]
print(f"排除最后4个元素 numbers[:-4] = {exclude_last_four}")


# 定义一个列表
items = ["apple", "banana", "cherry", "date", "elderberry"]

print(f"原始列表: {items}")
# range(-1, -len(items) - 1, -1)
# range(start, end, step)
# -1 -6 -1   -1到-5
# 方法1：使用range和负索引
print("\n方法1：使用range和负索引")
# 从-1开始到-len(items)-1结束，步长为-1
for i in range(-1, -len(items) - 1, -1):
    # 打印当前索引和对应的值
    print(f"索引 {i}: {items[i]}")

# 方法2：使用reversed函数
print("\n方法2：使用reversed函数")
# 使用reversed函数反向遍历列表
for item in reversed(items):
    # 打印当前值
    print(f"值: {item}")

# 方法3：使用切片[::-1]
print("\n方法3：使用切片[::-1]")
# 使用切片[::-1]创建反向列表
reversed_items = items[::-1]
# 遍历反向列表
for i, item in enumerate(reversed_items):
    # 计算原始索引
    original_index = len(items) - 1 - i
    # 打印原始索引和值
    print(f"原始索引 {original_index}: {item}")

# 方法4：使用enumerate和负索引
print("\n方法4：使用enumerate和负索引")
# 使用enumerate获取索引和值
for i, item in enumerate(items):
    # 计算对应的负索引
    negative_index = i - len(items)
    # 打印正索引、负索引和值
    print(f"正索引 {i}, 负索引 {negative_index}: {item}")




def is_palindrome(text):
    # 将字符串转换为小写并移除空格
    text = text.lower().replace(" ", "")
    # 使用负索引比较字符
    # len(text)=7 3  0 1 2
    for i in range(len(text) // 2):
        # 比较正索引和对应负索引位置的字符
        if text[i] != text[-(i + 1)]:
            # 如果不相等则不是回文
            return False
    # 如果所有字符都相等则是回文
    return True


# 字节和字符通过编码对应是吧 是的，同一个字符在不同的编码下对应字节是不一样的
# 我说 今天真冷，请你记下来，记录的时候可能不同的记录方式
# 测试几个字符串
test_strings = ["racecar", "hello", "A man a plan a canal Panama", "python"]

# 遍历测试字符串
for test_str in test_strings:
    # 检查是否为回文
    result = is_palindrome(test_str)
    # 打印结果
    print(f"'{test_str}' 是回文: {result}")



def rotate_array(arr, k):

    将数组向右旋转k个位置
    例如: [1, 2, 3, 4, 5] 右旋1位 -> [5, 1, 2, 3, 4]
    例如: [1, 2, 3, 4, 5] 右旋2位 -> [4, 5, 1, 2, 3]
    例如: [1, 2, 3, 4, 5] 右旋3位 -> [3, 4, 5,1, 2]

    # 处理k大于数组长度的情况 旋1位和旋6次一样的
    k = k % len(arr)
    # 通过负索引切片分段
    return arr[-k:] + arr[:-k]


# 测试数组旋转
print("\n=== 数组旋转演示 ===")
test_array = [1, 2, 3, 4, 5]
print(f"原始数组: {test_array}")
for k in [1, 2, 3]:
    rotated = rotate_array(test_array, k)
    print(f"向右旋转{k}位: {rotated}")

"""

# 定义不同的文件路径
file_paths = [
    "/home/user/documents/file.txt",
    "C:\\Users\\Admin\\Desktop\\data.csv",
    "/var/log/app.log",
    "config.ini",
    "folder/subfolder/file.py",
]

# 遍历文件路径
for path in file_paths:
    # 使用负索引获取文件名
    # 根据路径分隔符分割路径
    if "/" in path:
        # Unix/Linux路径分隔符
        filename = path.split("/")[-1]
    elif "\\" in path:
        # Windows路径分隔符
        filename = path.split("\\")[-1]
    else:
        # 没有路径分隔符，直接使用路径
        filename = path

    # 打印原始路径和提取的文件名
    print(f"路径: {path}")
    print(f"文件名: {filename}")

# 获取文件扩展名
print("=== 获取文件扩展名 ===")
# 定义文件列表
files = ["document.pdf", "avatar.image.jpg", "script.py", "data.xlsx", "readme"]

# 遍历文件列表
for file in files:
    # 使用负索引获取文件扩展名
    if "." in file:
        # 分割文件名和扩展名
        name_parts = file.split(".")
        # 获取扩展名（最后一个部分）
        extension = name_parts[-1]
        # 获取文件名（除扩展名外的所有部分）
        filename = ".".join(name_parts[:-1])
    else:
        # 没有扩展名
        extension = "无扩展名"
        filename = file

    # 打印文件名和扩展名
    print(f"文件: {file}")
    print(f"  文件名: {filename}")
    print(f"  扩展名: {extension}")


# 定义不同的URL
# url格式 协议 http https
# ://
# 域名 domain  baidu.com
# 文件或文件夹路径 /documents
# 文件名 page.html
urls = [
    "https://example.com/documents/page.html",
    "http://api.github.com/repos/user/repo/commits",
    "https://www.google.com/search?q=python",
    "ftp://files.example.com/data/file.zip",
    "https://subdomain.domain.com/path/to/resource",
]

# 遍历URL列表
for url in urls:
    # 使用负索引获取URL的不同部分
    # 分割URL
    url_parts = url.split("/")

    # 获取协议（第一部分）
    protocol = url_parts[0].replace(":", "")  # http
    # 获取域名（第二部分）
    domain = url_parts[2] if len(url_parts) > 2 else "无域名"
    # 获取最后一段（可能是文件名或资源名）
    last_segment = url_parts[-1] if url_parts[-1] else url_parts[-2]
    # 获取倒数第二段（可能是目录名）
    second_last = url_parts[-2] if len(url_parts) > 1 else "无"

    # 打印URL分析结果
    print(f"URL: {url}")
    print(f"  协议: {protocol}")
    print(f"  域名: {domain}")
    print(f"  最后一段: {last_segment}")
    print(f"  倒数第二段: {second_last}")

# 日志文件内容
# tail - f 日志文件名
# pm2 logs 应用名称
log_lines = [
    "2024-01-01 10:00:00 INFO: Application started",
    "2024-01-01 10:01:00 DEBUG: Loading configuration",
    "2024-01-01 10:02:00 INFO: Database connection established",
    "2024-01-01 10:03:00 WARNING: High memory usage detected",
    "2024-01-01 10:04:00 ERROR: Failed to process request",
    "2024-01-01 10:05:00 INFO: Application shutdown",
]

# 获取最新的几条日志
print("获取最新的3条日志:")
# 使用负索引切片获取最后3条日志
recent_logs = log_lines[-3:]
# 遍历最近的日志
for log in recent_logs:
    # 打印日志内容
    print(f"  {log}")

# 获取错误日志
print("\n获取所有错误日志:")
# 遍历所有日志
for log in log_lines:
    # 使用负索引检查日志级别（最后部分）
    log_parts = log.split(":")
    # 获取日志级别（倒数第二个部分）
    if len(log_parts) >= 2:
        log_level = log_parts[-2].strip()
        # 如果是错误日志则打印
        if "ERROR" in log_level:
            print(f"  {log}")

# 获取日志的时间戳
print("\n获取日志时间戳:")
# 遍历所有日志
for log in log_lines:
    # 使用负索引获取时间戳（前两个部分）
    log_parts = log.split(" ")
    # 获取日期和时间
    if len(log_parts) >= 2:
        date = log_parts[0]
        time = log_parts[1]
        # 打印时间戳
        print(f"  {date} {time}")
