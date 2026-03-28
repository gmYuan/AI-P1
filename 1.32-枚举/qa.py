


# ---------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:8])

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers)  # <filter object at 0x0000021D6A4659C0>

print(list(even_numbers)[3:8])



# ---------------------------------------------------------------------------

# 使用列表推导式和enumerate()查找所有位置

#    positions = [index for index, value in enumerate(lst) if value == target]
nums = [1, 2, 3]
list2 = [item * 2 for item in nums if item > 1]
print(list2)



# ---------------------------------------------------------------------------
# 定义一个字符串列表
words = ["hello", "world", "python", "programming"]

# 使用map()将字符串转换为大写
upper_words = map(str.upper, words)

# 使用enumerate()遍历转换后的结果
for index, word in enumerate(upper_words, start=1):
    # 打印序号和大写单词
    print(f"单词{index}: {word}")


lst = list(upper_words)
print(lst)
print(len(lst))  # 这个lst 为啥成[]了， 因为迭代器被上面的 for 循环遍历使用了
