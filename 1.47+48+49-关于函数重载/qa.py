
# ----------------------------------------------------------------

message = "用户 {} 登录成功 {} "
args = ("Alice", "2")
print(message.format(*args))




# ----------------------------------------------------------------

def wrapper(*args, **kwargs):
    pass


def register():
    print("register")


wrapper.register = register

wrapper.register()