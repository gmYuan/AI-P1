class DeepCopy:
    def __init__(self):
        self.memo = {}  # 记录已拷贝的对象，用于处理循环引用

    def deepcopy(self, x):
        self.memo = {}
        return self._deepcopy_dispatch(x)

    def _deepcopy_dispatch(self, x):
        """根据类型分发到不同的拷贝方法"""
        if type(x) in (int, float, str, type(None), bool):
            return x
        # 处理循环引用 如果已经是拷贝过的对象的话，可以直接引用
        if id(x) in self.memo:
            return self.memo[id(x)]
        # 默认使用通用的拷贝方法
        return self._deepcopy_generic(x)

    def _deepcopy_generic(self, x):
        try:
            # 尝试使用对象自己的__deepcopy__方法
            return x.__deepcopy__(self.memo)
        except AttributeError:
            pass
        # 创建新的实例 list dict set
        cls = type(x)
        result = cls.__new__(cls)  #  new Function()   new Object() new
        # 把拷贝后创建的新的对象和老的ID值进行关联
        self.memo[id(x)] = result
        # 把x上所有的属性拷贝到新的result对象上
        if hasattr(x, "__dict__"):  # setAttrbute getAttribute hasAttribute
            for attr, value in x.__dict__.items():
                setattr(result, attr, self._deepcopy_dispatch(value))
        return result


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


root = Node("根节点")
child1 = Node("子节点1")
child2 = Node("子节点2")
root.add_child(child1)
root.add_child(child2)
print(root.children)
print(child1.parent.value)

try:
    deep_copy = DeepCopy().deepcopy(root)
    print(id(root))
    print(root)
    print(id(deep_copy))
    print(deep_copy)
except Exception as e:
    print("拷贝失败")
    # list set dict .copy
