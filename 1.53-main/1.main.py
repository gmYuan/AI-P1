

# -------------------------------------------------------------------

import utils

def main():
    print("hello world")


if __name__ == "__main__":
    main()



# -------------------------------------------------------------------

import argparse


def main():
    parser = argparse.ArgumentParser(description="如何处理命令行参数")
    # 添加一个name的位置参数
    parser.add_argument("name", type=str, help="请输入你的名字")
    args = parser.parse_args()
    print(args)
    print(f"Hello,{args.name}")


if __name__ == "__main__":
    main()




# -------------------------------------------------------------------

import unittest
from calculator import add_numbers, greet_user


class TestMyFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_greet_user(self):
        self.assertEqual(greet_user("zhangsan"), "hello,zhangsan")


if __name__ == "__main__":
    unittest.main()



