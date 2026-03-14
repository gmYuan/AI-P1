"""
# 定义一个列表，它是一个典型的可迭代对象
my_list = [10, 20, 30, 40]

# 直接使用for循环遍历可迭代对象
print("--- 遍历列表 (Iterable) ---")
for item in my_list:
    # 打印当前元素
    print(item)
# 输出: 10, 20, 30, 40

# 字符串也是可迭代对象
my_string = "Hello"
print("\n--- 遍历字符串 (Iterable) ---")
for char in my_string:
    # 打印当前字符
    print(char)
# 输出: H, e, l, l, o


# 定义一个列表，作为可迭代对象
my_list = [10, 20, 30]

# 从可迭代对象my_list中获取一个迭代器
my_iterator = iter(my_list)

print("--- 使用迭代器 (Iterator) ---")
# 使用next()函数获取迭代器的下一个元素
print("第一次获取:", next(my_iterator))  # 输出 10
print("第二次获取:", next(my_iterator))  # 输出 20
print("第三次获取:", next(my_iterator))  # 输出 30

# 尝试获取第四个元素，此时迭代器已耗尽，会抛出StopIteration异常
try:
    print("第四次获取:", next(my_iterator))
except StopIteration:
    # 捕获StopIteration异常，表示迭代结束
    print("迭代器已耗尽，没有更多元素了。")

# 迭代器一旦耗尽，就不能再使用。如果需要重新迭代，必须重新获取迭代器
print("\n--- 重新获取迭代器并遍历 ---")
# 重新从my_list获取一个新的迭代器
another_iterator = iter(my_list)
# 遍历新的迭代器
for item in another_iterator:
    # 打印当前元素
    print(item)



# 可迭代对象 迭代器 迭代协议
# 自定义的迭代器
class MyCustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    # 实现__iter__方法，返回自己
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


myCustomIterator = MyCustomIterator([10, 20, 30])
# 1.获取myCustomIterator.__iter__()=获取myCustomIterator 2.myCustomIterator.__next__()

# it = myCustomIterator.__iter__()
# value1 = it.__next__()
# print(value1)
# value1 = it.__next__()
# print(value1)
# value1 = it.__next__()
# print(value1)

for item in myCustomIterator:
    print(item)



class MyCustomIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    # 实现__iter__方法，返回自己
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable.data):
            result = self.iterable.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyCustomIterator(self)


myIterable = MyIterable([10, 20, 30])

it1 = myIterable.__iter__()
v1 = it1.__next__()
v2 = it1.__next__()
v3 = it1.__next__()
print(v1, v2, v3)

it2 = iter(myIterable)
v1 = next(it2)
v2 = next(it2)
v3 = next(it2)
print(v1, v2, v3)

# for i in MyIterable([10,20,30]) 这样可以么
for i in MyIterable([10, 20, 30]):
    print(i)
# MyIterable的实现是不是就是相当于list的实现？
# myIterable本身就可以遍历吧 是的
# Iterable可以被 for in 遍历 是因为它的__iter__会返回迭代器。
# Iterator 实现了__iter__和__next__方法
# Iterable实现了__iter__方法



# 定义一个简单的生成器函数
def simple_gen():
    # 第一次调用next()时，yield 1并暂停
    yield 1
    # 第二次调用next()时，从上次暂停的地方继续，yield 2并暂停
    yield 2
    # 第三次调用next()时，从上次暂停的地方继续，yield 3并暂停
    yield 3


# 创建生成器对象
gen = simple_gen()
# 打印生成器对象的类型
print(f"生成器对象类型: {type(gen)}")
# 输出: <class 'generator'>

# 使用next()函数逐个获取值
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 2
print(next(gen))  # 输出: 3

# 再次调用next()会抛出StopIteration异常
try:
    print(next(gen))
except StopIteration:
    # 捕获StopIteration异常，表示生成器已耗尽
    print("生成器已耗尽，没有更多值")
#  iterable 可迭代对象
#  iterator 迭代器
#  generator 生成器
#  生成器函数就是一个特殊的函数，特殊在里面使用了yield 关键字  创建生成器对象的函数

# 可迭代对象和迭代器啥区别
# 迭代器代表一次读取过程

# 生成器函数怎么遵循迭代协议的？
# 迭代协议指的就是两个方法__iter__和__next__，只要有这二个方法就相当于遵循了迭代协议
# 迭代器能执行next方法，但可迭代对象不能，或者说不一定
# 感觉可迭代对象可以for in多次，迭代器只能for in一次，
# #可迭代对象的__iter_返回的是一个新迭代器

# 每次for in 都可以有新的迭代器， 这个不一定
# 关键要看for in 的对象是谁，如果这个对象iter方法返回的是自己，那就不行了。如果返回是新迭代器才可以
# 那刚刚举例子 10 20 30那个 不是只打印了一次


class MyCustomIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    # 实现__iter__方法，返回自己
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable.data):
            result = self.iterable.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyCustomIterator(self)


myIterable = MyIterable([10, 20, 30])
for item in myIterable:
    print(item)
for item in myIterable:
    print(item)


class MyCustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    # 实现__iter__方法，返回自己
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


print("=" * 50)
myCustomIterator = MyCustomIterator([10, 20, 30])
for item in myCustomIterator:
    print(item)
for item in myCustomIterator:
    print(item)


# 迭代器的iter，和可迭代对象的iter实现区别再看下
# 1.相同点，都是调用__iter__方法
# 2.不同点 可迭代对象的__iter__方法返回的可能是一个别的迭代器的实例
# 2.       迭代器的的__iter__方法返回的只能是自己

# 定义一个生成器函数
def number_generator():
    # 生成数字1到5
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# 创建生成器对象
gen = number_generator()

# 使用for循环遍历生成器
# for循环会自动处理next()调用和StopIteration异常
print("使用for循环遍历生成器:")
for num in gen:
    # 打印每个生成的值
    print(num)
# 输出: 1, 2, 3, 4, 5

# 注意：生成器一旦耗尽，就不能再次使用
print("\n尝试再次遍历已耗尽的生成器:")
for num in gen:
    print(num)  # 这行不会执行，因为生成器已耗尽

# 使用生成器表达式创建生成器
# 语法类似于列表推导式，但使用圆括号而不是方括号
my_gen = (x * x for x in range(10))
print(f"生成器表达式类型: {type(my_gen)}")
# 输出: <class 'generator'>

# 使用for循环遍历生成器表达式
print("生成器表达式的结果:")
for num in my_gen:
    # 打印每个平方数
    print(num)
# 输出: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81




# 内存使用对比
import sys

# 列表推导式：立即创建所有元素，内存中会存储所有元素
list_comp = [x * x for x in range(1000)]
print(f"列表推导式类型: {type(list_comp)}")
print(f"列表推导式大小: {len(list_comp)} 元素")
print(f"列表推导式内存使用: {sys.getsizeof(list_comp)} 字节")

# 生成器表达式：惰性求值，内存中只存储当前需要的元素
gen_expr = (x * x for x in range(1000))
print(f"生成器表达式类型: {type(gen_expr)}")
# 生成器表达式没有len()方法，因为它是惰性的
print(f"生成器表达式内存使用: {sys.getsizeof(gen_expr)} 字节")

# 复杂生成器表达式
complex_gen = (x**2 + 2 * x + 1 for x in range(5) if x % 2 == 0)
print("\n复杂生成器表达式结果:")
for value in complex_gen:
    print(value)
# 输出: 1, 9, 25 (对应x=0,2,4的x**2+2x+1)



# 定义一个生成无限数字序列的生成器函数
def infinite_numbers(start=0):
    # 初始化数字
    num = start
    # 无限循环
    while True:
        # 生成当前数字
        yield num
        # 数字递增
        num += 1


# 创建无限生成器
infinite_gen = infinite_numbers()
print("无限序列生成器:")
# 获取前10个数字
for i in range(10):
    # 使用next()获取下一个数字
    print(next(infinite_gen))
# 输出: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


# 斐波那契数列生成器
def fibonacci():
    # 初始化前两个数
    a, b = 0, 1
    # 无限循环生成斐波那契数
    while True:
        # 生成当前数
        yield a
        # 更新下一个数
        a, b = b, a + b


# 创建斐波那契生成器
fib_gen = fibonacci()
print("\n斐波那契数列:")
# 生成前10个斐波那契数
for i in range(10):
    print(next(fib_gen))
# 输出: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def double_yield():
    print("start running")
    x = yield
    while True:
        x = yield x * 2


gen = double_yield()
next(gen)
# 可通过send方法向生成器里面传值
print(gen.send(10))  # 20
print(gen.send(5))  # 10
print(gen.send(3))  # 6


# min max sum next len


def exception_handling_generator():
    try:
        while True:
            yield "正常运行中..."
    except GeneratorExit:
        print("生成器已经关闭")
    finally:
        print("生成器清理完成")


gen = exception_handling_generator()
print(next(gen))
# 关闭生成器，这将触发GeneratorExit异常，并被 内部的 except GeneratorExit:捕获
# gen.close()
# gen.throw()
print(next(gen))  # StopIteration




# 使用迭代器实现平方数生成
class SquareIterator:
    # 构造函数
    def __init__(self, n):
        # 存储最大值
        self.n = n
        # 初始化当前值
        self.current = 0

    # 实现__iter__方法
    def __iter__(self):
        return self

    # 实现__next__方法
    def __next__(self):
        # 检查是否超出范围
        if self.current >= self.n:
            raise StopIteration
        # 计算平方数
        result = self.current**2
        # 更新当前值
        self.current += 1
        # 返回平方数
        return result


# 使用生成器函数实现相同的功能
def square_generator(n):
    # 循环生成平方数
    for i in range(n):
        # 产出平方数
        yield i**2


# 测试迭代器
print("使用迭代器:")
# 创建迭代器实例
square_iter = SquareIterator(5)
# 遍历迭代器
for num in square_iter:
    print(num)
# 输出: 0, 1, 4, 9, 16

# 测试生成器
print("\n使用生成器:")
# 创建生成器
square_gen = square_generator(5)
# 遍历生成器
for num in square_gen:
    print(num)
# 输出: 0, 1, 4, 9, 16

# 代码行数对比
print(f"\n迭代器类代码行数: 约15行")
print(f"生成器函数代码行数: 约3行")
print("生成器更简洁！")



# for 循环的内部实现原理
iteratable = [10, 20, 30]
for item in iteratable:
    print(item)

# 1.获取迭代器
it = iter(iteratable)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break


def double_yield():
    print("start running")
    x = yield
    x = yield x * 2


gen = double_yield()
# next(gen)
# 可通过send方法向生成器里面传值
# 不能向一个刚开始的 生成器传递非None的值
# TypeError: can't send non-None value to a just-started generator
print(gen.send(None))  # 20 next send=传值并next
print(gen.send(5))  # 10
print(gen.send(3))  # 6


def double_yield():
    print("start running")
    x = yield None
    x = yield x * 2


gen = double_yield()
print(next(gen))
print(gen.send(10))
print(gen.send(50))  # StopIteration




def getPinyinOfChineseName():
    print("start running")
    chineseName = yield
    yield chineseName + "的拼音"


gen = getPinyinOfChineseName()
next(gen)
result = gen.send("张三")
print(result)



# ，没体现异步yield

import asyncio


# 异步生成器
async def async_generator_basic():
    for i in range(5):
        await asyncio.sleep(1)
        yield i


# 使用async for 消费异步生成器
async def consume_async_generator():
    print("开始消费异步生成器")
    async for value in async_generator_basic():
        print(f"收到值{value}")


asyncio.run(consume_async_generator())
"""
