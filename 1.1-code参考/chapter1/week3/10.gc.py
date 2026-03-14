import sys
import gc

"""
import sys

a = []
print(f"创建空列表后，引用计数为{sys.getrefcount(a)-1}")
b = a
print(f"b = a后，引用计数为{sys.getrefcount(a)-1}")
c = a
print(f"c = a后，引用计数为{sys.getrefcount(a)-1}")
del b
print(f"del b后，引用计数为{sys.getrefcount(a)-1}")
c = None
print(f"c = None后，引用计数为{sys.getrefcount(a)-1}")
del a
print(f"删除a之后，列表对象被垃圾回收{sys.getrefcount(a)-1}")


# 创建对象
import sys


obj = [1, 2, 3]
print(f"1. 创建对象后引用计数: {sys.getrefcount(obj)-1}")

# 赋值给变量
ref1 = obj
print(f"2. 赋值给ref1后引用计数: {sys.getrefcount(obj)-1}")

# 添加到列表
my_list = [obj]
print(f"3. 添加到列表后引用计数: {sys.getrefcount(obj)-1}")


# 作为函数参数
def test_func(param):
    print(f"4. 作为函数参数时引用计数: {sys.getrefcount(param)-1}")
    return param


result = test_func(obj)
print(f"5. 函数返回后引用计数: {sys.getrefcount(obj)-1}")

# 删除引用
del ref1
print(f"6. 删除ref1后引用计数: {sys.getrefcount(obj)-1}")

# 从列表中移除
my_list.remove(obj)
print(f"7. 从列表中移除后引用计数: {sys.getrefcount(obj)-1}")

# 重新赋值
result = None
print(f"8. result重新赋值后引用计数: {sys.getrefcount(obj)}")
del obj
print("9. 删除obj后引用计数: 0")


# 创建两个对象
obj1 = []
obj2 = []
print(f"创建obj1后引用计数: {sys.getrefcount(obj1)-1}")
print(f"创建obj2后引用计数: {sys.getrefcount(obj2)-1}")
# 创建循环引用
obj1.append(obj2)
obj2.append(obj1)
print(f"创建循环引用后obj1引用计数: {sys.getrefcount(obj1)-1}")
print(f"创建循环引用后obj2引用计数: {sys.getrefcount(obj2)-1}")
# 删除外部引用
del obj1, obj2
print("删除外部引用后，对象仍然存在循环引用")
print("此时引用计数无法回收这些对象")
# 手动触发垃圾回收
collected = gc.collect()
print(f"垃圾回收器回收了 {collected} 个对象")

def show_generational_gc_stats():
    stats = gc.get_stats()  # 返回第0、1、2代的GC信息
    gen_names = ["第0代（年轻代）", "第1代（中年代）", "第2代（老年代）"]
    for i, stat in enumerate(stats):
        print(f"{gen_names[i]}: ")
        print(f"   回收次数 (collections): {stat['collections']}")
        print(f"   回收对象数 (collected): {stat['collected']}")
        print(f"   无法回收 (uncollectable): {stat['uncollectable']}")


print("分代垃圾回收状态：")
show_generational_gc_stats()

print("手动触发第0代垃圾回收...")
collected = gc.collect(0)
print(f"回收了 {collected} 个对象")

print("手动触发第2代（全代）垃圾回收...")
collected = gc.collect(2)
print(f"回收了 {collected} 个对象")


import gc

# 1. 显示当前垃圾收集器状态
print("当前GC开关:", gc.isenabled())  # True一般表示默认开启

# 2. 主动关闭、再开启GC
gc.disable()
print("关闭GC:", gc.isenabled())
gc.enable()
print("重新开启GC:", gc.isenabled())

# 3. 手动收集所有不可达对象
print("手动触发一次全代垃圾回收")
unreachable = gc.collect()
print(f"共清理不可达对象数量: {unreachable}")

# 4. 只收集第0代（年轻代）
print("只收集第0代GC: ", gc.collect(0))


gc.set_debug(gc.DEBUG_LEAK)  # 打开gc调试模式
gc.collect()
gc.set_debug(0)  # 关闭调试模式



# 小对象的内存管理
import sys

print("小对象内存管理:")
small_objects = []
for i in range(10):
    # 创建小对象
    obj = i
    small_objects.append(obj)
    print(f"对象 {i} 的内存地址: {id(obj)}")

# 字符串的内存优化
print("\n字符串内存优化:")
str1 = "hello"
str2 = "hello"
print(f"str1 内存地址: {id(str1)}")
print(f"str2 内存地址: {id(str2)}")
print(f"str1 和 str2 是同一个对象: {str1 is str2}")

# 大对象的内存管理
print("\n大对象内存管理:")
large_object = [i for i in range(10000)]
print(f"大对象内存地址: {id(large_object)}")
print(f"大对象大小: {sys.getsizeof(large_object)} 字节")

# 内存池的复用
print("\n内存池复用:")
del large_object
new_large_object = [i for i in range(10000)]
print(f"新大对象内存地址: {id(new_large_object)}")

# 启动tracemalloc，开始跟踪内存分配
import tracemalloc

tracemalloc.start()

# 获取初始内存快照
snapshot1 = tracemalloc.take_snapshot()
print("初始内存快照已创建")

# 创建一些对象来模拟内存分配
print("\n创建对象...")
my_list = [str(i) * 100 for i in range(10000)]
my_dict = {i: f"value_{i}" for i in range(5000)}
my_set = set(range(1000))

# 获取第二个内存快照
snapshot2 = tracemalloc.take_snapshot()
print("对象创建后内存快照已创建")

# 比较两个快照
top_stats = snapshot2.compare_to(snapshot1, "lineno")
print("\n内存分配统计 (前10个最大的分配):")
for stat in top_stats[:10]:
    print(stat)

# 获取当前内存使用情况
current, peak = tracemalloc.get_traced_memory()
print(f"\n当前内存使用: {current / 1024 / 1024:.2f} MB")
print(f"峰值内存使用: {peak / 1024 / 1024:.2f} MB")

# 停止内存跟踪
tracemalloc.stop()
print("\n内存跟踪已停止")

# 清理对象
del my_list, my_dict, my_set
print("对象已清理")



# 导入os模块，用于获取当前进程ID
import os

# 导入psutil模块，用于获取进程的内存信息
import psutil

# 导入gc模块，用于垃圾回收
import gc

# 获取当前进程对象
process = psutil.Process(os.getpid())
# 打印初始时进程的内存使用情况（以MB为单位）
print(f"初始内存: {process.memory_info().rss / 1024 / 1024:.2f} MB")

# 创建一个空列表，用于存储对象
objs = []

# 循环10万次，创建对象并添加到列表中
for i in range(100_000):
    # 向列表中添加一个包含索引和数据的字典对象
    objs.append({"index": i, "data": "x" * 100})
    # 每当对象数为2万的倍数时，打印当前内存使用情况
    if (i + 1) % 20_000 == 0:
        # 获取当前内存使用情况
        current = process.memory_info().rss / 1024 / 1024
        # 打印当前已创建对象数量和内存使用情况
        print(f"创建{i+1}个对象, 当前内存: {current:.2f} MB")

# 打印持有所有对象后的内存使用情况
print(f"持有全部对象后内存: {process.memory_info().rss / 1024 / 1024:.2f} MB")

# 删除所有对象
del objs
# 手动进行垃圾回收
print(gc.collect())

# 打印垃圾回收后内存使用情况
print(f"清理后内存: {process.memory_info().rss / 1024 / 1024:.2f} MB")



# 导入gc模块，用于垃圾回收操作
import gc

# 创建一个空列表用于保存对象，制造垃圾对象
objs = []
# 循环1万次，制造多个带有循环引用的对象
for i in range(10000):
    # 创建一个只包含当前索引的列表
    a = [i]
    # 将自己追加到自己的末尾，形成循环引用
    a.append(a)  # 人为制造循环引用
    # 将创建的列表对象添加到objs列表
    objs.append(a)
# 删除_objs_列表的引用，准备进行垃圾回收
del objs

# 强制进行一次垃圾回收，返回不可达对象的数量
unreachable = gc.collect()
# 输出本次垃圾回收中不可达对象的数量
print(f"不可达对象数量: {unreachable}")


# 导入tracemalloc模块，用于跟踪内存分配
import tracemalloc

# 启动内存分配跟踪
tracemalloc.start()

# 分配一组大的bytearray对象，模拟可能产生内存泄漏的操作
data = [bytearray(100000) for _ in range(1000)]

# 捕获当前的内存分配快照
snapshot = tracemalloc.take_snapshot()
# 统计每一行代码的内存分配情况
top_stats = snapshot.statistics("lineno")

# 输出“Top 5 内存分配位置：”
print("Top 5 内存分配位置：")
# 遍历前5个分配内存最多的代码位置
for stat in top_stats[:5]:
    # 打印每个分配位置的信息
    print(stat)

# 传统列表方式
import sys


def create_list(n):
    # 创建包含n个元素的列表
    return [i**2 for i in range(n)]


# 生成器方式
def create_generator(n):
    # 创建生成器，逐个产生元素
    for i in range(n):
        yield i**2


# 比较内存使用
n = 100000

# 列表方式
my_list = create_list(n)
list_memory = sys.getsizeof(my_list)
print(f"列表内存使用: {list_memory} 字节")

# 生成器方式
my_generator = create_generator(n)
generator_memory = sys.getsizeof(my_generator)
print(f"生成器内存使用: {generator_memory} 字节")

# 计算内存节省
memory_saved = list_memory - generator_memory
print(f"内存节省: {memory_saved} 字节 ({memory_saved/list_memory*100:.1f}%)")

# 演示生成器的使用
print("\n生成器使用示例:")
gen = create_generator(10)
for i, value in enumerate(gen):
    print(f"第{i+1}个值: {value}")
    if i >= 4:  # 只取前5个值
        break

# 清理
del my_list, my_generator


# 那生成器最后变成列表  不是每个生成器都会变成列表的
# JS V8 垃圾回收机制
# STOP WORLD




# 垃圾回收机制
import gc


# 获取垃圾回收统计信息
def show_gc_stats():
    # 获取各代的对象数量和回收统计
    stats = gc.get_stats()
    print("垃圾回收统计信息:")
    for i, stat in enumerate(stats):
        print(f"  第{i}代: {stat}")


# 显示初始状态
print("初始垃圾回收状态:")
show_gc_stats()


# 创建循环引用
def create_circular_reference():
    # 创建两个对象
    obj1 = []
    obj2 = []
    # 形成循环引用
    obj1.append(obj2)
    obj2.append(obj1)
    return obj1, obj2


# 创建循环引用但不保存引用
create_circular_reference()
print("\n创建循环引用后:")
show_gc_stats()

# 手动触发垃圾回收
collected = gc.collect()
print(f"\n手动垃圾回收回收了 {collected} 个对象")

# 显示回收后状态
print("垃圾回收后状态:")
show_gc_stats()


# 循环引用问题演示
import gc
import sys


class Node:
    def __init__(self, value):
        # 初始化节点值
        self.value = value
        # 父节点引用
        self.parent = None
        # 子节点列表
        self.children = []

    def add_child(self, child):
        # 添加子节点
        self.children.append(child)
        # 设置子节点的父节点
        child.parent = self

    def __del__(self):
        # 析构函数，用于观察对象销毁
        print(f"节点 {self.value} 被销毁")


# 创建循环引用的节点
print("1. 创建循环引用的节点:")
parent = Node("父节点")
child1 = Node("子节点1")
child2 = Node("子节点2")

# 建立循环引用关系
parent.add_child(child1)
parent.add_child(child2)

print(f"父节点引用计数: {sys.getrefcount(parent)-1}")
print(f"子节点1引用计数: {sys.getrefcount(child1)-1}")
print(f"子节点2引用计数: {sys.getrefcount(child2)-1}")

# 删除外部引用
print("\n2. 删除外部引用:")
del parent, child1, child2

# 检查垃圾回收器状态
print("垃圾回收器追踪的对象数量:", len(gc.get_objects()))

# 手动触发垃圾回收
print("\n3. 手动触发垃圾回收:")
collected = gc.collect()
print(f"回收了 {collected} 个对象")

# 再次检查对象数量
print("垃圾回收后对象数量:", len(gc.get_objects()))


# 使用弱引用解决循环引用问题
import gc
import sys
import weakref


class Node:

    def __init__(self, value):
        # 初始化节点值
        self.value = value
        # 使用弱引用存储父节点
        self._parent = None
        # 子节点列表
        self.children = []

    @property
    def parent(self):
        # 获取父节点（弱引用）
        return self._parent()

    @parent.setter
    def parent(self, parent_node):
        # 设置父节点（弱引用）
        self._parent = weakref.ref(parent_node)

    def add_child(self, child):
        # 添加子节点
        self.children.append(child)
        # 设置子节点的父节点（弱引用）
        child.parent = self

    def __del__(self):
        # 析构函数
        print(f"节点 {self.value} 被销毁")


# 创建使用弱引用的节点
print("1. 创建使用弱引用的节点:")
parent = Node("父节点")
child = Node("子节点")

# 建立关系
parent.add_child(child)

print(f"父节点引用计数: {sys.getrefcount(parent)-1}")
print(f"子节点引用计数: {sys.getrefcount(child)-1}")

# 删除父节点引用
print("\n2. 删除父节点引用:")
del parent

# 检查子节点是否还能访问父节点
print(f"子节点还能访问父节点: {child.parent is not None}")

# 删除子节点引用
print("\n3. 删除子节点引用:")
del child

# 手动触发垃圾回收
collected = gc.collect()
print(f"回收了 {collected} 个对象")
"""


# 模拟C库内存分配
class CMemoryManager:
    """模拟C库内存管理器"""

    def __init__(self):
        # 记录分配的内存块
        self.allocated_blocks = []
        print("C库内存管理器初始化")

    def allocate(self, size):
        # 模拟C库分配内存
        block = bytearray(size)
        self.allocated_blocks.append(block)
        print(f"C库分配了 {size} 字节内存，当前分配块数: {len(self.allocated_blocks)}")
        return block

    def deallocate(self, block):
        # 模拟C库释放内存
        if block in self.allocated_blocks:
            self.allocated_blocks.remove(block)
            print(f"C库释放了内存块，剩余块数: {len(self.allocated_blocks)}")
        else:
            print("尝试释放未分配的内存块")

    def cleanup(self):
        # 清理所有分配的内存
        print(f"C库清理 {len(self.allocated_blocks)} 个内存块")
        self.allocated_blocks.clear()


# 创建C库内存管理器
c_manager = CMemoryManager()

# 分配一些内存
print("\n1. 分配C库内存:")
block1 = c_manager.allocate(1024)  # 1KB
block2 = c_manager.allocate(2048)  # 2KB
block3 = c_manager.allocate(512)  # 512B

# 释放部分内存
print("\n2. 释放部分内存:")
c_manager.deallocate(block2)

# 模拟程序退出时的情况
print("\n3. 程序退出时的清理:")
# 如果没有显式调用cleanup，C库内存可能不会被释放
# c_manager.cleanup()  # 注释掉这行来模拟内存泄漏

# 删除Python引用
del c_manager, block1, block3

print("Python对象已删除，但C库内存可能仍然存在")
