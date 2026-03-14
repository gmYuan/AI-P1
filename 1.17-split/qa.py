


# -------------------------------------------------------------------------------
# 1.17-1.3 split的 分隔符参数


text_with_whitespace = "apple   orange\tbanana\ncherry"
space_split = text_with_whitespace.split(" ")
print("指定空格分割:", space_split)  # 指定空格分割: ['apple', '', '', 'orange\tbanana\ncherry']



# 1.17-1.3 split的 分隔符参数-  对分割个数的理解答疑

# Q:
# 3个连续空格，第一个视为分割符，没了，
# 第二个是被分割的保留了，
# 那为啥第三个为什么没有被视为分隔符，而是被保留了，

# A：用, 更容易直观看出来

text_with_whitespace = "apple,,,orange\tbanana\ncherry"
space_split = text_with_whitespace.split(",")
print("指定,分割:", space_split)

print(",".join("a,b,c".split(",")))

print(",a,,,b".split(","))  # ['', 'a', '', '', 'b']
