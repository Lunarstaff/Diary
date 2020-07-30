from name_function import get_formatted_name

# 主函数
if __name__ == "__main__":
    print("在任何时候按下\"q\"键退出！")
    while True:
        first = input("请输入英文名的名字：")
        if first == "q":
            break
        last = input("请输入英文名的姓：")
        if first == "q":
            break
        formatted_name = get_formatted_name(first, last)
        print("完整的姓名为：" + formatted_name)
