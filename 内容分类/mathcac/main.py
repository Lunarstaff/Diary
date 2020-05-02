# import tkinter as tk
# main_frame = tk.Tk(bg="red")
# 窗口大小
# main_frame.mainloop()

import math
import random
global num_global
num_global = "0123456789"

# 生成指定位数的随机整数
def generate_N_num(N=3):
    # 返回数据
    re_num = 0
    # 位指数
    pos_i = 1
    for re_num_i in range(N):
        re_num += int(random.choice(num_global)) * pos_i
        pos_i *= 10
    return re_num


# 运算符号类
# class CALCU_SIGNS():
#     def __init__:
       

# 生成指定或随机的运算符号(calculating signs)
def generate_symbol():
    arg = "+-×÷"
    # 返回数据
    re_s = random.choice(arg)
    return re_s


# 检查结果
def checker_two(a1, a2, r, symbol):
    # fsum的入参是数据列表
    # fsum 计算结果带小数
    if symbol == "+":
        if int(r) == sum((a1, a2)):
            print("[√]**********************结果正确！*************************")
        else:
            print("[×]**********************结果错误！*************************")
            print("{0}{1}{2}正确结果为{3}".format(a1,symbol,a2,sum((a1, a2))))
    elif symbol == "-":
        if int(r) == a1-a2:
            print("[√]**********************结果正确！*************************")
        else:
            print("[×]**********************结果错误！*************************")
            print("{0}{1}{2}正确结果为{3}".format(a1,symbol,a2,(a1-a2)))
    elif symbol == "×":
        if int(r) == a1*a2:
            print("[√]**********************结果正确！*************************")
        else:
            print("[×]**********************结果错误！*************************")
            print("{0}{1}{2}正确结果为{3}".format(a1,symbol,a2,(a1*a2)))
    elif symbol == "÷":
        if float(r) == round(a1/a2,2):
            print("[√]**********************结果正确！*************************")
        else:
            print("[×]**********************结果错误！*************************")
            print("{0}{1}{2}正确结果为{3}".format(a1,symbol,a2,(round(a1/a2,2))))
    else:
        print("checker_two 的定义-- 入参【符号】为空或不合法")
    

# 随机生成加法算术题
def generate_sum(sum_N, symb="+"):
    add_1 = generate_N_num(sum_N)
    add_2 = generate_N_num(sum_N)
    # 输出
    print("{0}{1}{2}=".format(add_1, symb, add_2))
    while True:
        resualt = input("************请输入结果：")
        if resualt != "":
            break
    checker_two(add_1, add_2, resualt, symb)


# 随机生成减法算术题
def generate_minus(minus_N, symb="-"):
    while True: # 减数大于被减数
        minus_1 = generate_N_num(minus_N)
        minus_2 = generate_N_num(minus_N)
        if minus_1 > minus_2:
            break
    # 输出
    print("{0}{1}{2}=".format(minus_1, symb, minus_2))
    while True:
        resualt = input("************请输入结果：")
        if resualt != "":
            break
    checker_two(minus_1, minus_2, resualt, symb)


# 随机生成乘法算术题
def generate_multiply(multi_N, symb="×"):
    multi_1 = generate_N_num(multi_N)
    multi_2 = generate_N_num(multi_N)
    # 输出
    print("{0}{1}{2}=".format(multi_1, symb, multi_2))
    while True:
        resualt = input("************请输入结果：")
        if resualt != "":
            break
    checker_two(multi_1, multi_2, resualt, symb)


# 随机生成除法算术题
def generate_divide(divide_N, symb="÷"):
    divide_1 = generate_N_num(divide_N)
    while True:  # 被除数不能为0
        divide_2 = generate_N_num(divide_N)
        if divide_2 != 0:
            break
    # 输出
    print("{0}{1}{2}=".format(divide_1, symb, divide_2))
    while True:
        resualt = input("************请输入结果(如果是小数，保留2位小数)：")
        if resualt != "":
            break
    checker_two(divide_1, divide_2, resualt, symb)

# 生成随机算术题
# def generate_title(divide_N, symb="+"):
    

# 试卷
def generate_paper(title_num=10, max_n=3, symbol_in_paper=""):
    '''
    title_num 试卷题目数量，默认为10
    max_n 数据范围，默认为3位数
    symbol_in_paper 选择的题目类型，默认随机
    '''

    # 正确数量
    correct_num = 0

    # 题目类型
    if symbol_in_paper == "":
        symbol_in_title = "随机"
    elif symbol_in_paper in "+-×÷*/":
        if symbol_in_paper == "*":
            symbol_in_paper = "×"
        if symbol_in_paper == "/":
            symbol_in_paper = "÷"
        symbol_in_title = symbol_in_paper  
    else:
        print("generate_paper()-- 输入参数symbol_in_paper 错误")

    # 试卷开始
    print("*************************试卷开始*************************")
    print("*共{}题，满分100分，平均每题{}分！                           *".format(title_num, round(100/title_num, 2)))
    print("*算术类型为{}                                             *".format(symbol_in_title))
    print("*********************************************************")
    for title_i in range(title_num):
        print("*第{}题                                              *".format(title_i+1))
        # 生成题目
        if symbol_in_title == "随机":
            symbol_in_title = generate_symbol()
        else:
            symbol_in_title = symbol_in_paper
        if symbol_in_title == "+":
            generate_sum(max_n)
        elif symbol_in_title == "-":
            generate_minus(max_n)
        elif symbol_in_title in"*×":
            generate_multiply(max_n)
        elif symbol_in_title in "/÷":
            generate_divide(max_n)

        # 统计
        

# 测试主函数
if __name__ == "__main__":

    # 测试generate_N_num(1) 是否可以生成数字0
    #while True:
    #    tt = generate_N_num(1)
    #    if tt == 0:  # 测试generate_N_num(1) 是否可以生成数字0
    #        print("tt == 0 True")
    #        break

    # 测试输出随机运算符
    # generate_symbol()
    # print("symbol_t = generate_symbol" + symbol_t)

    # 测试输出加法
    # generate_sum(10)
    # generate_minus(2)
    # generate_multiply(1)
    # generate_divide(2)

    # 测试试卷
    
    while True:
        title_num = input("试卷题目数量为：")
        if title_num != "":
            title_num = int(title_num)
            break
    while True:
        max_n = input("试卷数据位数为：")
        if max_n != "":
            max_n = int(max_n)
            break
    while True:
        symbol_in_paper = input("试卷题目类型为：")
        if symbol_in_paper != "":
            break
    generate_paper(title_num, max_n, symbol_in_paper)

    
        
        
    

