def find_candidate(mro_lists, debug=False):
    """
    从MRO列表中查找符合条件的候选类
    候选类的条件：
    1.出现在某个列表的头部
    2.不能出现在其它一表非头部的位置
    """
    for mro_list in mro_lists:
        # 跳过空列表
        if not mro_list:
            continue
        # 获取第一个列表的第一个类作为候选类
        candidate = mro_list[0]
        # 是否合法
        is_valid = True
        #
        for other_list in mro_lists:
            # 如果候选类出现在任何其它列表的非头部的位置
            if candidate in other_list[1:]:
                is_valid = False
                break
        # 如果没有冲突，则返回该候选类
        if is_valid:
            return candidate
    # 如果没有找到任何满足条件的候选类，是返回None
    return None


# 合并多个MRO列表，按照C3算法规则
def merge_mro_lists(mro_lists, debug=False):
    """
    合并多个MRO列表
    算法规则如下：
    1.从第一个列表的第一个元素开始检查
    2.如果某个类在所有的列表中都出现在第一个位置，就可以该类添加到结果中并从所有的列表移除
    3.重复直到所有的列表都为空为止
    """
    # 初始化结果列表
    result = []
    # 循环直到所有的MRO列表被处理完为止
    while any(mro_lists):
        if debug:
            print(
                f"当前所有的 MRO列表:{[ [c.__name__ for c in mro] for mro in mro_lists]}"
            )
        # 查找下一个满足C3规则的候选类
        candidate = find_candidate(mro_lists, debug)
        if candidate is None:
            raise TypeError("无法创建一致性的MRO，存在继承冲突")
        # 把该 候选类添加到结果 列表中
        result.append(candidate)
        if debug:
            print(f"选择候选类:{candidate.__name__}")
        # 从所有的MRO列表的开头位置移除候选类
        for mro_list in mro_lists:
            if mro_list and mro_list[0] == candidate:
                mro_list.pop(0)
        # 移除所有的已经为空的mro列表
        mro_lists = [lst for lst in mro_lists if lst]
    return result


def c3_mro_algorithm(cls, debug=False):
    """
    C3线性化算法
    参数：
       cls: 要计算MRO的类
       debug:是否显示调试信息
    返回:
       该类的MRO列表
    """
    # 如果当前的类是object,直接返回[object]
    if cls is object:
        return [object]
    if debug:
        print(f"计算{cls.__name__}的MRO:")
    # 创建一个空的列表，用于存储所有父类的MRO
    bases_mros = []
    # 遍历当前类所有的直接的父类
    for base in cls.__bases__:
        # 递归计算父类的MRO列表
        base_mro = c3_mro_algorithm(base, debug)
        # 添加该父类的MRO到列表中
        bases_mros.append(base_mro)
        if debug:
            print(
                f"{cls.__name__}的父类{base.__name__}的MRO：{[c.__name__ for c in base_mro]}"
            )
    bases_mros.insert(0, [cls])
    if debug:
        print(f"所有的 MRO列表:{[ [c.__name__ for c in mro] for mro in bases_mros]}")
    result = merge_mro_lists(bases_mros, debug)
    if debug:
        print(f"{cls.__name__}的最终的MRO为:{[c.__name__ for c in result]}")
    return result


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print("D mro", [cls.__name__ for cls in D.mro()])
print("D mro", [cls.__name__ for cls in c3_mro_algorithm(D, True)])
