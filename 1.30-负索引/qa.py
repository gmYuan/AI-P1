

# ---------------------------------------------------------------------------
# 1.30-3 循环遍历中的使用

items = ["apple", "banana", "cherry", "date", "elderberry"]
# 使用切片[::-1]创建反向列表 ['elderberry', 'date', 'cherry', 'banana', 'apple']
reversed_items = items[::-1]
print(reversed_items)

# 遍历反向列表
for i, item in enumerate(reversed_items):
    # 计算原始索引
    original_index = len(items) - 1 - i
    # 打印原始索引和值
    print(f"原始索引 {original_index}: {item}")


# 例2
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers1 = numbers[-8:-2]
print(numbers1)  # [3, 4, 5, 6, 7, 8]
numbers2 = numbers[-2:-8:-1]
print(numbers2)  # [9, 8, 7, 6, 5, 4]


# 我刚才试了a = num[-2:-8:] 是空的。说明不支持从右到左的正向

numbers3 = numbers[-2:-8:1]
# start=8  end=3 |  startIndex=8,endIndex=3 1   index需要大于等于8，小于3
print(numbers3)

# start=8  end=3 |  startIndex=8,endIndex=3 1   index需要大于等于8，小于3
numbers4 = numbers[-2:-8:-1]
print(numbers4)



# ---------------------------------------------------------------------------
# 1.30-4.2 循环在 算法应用 2- 数组旋转

l1 = [1, 2]
l2 = [3, 4]
l3 = l1 + l2

print(l3)



# ---------------------------------------------------------------------------
# 1.30-5.3 实际应用2- 日志文件内容

import logging

arr6 = ["a", "b", "c"]
print(arr6[-1])