# com_fun.py

import random
from os import path
import time

# 生成指定位数的随机整数
def generate_data(data_len):
    # 返回数据
    return_data = 0
    # 位指数
    pos_i = 1
    for re_num_i in range(data_len):
        return_data += int(random.choice("0123456789")) * pos_i
        pos_i *= 10
    return return_data

# 生成随机的运算符号
def generat_random_symbol():
    arg = "+-×÷"
    # 返回数据
    re_s = random.choice(arg)
    return re_s

def generat_symbol(op_symbol):
    if op_symbol == "":
        symbol_out = generat_random_symbol()
    elif op_symbol == "+":
        symbol_out = "+"
    elif op_symbol == "-":
        symbol_out = "-"
    elif op_symbol in "*×":
        symbol_out = "×"
    elif op_symbol in "/÷":
        symbol_out = "÷"
    else:
        print("Symbol-self.symbol_in -- 输入错误")
    return symbol_out


# 打印题目
def print_subject(subject):
    opdata_1 = str(subject.opdata_1)
    opdata_2 = str(subject.opdata_2)
    op_symbol = str(subject.op_symbol)
    str_out = "{0}{1}{2}=".format(opdata_1, op_symbol, opdata_2)
    print(str_out)

# 格式打印
def print_len_str(str_len, fill_char, s_in):
    s_out = s_in.ljust(str_len, fill_char)
    print(s_out)


# 获取当前系统时间返回字符串
def get_time_str():
 return time.strftime("%Y%m%d%H%M%S")

# 把指定的字符串写入指定的目录文件中
# cf.write_str_to_file(text_out,"C:/Users/Lunar12/Desktop/" + cf.get_time_str() + ".txt")
def write_str_to_file(text_str, file_path):
    with open(file_path, "w") as fo:
        fo.write(text_str)
        fo.close()
    print("试卷保存在{}，保存成功！".format(file_path))

