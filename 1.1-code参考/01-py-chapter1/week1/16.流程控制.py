"""
# break语句的基本使用
# 遍历数字0到4，当遇到3时跳出循环
for i in range(5):
    if i == 3:
        break  # 当i等于3时，跳出循环
    print(i)  # 只打印0, 1, 2

# 输出结果: 0, 1, 2


# while循环中使用break
# 初始化计数器
count = 0

# 当计数器小于10时循环
while count < 10:
    if count == 5:
        break  # 当计数器等于5时跳出循环
    print(f"计数: {count}")
    count += 1

# 输出结果: 计数: 0, 计数: 1, 计数: 2, 计数: 3, 计数: 4


# continue语句的基本使用
# 遍历数字0到4，跳过数字3
for i in range(5):
    if i == 3:
        continue  # 跳过当前迭代，进入下一次迭代
    print(i)  # 打印0, 1, 2, 4

# 输出结果: 0, 1, 2, 4


# while循环中使用continue
# 初始化计数器
count = 0

# 当计数器小于5时循环
while count < 5:
    count += 1
    if count == 3:
        continue  # 跳过计数器为3的迭代
    print(f"计数: {count}")

# 输出结果: 计数: 1, 计数: 2, 计数: 4, 计数: 5

# pass语句的基本使用
# 遍历数字0到4，对数字3不做任何操作
for i in range(5):
    if i == 3:
        pass  # 对数字3不做任何操作，继续执行后续代码
    print(i)  # 打印0, 1, 2, 3, 4

# 输出结果: 0, 1, 2, 3, 4


print("=== break示例 ===")
# 使用break终止循环
for i in range(5):
    if i == 3:
        break  # 终止循环
    print(f"break - i = {i}")

print("\n=== continue示例 ===")
# 使用continue跳过当前迭代
for i in range(5):
    if i == 3:
        continue  # 跳过当前迭代
    print(f"continue - i = {i}")

print("\n=== pass示例 ===")
# 使用pass不做任何操作
for i in range(5):
    if i == 3:
        pass  # 不做任何操作
    print(f"pass - i = {i}")
"""

# 嵌套循环中的break只影响内层循环
print("=== 嵌套循环中的break ===")

# 外层循环和内层循环
for i in range(3):
    print(f"外层循环: {i}")
    for j in range(3):
        if j == 1:
            break  # 只跳出内层循环
        print(f"  内层循环: {i}, {j}")

# 输出结果:
# 外层循环: 0
#   内层循环: 0, 0
# 外层循环: 1
#   内层循环: 1, 0
# 外层循环: 2
#   内层循环: 2, 0


# 嵌套循环中的continue只影响内层循环
print("\n=== 嵌套循环中的continue ===")

# 外层循环和内层循环
for i in range(3):
    print(f"外层循环: {i}")
    for j in range(3):
        if j == 1:
            continue  # 只跳过内层循环的当前迭代
        print(f"  内层循环: {i}, {j}")
