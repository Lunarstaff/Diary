from survey import AnonymousSurvey

# 定义一个问题，创建关于这个问题的调查对象
question = "你最喜欢做什么事？"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("任何时候按下\"q\"退出程序。")
while True:
    response = input("最喜欢做：")
    if response == "q":
        break
    my_survey.store_response(response)

# 显示调查结果：
print("谢谢参与！")
my_survey.show_results()
