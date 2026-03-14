def deepCopy(obj, memo=None):
    # 存放着已经拷贝过的对象 key 被 拷贝对象的内存ID，值拷贝出来的新的对象
    if memo is None:
        memo = {}
    # 如果对象已经被 拷贝过，直接返回拷贝后的对象
    if id(obj) in memo:
        return memo[id(obj)]
    if isinstance(obj, list):
        copy_list = []
        memo[id(obj)] = copy_list
        copy_list.extend(deepCopy(item, memo) for item in obj)
        return copy_list
    elif isinstance(obj, tuple):
        copy_tuple = tuple(deepCopy(item, memo) for item in obj)
        memo[id(obj)] = copy_tuple
        return copy_tuple
    elif isinstance(obj, dict):
        copy_dict = {}
        memo[id(obj)] = copy_dict
        for key, value in obj.items():
            copy_dict[deepCopy(key, memo)] = deepCopy(value, memo)
        return copy_dict
    elif isinstance(obj, set):
        copy_set = set()
        memo[id(obj)] = copy_set
        for item in obj:
            copy_set.add(deepCopy(item, memo))
        return copy_set
    # 如果有__dict__属性的话说明obj是类的实例
    elif hasattr(obj, "__dict__"):
        # 创建新的实例，但不调用__init__
        copy_obj = obj.__class__.__new__(obj.__class__)
        memo[id(obj)] = copy_obj
        # 拷贝所有的属性
        for attr_name, attr_value in obj.__dict__.items():
            setattr(copy_obj, attr_name, deepCopy(attr_value, memo))
        # 如果有自定义__deepcopy__的话，优先使用
        if hasattr(obj, "__deepcopy__"):
            return obj.__deepcopy__(memo)
        return copy_obj
    else:
        return obj


class Node:
    def __init__(self, name):
        self.name = name

    def add_friend(self, friend):
        self.friend = friend

    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]
        copy_obj = self.__class__.__new__(self.__class__)
        memo[id(self)] = copy_obj
        copy_obj.value = deepCopy(self.value, memo)
        copy_obj.parent = deepCopy(self.parent, memo)
        copy_obj.children = deepCopy(self.children, memo)
        return copy_obj


node1 = Node("节点1 ")
node2 = Node("节点2")
node1.add_friend(node2)
node2.add_friend(node1)
newnode1 = deepCopy(node1)
newnode2 = newnode1.friend
print(newnode1.name)
print(newnode2.name)
