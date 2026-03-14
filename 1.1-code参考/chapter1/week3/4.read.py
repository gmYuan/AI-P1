"""
# 创建测试文件内容，包含多行文本
test_content = "第一行：Python文件读取
第二行：read()方法示例
第三行：一次性读取全部内容
第四行：适合小文件处理
第五行：返回字符串类型"

# 以写入模式打开文件，使用UTF-8编码
with open("test_file.txt", "w", encoding="utf-8") as f:
    # 将测试内容写入文件
    f.write(test_content)

# 使用read()方法读取文件
with open("test_file.txt", "r", encoding="utf-8") as file:
    # 使用read()方法一次性读取整个文件内容
    content = file.read()
    # 打印提示信息
    print("完整文件内容：")
    # 使用repr()函数显示内容，包括换行符等特殊字符
    print(repr(content))  # 使用repr显示换行符
    # 打印换行符
    print("\n实际显示：")
    # 直接打印内容，正常显示文本
    print(content)
    # 打印内容长度（字符数）
    print(f"内容长度: {len(content)} 字符")
    # 打印当前文件指针位置
    print(f"文件指针位置: {file.tell()}")


# 1\n2\n3\n
# 以读取模式打开文件，使用UTF-8编码
with open("test_file.txt", "r", encoding="utf-8") as file:
    # 打印提示信息
    print("逐行读取文件：")
    print(f"  文件指针位置: {file.tell()}")
    # 初始化行号计数器
    line_number = 1

    # 使用无限循环逐行读取文件
    while True:
        # 使用readline()方法读取一行内容
        line = file.readline()
        # 如果读取的行为空（文件结束），则跳出循环
        if not line:  # 文件结束
            break

        # 打印当前行号和使用repr()显示的行内容   # 1\n   2\n 3\n
        print(f"第{line_number}行: {repr(line)}")
        # 打印去除首尾空白字符的行内容
        print(f"  内容: {line.strip()}")  # 1
        # 打印当前文件指针位置
        print(f"  文件指针位置: {file.tell()}")
        # 打印空行用于分隔
        print()
        # 行号计数器加1
        line_number += 1

# 重置文件指针并演示指定大小读取
print("=== readline() 指定大小读取 ===")
# 重新打开文件进行指定大小读取演示
with open("test_file.txt", "r", encoding="utf-8") as file:
    # 使用readline(2)只读取前4个字符
    partial_line = file.readline(2)
    # 打印读取到的部分内容
    print(f"读取前2个字符: {repr(partial_line)}")
    # 继续读取剩余内容 再调用readline会从当前指针的位置继续读取到行尾
    print(f"剩余内容: {repr(file.readline())}")

# 文件都要在内存里操作吗，可以在磁盘直接该吗?
# 如果一行中存在\n,\t时，是到\n结束还是到\t结束？ \t是制表符，不是行的结束，
# \n newline
# 如果一行后面有N个空格，然后再换行，读到的是什么？ 空格 普通 的字符是一样

# readline是迭代器？
# \t 是tab吗  是的同代表2个或4个空格，也是空白字符的一种 这个可以由编辑器自己定义
# 中文字符是不是一个 指针推进3个或者2个 如果中文的话，一个中文汉字对应3个字节，所以索引或者说指针
# 一个汉字也会移动3位 因为这个指针指的是字节的移动指针
# 有特别罕见的汉字也也会占用四个字节
# \n换行符 它其实是一个字符，在内存里占用一个字节 指针的位置也是占的是一个位置
# readeline(2) 这个2应该指的字符吧 是的


# read(）参数是字符数量 字一个字可能是一个字节，一个位置 ，也可能是2个字节，2个位置 ，也可能是3个字节3个位置
# windows读换行 读取2个字节 2个位置  mac里读取1个字节，1个位置
# with open("test.txt", "w", encoding="utf-8") as f:
#    f.write("AB\nCD")
#   f.write("A中\r\nCD")
# windows 0->1->4->6->->8
# mac 0->1->4->5->6->7
# 那就是read 读取整个文件 跟readline有区别？ readline只读一行
with open("test.txt", "r", encoding="utf-8") as f:
    pos1 = f.tell()
    print(f"刚开始的时候指针的位置是{pos1}")
    char1 = f.read(1)
    pos1 = f.tell()
    print(f"读取了{char1}后，指针的位置是{pos1}")
    char1 = f.read(1)
    pos1 = f.tell()
    print(f"读取了{char1}后，指针的位置是{pos1}")
    char1 = f.read(1)
    pos1 = f.tell()
    print(f"读取了{repr(char1)}后，指针的位置是{pos1}")
    char1 = f.read(1)
    pos1 = f.tell()
    print(f"读取了{char1}后，指针的位置是{pos1}")
    char1 = f.read(1)
    pos1 = f.tell()
    print(f"读取了{char1}后，指针的位置是{pos1}")


# 不同的操作系统换行符是不一样的
# windows  \r\n 回车 换行
# linux \n 换行符
# 工作还得统一电脑型号吗 不需要 因为readline的话读到数据是一样的
# read读的字符，也是一样的啊
# 即和操作系统有关，如果以编码格式GBK打开，结果又不一样

with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    print("字节的长度" + str(len(content.encode("utf-8"))))

# 以读取模式打开文件，使用UTF-8编码
with open("test.txt", "r", encoding="utf-8") as file:
    # 使用readlines()方法一次性读取所有行，返回列表
    lines = file.readlines()

    # 打印返回数据的类型
    print(f"返回类型: {type(lines)}")
    # 打印行数（列表长度）
    print(f"行数: {len(lines)}")
    # 打印提示信息
    print("\n所有行内容：")

    # 使用enumerate遍历所有行，从1开始计数
    for i, line in enumerate(lines, 1):
        # 打印行号和使用repr()显示的行内容
        print(f"第{i}行: {repr(line)}")

    # 打印当前文件指针位置 文件指针就指向下一个要读的位置 0
    print(f"\n文件指针位置: {file.tell()}")

    # 处理每行（去除换行符）
    print("\n处理后的内容：")
    # 再次遍历所有行，去除首尾空白字符
    for i, line in enumerate(lines, 1):
        # 使用strip()方法去除行首尾的空白字符（包括换行符）
        clean_line = line.strip()
        # 打印处理后的行内容
        print(f"第{i}行: {clean_line}")

# 还是老师说的每一行的长度加起来后，后面就是指针执行的位置是这样的




# seek方法可以移动文件指针 的位置 ，它允许 你在文件中随机访问，而不是只能顺序访问
# seek(offset,whence) offset移动的偏移量  whence指的是参考的位置 可选，默认是0
#  whence参数传的可不是位置 ，而是一个枚举值,指的是三种模式
#   0  从开头移动
#   1  从当前的位置计算
#   2  从文件的末尾计算
# 其实这个光标或者说指针是可以移动
# A中\r\nCD\r\nEF

with open("test.txt", "r", encoding="utf-8") as f:
    pos1 = f.tell()
    print(f"刚开始的时候指针的位置是{pos1}")  # 0
    char1 = f.read(1)
    pos1 = f.tell()
    print(f"读取了{char1}后，指针的位置是{pos1}")  # 1
    char1 = f.read(1)
    pos1 = f.tell()
    print(f"读取了{char1}后，指针的位置是{pos1}")  # 4
    # char1 = f.read(1)
    # pos1 = f.tell()
    # print(f"读取了{repr(char1)}后，指针的位置是{pos1}")  # 6
    # f.seek(1)
    # f.seek(1, 0)
    f.seek(3, 1)
    char1 = f.read(1)
    pos1 = f.tell()
    print(f"读取了{char1}后，指针的位置是{pos1}")


# A中\r\nCD\r\nEF
# 在文本模式下只能使用seek(offset,0) 从开头
# 不有使用 seek(offset,1) seek(offset,2)
with open("test.txt", "rb", encoding="utf-8") as f:
    # 从文件的开头移动5个位置
    f.seek(5, 0)
    print(repr(f.read(1)))
    # 从当前的位置再移动3个位置 offset：移动的字节数，可以是正数（向前）或负数（向后）
    # f.seek(1, 1)
    # io.UnsupportedOperation: can't do nonzero cur-relative seeks
    # print(repr(f.read(1)))
    # 从文件的末尾开始计算，向前移动3个位置

    f.seek(-3, 2)
    print(repr(f.read(1)))
"""

# 使用二进制模式才可能使用 1 和2
with open("test.txt", "rb") as f:
    f.seek(-5, 2)
    print(repr(f.read(1)))
