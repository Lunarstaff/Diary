# 100以内的加减法
import random
num_max = input("请输入算术结果范围：")
m_numbers_max = input("请输入算术题数量：")
numbers = range(1, int(num_max)+1)
sembol = ["+", "-", "×", "÷"]
m_numbers = 0   # 题目数量
correct_num= 0  # 正确数量
wrong_num = 0   # 错误数量


# 审阅
def if_correct(num1, num2, sem, rel):
    rel = int(rel)
    if sem == "+":
        if num1 + num2 == rel:
            return True
        else:
            return False
    elif sem == "-":
        if num1 - num2 == rel:
            return True
        else:
            return False
    elif sem == "×":
        if num1 * num2 == rel:
            return True
        else:
            return False
    elif sem == "÷":
        num1 = float(num1)
        num2 = float(num2)
        rel = float(rel)
        if num1 / num2 == rel:
            return True
        else:
            return False
    else:
        print("不支持的算术类型！")


# 计算分数
def get_score(num, c_num):
    score = (100/num) * c_num
    return score


# 主函数
if __name__ == "__main__":
    while True:
        add_01 = random.choice(numbers)
        add_02 = random.choice(numbers)
        sembol_m = random.choice(sembol)
        if sembol_m == "-":
            if add_01 < add_02:
                continue
        elif sembol_m == "+":
            if add_01 + add_02 > int(num_max):
                continue
        elif sembol_m == "×":
            if add_01 * add_02 > int(num_max):
                continue
        m_numbers += 1
        print(str(add_01) + sembol_m + str(add_02) + " ")
        resualt = input("=")
        if if_correct(add_01, add_02, sembol_m, resualt):
            print("------[√]")
            correct_num += 1
        else:
            print("------[×]")
        if m_numbers == int(m_numbers_max):
            break
    print("答题完毕！得分为：" + str(get_score(m_numbers, correct_num)))



