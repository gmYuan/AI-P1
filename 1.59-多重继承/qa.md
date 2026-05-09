

计算A的MRO:
bases_mros=[['A'], ['object']]
['A','object]
计算B的MRO:
bases_mros=[['B'], ['object']]
['B','object]

计算C的MRO:

bases_mros=[]
result=['C','A','B','object']


# 从左到右，深度优先，留住顶端