"""
# 定义一个停止值，序列将在此值之前结束
stop_value = 5
# 遍历从0到stop_value-1的整数
for i in range(stop_value):
    # 打印当前整数
    print(i)



# 定义序列的起始值
start_value = 2
# 定义序列的停止值
stop_value = 5
# 遍历从start_value到stop_value-1的整数
for i in range(start_value, stop_value):
    # 打印当前整数
    print(i)



# 定义序列的起始值
start_value = 1
# 定义序列的停止值
stop_value = 10
# 定义序列的步长
step_value = 2
# 遍历从start_value到stop_value-1，步长为step_value的整数
for i in range(start_value, stop_value, step_value):
    # 打印当前整数
    print(i)


# 生成一个range对象，表示从0到4的序列
my_range_object = range(5)
print(my_range_object)
# 将range对象转换为列表并打印
print(list(my_range_object))


# 创建一个非常大的range对象
large_range = range(100000)
range = (0, +1)
for i in range:
    print(i)
# 打印range对象的内存占用（非常小）
print(f"range对象大小: {large_range.__sizeof__()} 字节")  # 48 字节

# 如果转换为列表，内存占用会很大
large_list = list(large_range)  # 这会占用大量内存
print(f"列表大小: {large_list.__sizeof__()} 字节")  # 8000040 字节


# 定义序列的起始值
start_value = 5
# 定义序列的停止值
stop_value = 0
# 定义负数步长，实现递减
negative_step = -1
# 遍历从start_value到stop_value+1，步长为negative_step的整数
for i in range(start_value, stop_value, negative_step):
    # 打印当前整数
    print(i)


# 创建一个从0到9的range对象
r = range(10)
print(list(r))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 对range对象进行切片操作：从索引2开始，到索引8结束（不包含），步长为2
# 结果将是range(2, 8, 2)
print(r[2:8:2])
# 将切片结果转换为列表查看
print(list(r[2:8:2]))  # [2, 4, 6]
"""
