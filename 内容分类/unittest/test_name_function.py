# test_name_function.py

import unittest
from name_function import get_formatted_name


# 测试name_function.py
class NameTestCase(unittest.TestCase):

    # 检查处理只有姓和名的名字
    def test_first_last_name(self):
        formatted_name = get_formatted_name("mingzi", "xingshi")
        self.assertEqual(formatted_name, "Mingzi Xingshi")

    # 检查处理有姓、名和中间名的名字
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name("fname", "lname", "mname")
        self.assertEqual(formatted_name, "Fname Mname Lname")


# 主函数
if __name__ == "__main__":
    unittest.main()
