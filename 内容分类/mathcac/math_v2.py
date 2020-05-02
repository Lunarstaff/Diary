# math_v2.py
from testpaper import TestPaper
import com_fun as cf

if __name__ == "__main__":

    # 获取输入值
    while True:
        data_len_in = input("请输入数据位数：")
        if data_len_in.isdigit() and int(data_len_in) > 0 and int(data_len_in) < 10:
            data_len_in = int(data_len_in)
            break
    while True:
        subject_num = input("请输入题目数量：")
        if subject_num.isdigit() and int(subject_num) > 0 and int(subject_num) <= 200:
            subject_num = int(subject_num)
            break
    op_symbol_in = input("请输入题目类型：")


    # 生成试卷
    t1 = TestPaper(data_len_in, subject_num, op_symbol_in)
    t1.print_paper_title()
    t1.test_start()
    t1.get_score()

    # 保存考试记录
    t1.save_test_paper()
