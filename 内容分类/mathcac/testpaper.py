# testpaper.py
from subject import Subject
import com_fun as cf
class TestPaper():
    def __init__(
        self, data_len, subject_num_in_paper, symbol_in_paper):
        self.data_len = data_len
        self.subject_num_in_paper = subject_num_in_paper
        self.subject_in_paper = []
        self.correct_num_in_paper = 0
        self.score = 0.0
        self.score_of_paper = 100.0
        if symbol_in_paper == "":
            self.paper_type = "随机"
        else:
            self.paper_type = symbol_in_paper
        self.symbol_in_paper = symbol_in_paper


    # 打印试卷头
    def print_paper_title(self):
        cf.print_len_str(70, "*", "")  # 加个时间？
        cf.print_len_str(40, " ", 
            "本次共{0}道题，满分100.0分，平均每道题{1}分".format(
                self.subject_num_in_paper, round(self.score_of_paper/self.subject_num_in_paper, 2)
                )
            )
        cf.print_len_str(40, " ", "题目类型为：{0}".format(self.paper_type))


    # 开始
    def test_start(self):
        cf.print_len_str(70, "*", "开始")
        # 根据数量循环产生算术题目
        for i in range(1, self.subject_num_in_paper + 1):
            subject_i = Subject(self.data_len, self.symbol_in_paper)
            subject_i.generate_subject()
            subject_i.get_correct_answer()
            # 输出题目
            cf.print_len_str(70, "*", "第{0}题".format(i))
            cf.print_subject(subject_i)
            # 判断正误
            while True:
                answer_in = input("请输入答案（如果是小数，请保留2位小数）：")
                if answer_in != "":
                    subject_i.answer_in = answer_in
                    break
            if subject_i.op_symbol == "÷":
                if subject_i.value == float(answer_in):
                    # 正确
                    self.correct_num_in_paper += 1
                    cf.print_len_str(35, "√", "正确！")
                    subject_i.answer_flag = "√"
                else:
                    #错误，输出正确答案
                    cf.print_len_str(35, "×", "错误！")
                    subject_i.answer_flag = "×"
                    print("正确答案为:{}".format(subject_i.value))
            else:
                if subject_i.value == int(answer_in):
                    # 正确
                    self.correct_num_in_paper += 1
                    cf.print_len_str(35, "√", "正确！")
                    subject_i.answer_flag = "√"
                else:
                    #错误，输出正确答案
                    cf.print_len_str(35, "×", "错误！")
                    subject_i.answer_flag = "×"
                    print("正确答案为:{}".format(subject_i.value))

            self.subject_in_paper.append(subject_i)


    # 统计结果和分数
    def get_score(self):
        cf.print_len_str(70, "*", "结束!")
        self.score = round(self.score_of_paper * self.correct_num_in_paper / self.subject_num_in_paper, 2)
        print("本次考试得分为：{}".format(self.score))


    # 保存考试记录
    def save_test_paper(self):
        text_out = "数据位数：{}\n题目数量：{}\n题目类型：{}\n本次得分：{}\n".format(
            self.data_len, self.subject_num_in_paper, self.paper_type, self.score)
        for i in range(1, self.subject_num_in_paper + 1):
            subject_i_text = "【第{0}题】:\n{1}{2}{3}={4}\t\t\t输入答案为{5}********{6}\n".format(
                i, self.subject_in_paper[i-1].opdata_1, self.subject_in_paper[i-1].op_symbol,
                self.subject_in_paper[i-1].opdata_2, self.subject_in_paper[i-1].value,
                self.subject_in_paper[i-1].answer_in, self.subject_in_paper[i-1].answer_flag
                )
            text_out += subject_i_text
        cf.write_str_to_file(text_out,"C:/Users/Lunar12/Desktop/" + cf.get_time_str() + ".txt")
