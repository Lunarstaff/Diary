# subject.py
import com_fun as cf
class Subject():
    '''
    输入数据位数data_len和算术符号op_symbol
    先调用 cf.generate_data() 生成算术数据opdata_1、opdata_2
    再调用 get_correct_answer() 生成正确答案value
    '''
    def __init__(self, data_len, op_symbol):
        self.data_len = data_len
        self.opdata_1 = 0
        self.opdata_2 = 0
        self.value = 0.0
        self.op_symbol = cf.generat_symbol(op_symbol)
        self.answer_in = 0.0
        self.answer_flag = ""

    # 生成题目数据
    # 应该要加上 符号
    def generate_subject(self):
        if self.op_symbol == "÷":
            self.opdata_1 = cf.generate_data(self.data_len)
            while True:
                self.opdata_2 = cf.generate_data(self.data_len)
                if self.opdata_2 !=0:
                    break
        elif self.op_symbol in "+-×":
            self.opdata_1 = cf.generate_data(self.data_len)
            self.opdata_2 = cf.generate_data(self.data_len)
        else:
            print("Subject-generate_subject------self.op_symbol 错误")

    # 计算题目正确答案
    def get_correct_answer(self):
        if self.op_symbol == "+":
            self.value = sum((self.opdata_1, self.opdata_2))
        elif self.op_symbol == "-":
            self.value = self.opdata_1 - self.opdata_2
        elif self.op_symbol == "×":
            self.value = self.opdata_1 * self.opdata_2
        elif self.op_symbol == "÷":
            self.value = round(self.opdata_1 / self.opdata_2, 2)