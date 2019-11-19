#

import unittest as ut

class T1(ut.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试类T1的setUp方法，已经为下面的测试做好了准备！~\n")

    @classmethod
    def tearDownClass(cls):
        print("测试类T1的tearDown方法，这里结束测试！~")

    # @classmethod
    # def tearDown(cls):
    #     print("测试类T1的tearDown方法，这里结束测试！~")

    def test_fuc_001(self):
        print("测试类T1中的测试方法001")
        self.assertEqual(2, 1+1)

    def test_fuc_002(self):
        print("测试类T1中的测试方法002")
        self.assertEqual(2, 1+1)

    def test_fuc_003(self):
        print("测试类T1中的测试方法003")
        self.assertEqual(2, 1+1)

    def test_fuc_004(self):
        print("测试类T1中的测试方法004")
        self.assertEqual(2, 2+1)

    def test_fuc_005(self):
        print("测试类T1中的测试方法005")
        self.assertEqual(2, 1+1)




# 主函数
if __name__ == "__main__":
    ut.main()
