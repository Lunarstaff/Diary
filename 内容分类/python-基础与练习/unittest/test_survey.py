import unittest
from survey import AnonymousSurvey
import sys


class TestAnonymousSurvey(unittest.TestCase):
    # setUp方法，创建测试用的测试问题，调查对象，答案
    @classmethod
    def setUpClass(cls):
        question = "测试问题XXX..."
        cls.test_survey = AnonymousSurvey(question)
        cls.responses = ["1st answer", "2nd answer", "3rd answer"]

    # 检查点一：接收到单个答案时是否可以正确保存
    def test_store_single_response(self):
        self.test_survey.store_response(self.responses[0])
        # 断言
        self.assertIn(self.responses[0], self.test_survey.responses)

    # 检查点二：接收到三个答案时是否可以正确保存
    @unittest.skip("跳过测试接收到三个答案的场景！")
    def test_store_three_responses(self):
        for i in self.responses:
            self.test_survey.store_response(i)
        # 断言
        for j in self.responses:
            self.assertIn(j, self.test_survey.responses)

    # 跳过测试演示
    lp = "C:\\E-Data-File\\腾讯课堂\\Diary\\内容分类\\python-基础与练习\\unittest"
    @unittest.skipIf(AnonymousSurvey.__path__ == lp, "测试路径正确，跳过测试。")
    def test_pathtest(self):
        print("如果打印这条消息，说明测试路径不对。")

    # 跳过测试演示
    @unittest.skipUnless(sys.platform.startswith("linux"), "只在Linux平台下执行这条测试")
    def test_platforinfo(self):
        print("如果打印这条消息，说明当前是在Linux平台测试")


# 主函数
if __name__ == "__main__":
    unittest.main()
