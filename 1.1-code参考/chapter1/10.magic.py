"""
class CustomResource:
    def __init__(self, name):
        self.name = name
        self.is_acuiqred = False

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
        return False

    def acquire(self):
        if self.is_acuiqred:
            raise RuntimeError(f"资源{self.name}已经获取")
        self.is_acuiqred = True
        print(f"资源已经成功获取")

    def use(self):
        if not self.is_acuiqred:
            raise RuntimeError(f"资源{self.name}尚未获取")
        print(f"正在使用资源")

    def release(self):
        if not self.is_acuiqred:
            raise RuntimeError(f"资源{self.name}尚未获取")
        self.is_acuiqred = False
        print(f"资源已经成功释放")


with CustomResource("数据库资源") as resource:
    resource.use()
    print("执行数据库操作")



class FileManager:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"文件{self.filename}已经打开")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"文件已经关闭")
        if exc_type:
            print(f"发生异常，{exc_type.__name__} :{exc_val}")
        return False


try:
    with FileManager("test.txt", "r") as file:
        # file.write("hello")
        raise RuntimeError("发生运行进异常")
        print("文件读取完成")
except FileNotFoundError as e:
    print(f"文件操作失败:{e}")



class CustomList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)


c1 = CustomList()
c1.append(1)
c1.append(2)
c1.append(3)
print(f"列表的长度:{len(c1)}")
print(f"索引为0的元素:{c1[0]}")
print(f"索引为1的元素:{c1[1]}")

c1[1] = 10

for item in c1:
    print(f"{item}")

del c1[0]

if 10 in c1:
    print("10在c1里")



# 定义一个自定义字典类
class CustomDict(dict):
    pass


# 创建自定义字典
cd = CustomDict()
# 添加键值对
cd["name"] = "Alice"
cd["age"] = 30
cd["city"] = "New York"
# 测试字典操作
print(f"字典长度: {len(cd)}")
print(f"name的值: {cd['name']}")
print(f"age的值: {cd['age']}")
# 测试成员测试
print(f"'name' 在字典中: {'name' in cd}")
print(f"'salary' 在字典中: {'salary' in cd}")
# 测试迭代
print("字典键值对:")
# for in循环需要一个可迭代对象，内部会动调用iter得到迭代器进行迭代
# 可迭代对象是不需要有next方法的，但是返回的迭代器是需要有next方法的
for key, value in cd.items():
    print(f"  {key}: {value}")
# 删除键
del cd["city"]
print(f"删除'city'后: {cd}")



class Callable:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, value):
        return self.multiplier * value


multiplier = Callable(5)
# TypeError: 'Callable' object is not callable
result1 = multiplier(10)
print(result1)
"""


class Attribute:
    def __init__(self):
        self._private_data = {}

    def __setattr__(self, name, value):
        print(f"设置属性:{name}={value}")
        super().__setattr__(name, value)

    # 优先级是最最低的，只有其它查找属性都失败的失败的情况下才会走到这
    def __getattr__(self, name):
        print(f"访问不存在的属性{name}")
        return None

    #    def __hasattr__(self, name):
    #        # hasattr是一个内置函数
    #        return hasattr(self, name)

    def __delattr__(self, name):
        print(f"删除属性{name}")
        super().__delattr__(name)

    def __contains__(self, item):
        return True


print(Attribute.__bases__)  # (<class 'object'>,)
obj = Attribute()
obj.name = "Alice"
obj.age = 30
obj.home = "北京"
print(obj.name)
print(obj.age)
print(obj.salary)  # AttributeError: 'Attribute' object has no attribute 'salary'
del obj.age
if "name" in obj:
    print("存在name")

# 属性查找优先级
#
# 数据描述符的__get__（定义了 __set__）
# 实例字典（instance.__dict__）
# 非数据描述符（仅有 __get__）
# 类字典/父类字典
# __getattr__
