

# ---------------------------------------------------------------------------
# 1.26-2.2 实际使用2- 文件读写模式


# Q1: 1100如果右移3位  会怎么样
# A: 结果是 1

print(0b1100 >> 4 == 0b1100 >> 5)    # True



# Q2: 感觉r+，w+，a+是一样的作用？
# A:
# w 清空原来内容写入
# a 在原来内容的尾部追加写入
# 注意这些表示的是 操作权限，可不是操作顺序 🌟🌟

with open("./test.txt", "r+") as file:
   file.write("It's test.txt~~ new 1")
   file.read()

   file.read()
   file.write("It's test.txt~~ new 2")



# Q3: set_mode 通过  mode | fllag实现能懂。另外清除切换包含三个操作 位迅运算 不太理解。
# A:

READ = 0b0001     # 1
WRITE = 0b0010    # 2
APPEND = 0b0100   # 4
mode = 0b0000

# + READ
mode |= READ    # 0b0001
mode |= 0b0010  # 0b0011  ==> 3
print(mode)     # 3

# ~READ           0b1110
mode &= ~READ  #  0b0010 ==>   2
print(mode)     # 2



# ---------------------------------------------------------------------------
# 1.26-2.3 实际使用3- Unicode 字符 → UTF-8 字节

b = bytes([65])
print(b)