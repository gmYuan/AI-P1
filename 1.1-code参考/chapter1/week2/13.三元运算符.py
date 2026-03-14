# value_if_true if condition else value_if_false
"""
x = 10
result = "正数" if x > 0 else "非正数"
# const result =  x > 0?"正数" : "非正数";
print(result)

a = 5
b = 3
max_num = a if a > b else b

if a > b:
    max_num = a
else:
    max_num = b
print(max_num)



def get_user_preference():
    # 模拟用户输入
    user_input = input("请输入您的偏好（1-3）：")
    # 使用三元表达式设置默认值
    # 如果user_input在['1', '2', '3']中，则preference为user_input
    # 否则，preference为'1'（默认值）
    preference = user_input if user_input in ["1", "2", "3"] else "1"
    return preference


# 测试函数
preference = get_user_preference()
print(f"用户偏好：{preference}")


# 是否在生产环境 development test production
is_production = True
# 根据环境选择不同的数据库URL
# 如果is_production为True，则使用生产环境URL
# 否则，使用开发环境URL
database_url = (
    "mysql://prod-server:3306/db" if is_production else "mysql://localhost:3306/db"
)
print(f"数据库URL：{database_url}")


def safe_get_name(user_dict):
    # 安全地获取用户名
    # 如果user_dict中有'name'键且值不为空，则返回该值
    # 否则，返回'未知用户'
    return user_dict.get("name") if user_dict.get("name") else "未知用户"


# 测试函数
user1 = {"name": "张三", "age": 25}
user2 = {"name": "", "age": 30}
user3 = {"age": 35}

print(f"用户1：{safe_get_name(user1)}")
print(f"用户2：{safe_get_name(user2)}")
print(f"用户3：{safe_get_name(user3)}")




# 在列表推导式中使用三元表达式
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 将偶数转换为字符串，奇数保持原样
# 对于每个数字，如果是偶数则转换为字符串，否则保持原样
processed_numbers = [str(x) if x % 2 == 0 else x for x in numbers]
print(f"处理后的数字：{processed_numbers}")

# 根据条件过滤和转换数据
scores = [85, 92, 78, 96, 88, 91, 87, 94]
# 将高分（>=90）标记为"优秀"，其他标记为"良好"
grade_list = ["优秀" if score >= 90 else "良好" for score in scores]
print(f"成绩等级：{grade_list}")

# 处理字符串列表
words = ["hello", "world", "python", "programming"]
# 将长度大于5的单词转换为大写，其他保持原样
processed_words = [word.upper() if len(word) > 5 else word for word in words]
print(f"处理后的单词：{processed_words}")



# 在函数中使用三元表达式
def get_user_role(user_type):
    # 根据用户类型返回角色
    # 如果user_type为'admin'，则返回'管理员'
    # 否则，返回'普通用户'
    return "管理员" if user_type == "admin" else "普通用户"


def calculate_discount(amount, is_vip):
    # 计算折扣
    # 如果是VIP用户且金额大于1000，则打8折
    # 否则，不打折
    discount_rate = 0.8 if is_vip and amount > 1000 else 1.0
    return amount * discount_rate


def format_phone_number(phone):
    # 格式化电话号码
    # 如果电话号码长度为11位，则添加分隔符
    # 否则，返回原号码
    return f"{phone[:3]}-{phone[3:7]}-{phone[7:]}" if len(phone) == 11 else phone


# 测试函数
print(f"用户角色：{get_user_role('admin')}")
print(f"用户角色：{get_user_role('user')}")

print(f"VIP用户1000元商品折扣后：{calculate_discount(1000, True)}")
print(f"普通用户1000元商品折扣后：{calculate_discount(1000, False)}")

print(f"格式化电话号码：{format_phone_number('13812345678')}")
print(f"格式化电话号码：{format_phone_number('1234567')}")

# const result =  x > 0?"正数" : x==0?"零":"非零";
x = 6
result1 = "正数" if x > 0 else "非正数"
result2 = "正数" if x > 0 else "0" if x == 0 else "负数"
result3 = "大于5" if x > 5 else "小于等于5" if x > 0 else "非正数"
print(result1)
print(result2)
print(result3)

"""
