"""


# 定义一个名为 Duck 的类
class Duck:
    # 定义 Duck 类

    def __init__(self, name):
        # 构造函数，用于初始化鸭子
        # self 是实例本身
        # name 是鸭子的名字
        self.name = name
        # 设置鸭子名字

    def quack(self):
        # 定义 Duck 类的一个方法 quack
        # self 是实例本身
        print(f"{self.name} 说: Quack!")
        # 打印鸭子的叫声

    def walk(self):
        # 定义 Duck 类的一个方法 walk
        # self 是实例本身
        print(f"{self.name} 正在走路")
        # 打印鸭子走路的信息


# 定义一个名为 Person 的类
class Person:
    # 定义 Person 类

    def __init__(self, name):
        # 构造函数，用于初始化人
        # self 是实例本身
        # name 是人的名字
        self.name = name
        # 设置人的名字

    def quack(self):
        # 定义 Person 类的一个方法 quack
        # self 是实例本身
        print(f"{self.name} 模仿鸭子说: Quack!")
        # 打印人模仿鸭子的叫声

    def walk(self):
        # 定义 Person 类的一个方法 walk
        # self 是实例本身
        print(f"{self.name} 正在走路")
        # 打印人走路的信息


# 定义一个名为 Robot 的类
class Robot:
    # 定义 Robot 类

    def __init__(self, name):
        # 构造函数，用于初始化机器人
        # self 是实例本身
        # name 是机器人的名字
        self.name = name
        # 设置机器人的名字

    def quack(self):
        # 定义 Robot 类的一个方法 quack
        # self 是实例本身
        print(f"{self.name} 发出电子声音: Quack!")
        # 打印机器人模仿鸭子的叫声

    def walk(self):
        # 定义 Robot 类的一个方法 walk
        # self 是实例本身
        print(f"{self.name} 正在移动")
        # 打印机器人移动的信息


# 定义一个函数 make_it_quack，它接受一个参数 duck_like
# 这个函数不关心 duck_like 的具体类型，只关心它是否有 quack 方法
def make_it_quack(duck_like):
    # 定义一个函数，用于让对象发出叫声
    # duck_like 是任何具有 quack 方法的对象
    duck_like.quack()
    # 调用传入对象的 quack 方法


# 定义一个函数 make_it_walk，它接受一个参数 walkable
# 这个函数不关心 walkable 的具体类型，只关心它是否有 walk 方法
def make_it_walk(walkable):
    # 定义一个函数，用于让对象走路
    # walkable 是任何具有 walk 方法的对象
    walkable.walk()
    # 调用传入对象的 walk 方法


# 创建 Duck 类的一个实例
my_duck = Duck("小黄鸭")
# 创建 Person 类的一个实例
my_person = Person("小明")
# 创建 Robot 类的一个实例
my_robot = Robot("机器人A")

# 调用 make_it_quack 函数，传入 Duck 实例
# 此时会调用 Duck 实例的 quack 方法
print("--- 调用 make_it_quack(my_duck) ---")
make_it_quack(my_duck)
# 预期输出: 小黄鸭 说: Quack!

# 调用 make_it_quack 函数，传入 Person 实例
# 此时会调用 Person 实例的 quack 方法
print("\n--- 调用 make_it_quack(my_person) ---")
make_it_quack(my_person)
# 预期输出: 小明 模仿鸭子说: Quack!

# 调用 make_it_quack 函数，传入 Robot 实例
# 此时会调用 Robot 实例的 quack 方法
print("\n--- 调用 make_it_quack(my_robot) ---")
make_it_quack(my_robot)
# 预期输出: 机器人A 发出电子声音: Quack!

# 调用 make_it_walk 函数，传入不同的对象
print("\n--- 调用 make_it_walk 函数 ---")
make_it_walk(my_duck)
# 预期输出: 小黄鸭 正在走路
make_it_walk(my_person)
# 预期输出: 小明 正在走路
make_it_walk(my_robot)
# 预期输出: 机器人A 正在移动


# 尝试创建一个没有 quack 方法的类
class Stone:
    # 定义 Stone 类

    def __init__(self, name):
        # 构造函数，用于初始化石头
        # self 是实例本身
        # name 是石头的名字
        self.name = name
        # 设置石头的名字

    def roll(self):
        # 定义 Stone 类的一个方法 roll
        # self 是实例本身
        print(f"{self.name} 正在滚动")
        # 打印石头滚动的信息


# 创建 Stone 类的一个实例
my_stone = Stone("大石头")

# 尝试将 Stone 实例传入 make_it_quack 函数
# 这将导致 AttributeError，因为 Stone 没有 quack 方法
print("\n--- 调用 make_it_quack(my_stone) (预期会报错) ---")
try:
    make_it_quack(my_stone)
except AttributeError as e:
    # 捕获并打印错误信息
    print(f"错误: {e} - Stone 对象没有 'quack' 方法，符合鸭子类型原则。")


# 定义一个名为 Animal 的抽象基类
from abc import ABC, abstractmethod


class Animal(ABC):
    # 定义 Animal 抽象基类

    @abstractmethod
    def make_sound(self):
        # 抽象方法，子类必须实现
        # self 是实例本身
        pass
        # pass 表示此抽象方法在此处没有实现

    @abstractmethod
    def move(self):
        # 抽象方法，子类必须实现
        # self 是实例本身
        pass
        # pass 表示此抽象方法在此处没有实现


# 定义一个名为 Dog 的类，继承自 Animal
class Dog(Animal):
    # 定义 Dog 类，继承自 Animal

    def make_sound(self):
        # 实现抽象方法 make_sound
        # self 是实例本身
        print("汪汪!")
        # 打印狗的叫声

    def move(self):
        # 实现抽象方法 move
        # self 是实例本身
        print("狗在跑步")
        # 打印狗的运动方式


# 定义一个名为 Cat 的类，继承自 Animal
class Cat(Animal):
    # 定义 Cat 类，继承自 Animal

    def make_sound(self):
        # 实现抽象方法 make_sound
        # self 是实例本身
        print("喵喵!")
        # 打印猫的叫声

    def move(self):
        # 实现抽象方法 move
        # self 是实例本身
        print("猫在走路")
        # 打印猫的运动方式


# 定义一个名为 Car 的类，不继承自 Animal
class Car:
    # 定义 Car 类

    def make_sound(self):
        # 定义 Car 类的一个方法 make_sound
        # self 是实例本身
        print("汽车发出引擎声")
        # 打印汽车的声音

    def move(self):
        # 定义 Car 类的一个方法 move
        # self 是实例本身
        print("汽车在行驶")
        # 打印汽车的运动方式


# 定义一个函数，接受 Animal 类型的对象
def animal_behavior(animal):
    if not isinstance(animal, Animal):
        raise TypeError("不是 Animal 类型")
    # 定义一个函数，用于处理动物行为
    # animal 是 Animal 类型的对象
    animal.make_sound()
    # 调用传入对象的 make_sound 方法
    animal.move()
    # 调用传入对象的 move 方法


# 定义一个函数，接受任何具有 make_sound 和 move 方法的对象
def duck_typing_behavior(obj):
    # 定义一个函数，用于处理任何具有相应方法的对象
    # obj 是任何具有 make_sound 和 move 方法的对象
    obj.make_sound()
    # 调用传入对象的 make_sound 方法
    obj.move()
    # 调用传入对象的 move 方法


# 创建不同类型的对象
dog = Dog()
# 创建 Dog 类的实例
cat = Cat()
# 创建 Cat 类的实例
car = Car()
# 创建 Car 类的实例

# 使用静态类型方式（需要继承关系）
print("--- 静态类型方式（需要继承关系）---")
animal_behavior(dog)
# 预期输出: 汪汪! 狗在跑步
animal_behavior(cat)
# 预期输出: 喵喵! 猫在走路

# 尝试将 Car 对象传入 animal_behavior 函数会报错
# 因为 Car 不继承自 Animal
try:
    animal_behavior(car)
except TypeError as e:
    # 捕获并打印错误信息
    print(f"错误: {e} - Car 对象不是 Animal 类型")

# 使用鸭子类型方式（不需要继承关系）
print("\n--- 鸭子类型方式（不需要继承关系）---")
duck_typing_behavior(dog)
# 预期输出: 汪汪! 狗在跑步
duck_typing_behavior(cat)
# 预期输出: 喵喵! 猫在走路
duck_typing_behavior(car)
# 预期输出: 汽车发出引擎声 汽车在行驶


# 创建一个具有相同方法的对象
class Train:
    # 定义 Train 类

    def make_sound(self):
        # 定义 Train 类的一个方法 make_sound
        # self 是实例本身
        print("火车发出汽笛声")
        # 打印火车的声音

    def move(self):
        # 定义 Train 类的一个方法 move
        # self 是实例本身
        print("火车在铁轨上行驶")
        # 打印火车的运动方式


# 创建 Train 类的实例
train = Train()
# 使用鸭子类型方式处理 Train 对象
duck_typing_behavior(train)
# 预期输出: 火车发出汽笛声 火车在铁轨上行驶



# 1. 迭代器协议 - 鸭子类型的经典应用
class MyIterator:
    # 定义一个自定义迭代器类

    def __init__(self, data):
        # 构造函数，用于初始化迭代器
        # self 是实例本身
        # data 是要迭代的数据
        self.data = data
        # 设置要迭代的数据
        self.index = 0
        # 初始化索引

    def __iter__(self):
        # 实现迭代器协议的 __iter__ 方法
        # self 是实例本身
        return self
        # 返回迭代器自身

    def __next__(self):
        # 实现迭代器协议的 __next__ 方法
        # self 是实例本身
        if self.index < len(self.data):
            # 如果索引在数据范围内
            result = self.data[self.index]
            # 获取当前索引位置的值
            self.index += 1
            # 索引递增
            return result
            # 返回当前值
        else:
            # 如果索引超出数据范围
            raise StopIteration
            # 抛出 StopIteration 异常


# 创建一个自定义迭代器实例
my_iter = MyIterator([1, 2, 3, 4, 5])
# 使用 for 循环遍历迭代器
print("--- 自定义迭代器示例 ---")
# for item in my_iter:
# 遍历迭代器
#    print(item)
# 打印当前项

it = iter(my_iter)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break



# 2. 文件对象 - 鸭子类型的应用
class StringIO:
    # 定义一个模拟文件对象的类

    def __init__(self, content):
        # 构造函数，用于初始化字符串IO对象
        # self 是实例本身
        # content 是初始内容
        self.content = content
        # 设置内容
        self.position = 0
        # 初始化位置

    def read(self, size=-1):
        # 定义 read 方法，模拟文件读取
        # self 是实例本身
        # size 是要读取的字节数
        if size == -1:
            # 如果 size 为 -1，读取所有内容
            result = self.content[self.position :]
            # 获取从当前位置到末尾的内容
            self.position = len(self.content)
            # 设置位置到末尾
        else:
            # 如果 size 不为 -1，读取指定字节数
            result = self.content[self.position : self.position + size]
            # 获取指定长度的内容
            self.position += size
            # 位置递增
        return result
        # 返回读取的内容

    def write(self, data):
        # 定义 write 方法，模拟文件写入
        # self 是实例本身
        # data 是要写入的数据
        self.content += data
        # 将数据添加到内容中
        return len(data)
        # 返回写入的字节数

    def close(self):
        # 定义 close 方法，模拟文件关闭
        # self 是实例本身
        print("文件已关闭")
        # 打印文件关闭信息


# 创建一个字符串IO对象
string_io = StringIO("Hello")
string_io.write("world")
# 读取内容
content = string_io.read()
# 打印读取的内容
print(f"\n--- 字符串IO示例 ---")
print(f"读取的内容: {content}")
string_io.close()
# 预期输出: 读取的内容: Hello, World!
"""


# 1. 插件系统 - 鸭子类型的应用
class Plugin:
    # 定义一个插件基类

    def __init__(self, name):
        # 构造函数，用于初始化插件
        # self 是实例本身
        # name 是插件的名字
        self.name = name
        # 设置插件名字

    def execute(self):
        # 定义 execute 方法，子类应该重写
        # self 是实例本身
        print(f"插件 {self.name} 执行默认操作")
        # 打印默认操作信息


class TextPlugin(Plugin):
    # 定义一个文本插件类

    def execute(self):
        # 重写 execute 方法
        # self 是实例本身
        print(f"文本插件 {self.name} 正在处理文本")
        # 打印文本处理信息


class ImagePlugin(Plugin):
    # 定义一个图像插件类

    def execute(self):
        # 重写 execute 方法
        # self 是实例本身
        print(f"图像插件 {self.name} 正在处理图像")
        # 打印图像处理信息


class CustomPlugin:
    # 定义一个自定义插件类（不继承自 Plugin）

    def __init__(self, name):
        # 构造函数，用于初始化自定义插件
        # self 是实例本身
        # name 是插件的名字
        self.name = name
        # 设置插件名字

    def execute(self):
        # 定义 execute 方法
        # self 是实例本身
        print(f"自定义插件 {self.name} 正在执行特殊操作")
        # 打印特殊操作信息


class PluginManager:
    # 定义一个插件管理器类

    def __init__(self):
        # 构造函数，用于初始化插件管理器
        # self 是实例本身
        self.plugins = []
        # 初始化插件列表

    def register_plugin(self, plugin):
        # 定义一个方法，用于注册插件
        # self 是实例本身
        # plugin 是任何具有 execute 方法的对象
        self.plugins.append(plugin)
        # 将插件添加到列表中

    def run_all_plugins(self):
        # 定义一个方法，用于运行所有插件
        # self 是实例本身
        for plugin in self.plugins:
            # 遍历插件列表
            plugin.execute()
            # 调用插件的 execute 方法


# 创建插件管理器
plugin_manager = PluginManager()
# 注册不同类型的插件
plugin_manager.register_plugin(TextPlugin("文本处理"))
# 注册文本插件
plugin_manager.register_plugin(ImagePlugin("图像处理"))
# 注册图像插件
plugin_manager.register_plugin(CustomPlugin("自定义处理"))
# 注册自定义插件

# 运行所有插件
plugin_manager.run_all_plugins()
# 预期输出:
# 文本插件 文本处理 正在处理文本
# 图像插件 图像处理 正在处理图像
# 自定义插件 自定义处理 正在执行特殊操作
