import time
import csv
from datetime import datetime


# 定义ANSI颜色代码类，用来在终端输出带颜色的文字
class Colors:
    # 绿色
    GREEN = "\033[92m"
    # 黄色
    YELLOW = "\033[93m"
    # 红色
    RED = "\033[91m"
    # 重置颜色
    RESET = "\033[0m"


def colored_log(message, level="INFO"):
    colors = {
        "INFO": Colors.GREEN,
        "WARNING": Colors.YELLOW,
        "ERROR": Colors.RED,
    }
    color = colors.get(level, Colors.RESET)
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{color}{level} {timestamp}:{message}{ Colors.RESET}")


def show_progress():
    colored_log("开始加载学生的数据", "WARNING")
    for i in range(11):
        progress = i * 10
        bar = "#" * i + " " * (10 - i)
        print(f"\r{bar} {progress}%", end="", flush=True)
        time.sleep(0.1)
    colored_log("\n加载完成", "INFO")


class Student:
    def __init__(self, name, age, chinese, math, english):
        self.name = name
        self.age = age
        self.chinese = chinese
        self.math = math
        self.english = english
        self.average = (chinese + math + english) / 3

    # 定义对象的字符串表示，用于打印学生的信息
    def __str__(self):
        return f"学生:{self.name},年龄{self.age} 平均分:{self.average}"

    def get_grade(self):
        if self.average >= 90:
            return "A"
        elif self.average >= 80:
            return "B"
        elif self.average >= 70:
            return "C"
        else:
            return "D"


students_data = [
    ("张三", 20, 85, 92, 78),
    ("李四", 19, 76, 88, 94),
    ("王五", 21, 95, 87, 82),
    ("赵六", 20, 68, 75, 71),
    ("钱七", 22, 91, 96, 89),
]
students = [Student(*data) for data in students_data]
show_progress()
