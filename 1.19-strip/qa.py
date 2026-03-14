

# ---------------------------------------------------------------------------
# 1.19-4.1 str的切片性能优化： 短字符串缓存策略

str1 = "abcde"
str2 = "bcd"
str3 = str1[1:4]

print("st1是：" + str1, id(str1))
print("st2是：" + str2, id(str2))
print("st3是：" + str3, id(str3))
str4 = "bcd"
print("st4是：" + str4, id(str4))
print(str2 is str4)

print("-------------------------------")


# ---------------------------------------------------------------------------
# 1.19-4.2 split 和 list


# print("abc".split(""))  # ValueError: empty separator
# 没有分隔符的话，是没有办法将abc改为[a,b,c]的 只能通过list来生成
print(list("abc"))
