# 创建一个初始列表
# 创建一个包含三个元素的列表
"""
my_list = [1, 2, 3]

# 使用append添加单个元素
# 在列表末尾添加数字4
my_list.append(4)
print(f"添加数字后: {my_list}")  # 输出: [1, 2, 3, 4]

# 添加不同类型的元素
# 添加字符串元素
my_list.append("hello")
print(f"添加字符串后: {my_list}")  # 输出: [1, 2, 3, 4, 'hello']

# 添加列表元素（作为整体）
# 将整个列表作为一个元素添加
my_list.append([5, 6])
print(f"添加列表后: {my_list}")  # 输出: [1, 2, 3, 4, 'hello', [5, 6]]

# 添加元组元素
# 将元组作为一个元素添加
my_list.append((7, 8))
print(f"添加元组后: {my_list}")  # 输出: [1, 2, 3, 4, 'hello', [5, 6], (7, 8)]


# 从文件逐行读取数据并添加到列表
file_lines = []
# 模拟文件内容
file_content = ["第一行", "第二行", "第三行"]

# 逐行添加到列表
# 遍历文件内容并逐行添加
for line in file_content:
    file_lines.append(line.strip())

print(f"文件内容列表: {file_lines}")

# 收集用户输入的数据
user_inputs = []
# 模拟用户输入
inputs = ["张三", "25", "北京", "工程师"]

# 收集用户输入
# 将每个用户输入添加到列表
for user_input in inputs:
    user_inputs.append(user_input)

print(f"用户输入列表: {user_inputs}")

# 根据条件动态添加元素
numbers = []
# 模拟根据条件添加数字
for i in range(1, 11):
    if i % 2 == 0:  # 只添加偶数
        numbers.append(i)

print(f"偶数列表: {numbers}")


# 功能描述： insert方法用于在列表的指定位置插入一个元素，需要两个参数：插入位置的索引和要插入的元素。
# 创建一个初始列表
# 创建一个包含三个元素的列表
my_list = [1, 2, 3]

# 在指定位置插入元素
# 在索引1的位置插入字符'a'
my_list.insert(1, "a")
print(f"插入字符后: {my_list}")  # 输出: [1, 'a', 2, 3]

# 在列表开头插入元素
# 在索引0的位置插入元素（列表开头）
my_list.insert(0, "start")
print(f"在开头插入后: {my_list}")  # 输出: ['start', 1, 'a', 2, 3]

# 在列表末尾插入元素（等同于append）
# 使用insert在末尾插入元素
my_list.insert(len(my_list), "end")
print(f"在末尾插入后: {my_list}")  # 输出: ['start', 1, 'a', 2, 3, 'end']

# 插入复杂数据类型
# 在指定位置插入列表
my_list.insert(2, [4, 5, 6])
print(f"插入列表后: {my_list}")  # 输出: ['start', 1, [4, 5, 6], 'a', 2, 3, 'end']


# 在有序列表中插入新元素并保持顺序
sorted_list = [1, 3, 5, 7, 9]
new_number = 4

# 找到合适的插入位置
# 遍历列表找到插入位置
insert_position = 0
for i, num in enumerate(sorted_list):
    if new_number < num:
        insert_position = i
        break
    insert_position = i + 1

# 在合适位置插入新元素
sorted_list.insert(insert_position, new_number)
print(f"插入后的有序列表: {sorted_list}")


# 创建一个空的优先级队列列表
priority_queue = []
# 定义待插入的任务列表，每项为(优先级, 任务描述)
tasks = [(3, "低优先级任务"), (1, "高优先级任务"), (2, "中优先级任务")]
# [3] [1,3] [1,2,3]
# 遍历每一个任务及其优先级
for priority, task in tasks:
    # 初始化插入位置为0
    insert_pos = 0
    # 遍历当前队列中的任务
    for i, (existing_priority, _) in enumerate(priority_queue):
        # 如果当前任务优先级高于正在比较的任务（数字越小优先级越高）
        if priority < existing_priority:
            # 记录插入位置
            insert_pos = i
            # 找到位置后跳出循环
            break
        # 否则将插入位置移动到下一个
        insert_pos = i + 1

    # 将当前任务插入到相应的位置，保证队列有序
    priority_queue.insert(insert_pos, (priority, task))

# 打印优先级队列内容
print("优先级队列:")
# 遍历并打印队列中的每一个任务及其优先级
for priority, task in priority_queue:
    print(f"  优先级 {priority}: {task}")


# 管理历史记录，新记录插入到开头
history = ["记录5", "记录4", "记录3", "记录2", "记录1"]
new_record = "新记录"

# 将新记录插入到开头
history.insert(0, new_record)
print(f"更新后的历史记录: {history}")

# 限制历史记录长度
# 如果历史记录过长，删除最后一个
if len(history) > 5:
    history.pop()  # 删除最后一个元素

print(f"限制长度后的历史记录: {history}")



"""

# 创建一个初始列表
# 创建一个包含三个元素的列表
my_list = [1, 2, 3]

# 使用extend添加另一个列表的所有元素
# 将另一个列表的所有元素添加到当前列表
my_list.extend([4, 5, 6])
print(f"扩展列表后: {my_list}")  # 输出: [1, 2, 3, 4, 5, 6]

# 扩展不同类型的可迭代对象
# 扩展元组
my_list.extend((7, 8, 9))
print(f"扩展元组后: {my_list}")  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 扩展字符串（每个字符作为单独元素）
# 将字符串的每个字符作为单独元素添加
my_list.extend("abc")
print(f"扩展字符串后: {my_list}")  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c']

# 扩展生成器
# 扩展生成器表达式的结果
my_list.extend(range(10, 13))
print(
    f"扩展生成器后: {my_list}"
)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 10, 11, 12]

# 扩展集合的所有元素
my_list.extend({13, 14, 15})
print(
    f"扩展集合后: {my_list}"
)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 10, 11, 12, 13, 14, 15]


# 合并来自不同源的多个列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# 合并所有列表
# 创建一个新列表并扩展所有子列表
merged_list = []
merged_list.extend(list1)
merged_list.extend(list2)
merged_list.extend(list3)

print(f"合并后的列表: {merged_list}")


# 从不同数据源收集数据
database_results = ["数据1", "数据2"]
file_results = ["文件1", "文件2", "文件3"]
api_results = ["API1", "API2"]

# 收集所有数据
# 创建结果列表并扩展所有数据源
all_results = []
all_results.extend(database_results)
all_results.extend(file_results)
all_results.extend(api_results)

print(f"所有收集的数据: {all_results}")


# mac .bashrc userprofile
# 构建包含多个配置项的列表
base_config = ["配置1", "配置2"]
user_config = ["用户配置1", "用户配置2"]
system_config = ["系统配置1"]

# 合并配置
# 创建完整配置列表
full_config = []
full_config.extend(base_config)
full_config.extend(user_config)
full_config.extend(system_config)

print(f"完整配置: {full_config}")


# 展平嵌套的列表结构
nested_lists = [[1, 2, [7, 8]], [3, 4], [5, 6]]
flattened = []

# 展平嵌套列表
# 遍历嵌套列表并扩展每个子列表
for sublist in nested_lists:
    flattened.extend(sublist)

print(f"展平后的列表: {flattened}")
