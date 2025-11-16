# 1.把py文件编译. 编译阶段主要包括 词法/语法分析(生成抽象语法树)和字节码的生成

# 处理抽象语法树的
import ast

# 用于反汇编字节码
import dis

# 源代码
source_code = """
a = 1
print(a+2)
"""
print(source_code)

try:
    # 调用ast.parse 解析源代码为 AST语法树对象
    tree = ast.parse(source_code)
    # 打印AST语法树，缩进为2
    print(ast.dump(tree, indent=2))
except SyntaxError as e:
    print(f"语法错误:{e}")
# 编译字节码
try:
    # 使用compile 将源代码编译为字节码对象，文件名设置为<string>,模式为exec
    code_obj = compile(source_code, "<string>", "exec")
    print(
        code_obj
    )  # <code object <module> at 0x0000029ACB122D30, file "<string>", line 1>
    # 调用dis方法反汇编字节码，输出详细的字节码指令列表
    dis.dis(code_obj)
except SyntaxError as e:
    print("编译错误:{e}")

# 执行获取结果
try:
    # 用exec执行上面的compile出来的字节码对象
    exec(code_obj)
except Exception as e:
    print(f"执行错误:{e}")
