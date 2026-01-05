# a = 1
# print(a + 2 + 3)


def fn(a):
    print(a + 2)
    # return None python
    # return undefined js   null 空 undefined 未定义


print(fn(1))


# js 只能通过位置传参
# python里 有位置参数和关键字参数
def add(a, b, suffix=4):
    return a + b


add(1, 2)
add(1, 2, suffix=3)
