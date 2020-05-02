# Python tkinter
import tkinter
# 主窗体
main_win = tkinter.Tk()

# 主窗体标题
main_win.title = "主窗体标题"

# 设置主窗体的几何属性
# 参数为字符串 长x宽+(屏幕位置x)+(屏幕位置y),注意长x宽是X的小写，不是乘号
main_win.geometry("1200x800+0+0") 

# Label 控件
'''
main_win 父窗体对象
text 标签文本内容，为字符串
bg 背景色，用字符串表示，一般有两种形式，表示颜色名称的英文单词"red" "black"等，或者CSS表示颜色的以#号开头的16进制表示的三色数据"#FD9622"
fg 前景色（字体色）
font 字体
width 标签宽度（字数）
height 标签高度（行数）
wraplength 标签文本中多长(单位是像素)之后换行
justify 标签文本换行后的对齐方式
anchor 标签文本在标签体中的位置，默认为居中 anchor的值必须为 n北，e东，w西，s南, ne东北, se东南, sw西南, nw西北, center居中
'''
label_1_on_main_win = tkinter.Label(
        main_win,
        text = "label_1_on_main_win",
        bg = "#FD9622", fg = "red",
        # font = ("黑体", 20),
        width= 20,
        height = 1,
        # wraplength = 100,
        justify = "left",
        anchor = "nw"
    )
label_1_on_main_win.pack(anchor = "nw")


# Button控件
def button_1_func():
    print("button_1_on_main_win 按下")
'''
main_win 父窗体对象
text 按钮文本
command 按钮按下后的动作（方法名）
width 按钮宽度（字数）
height 按钮高度（行数）
anchor 按钮文本在按钮上的位置
'''
button_1_on_main_win = tkinter.Button(
        main_win,
        text = "按钮一", 
        command = button_1_func, 
        width = 5, 
        height = 1
        # , anchor = "nw"
    )
button_1_on_main_win.pack(anchor = "nw")

button_2_on_main_win = tkinter.Button(
        main_win,
        text = "退出", 
        command = main_win.quit, 
        width = 5, 
        height = 1,
        bg = "#FD9622", fg = "red"
        # , anchor = "nw"
    )
button_2_on_main_win.pack(anchor = "sw")

# Entry控件

    # 密文显示
    # 使用show = "*" 表示输入字符后显示为*
entry_1 = tkinter.Entry(
        main_win,
        show = "*"
    )
entry_1.pack(anchor = "nw")

    # 绑定变量
var = tkinter.Variable()
entry_2 = tkinter.Entry(
        main_win,
        textvariable = var
    )
entry_2.pack(anchor = "nw")

    # 给entry_2中要显示的值赋值
var.set("5555")


# 点击按钮输出Entry中的内容
def print_entry():
    print(entry_2.get())

button_3_on_main_win = tkinter.Button(
        main_win,
        text = "输出Entry内容", 
        command = print_entry,
        width = 9, 
        height = 1,
        bg = "#FD9622", fg = "red"
        # , anchor = "nw"
    )
button_3_on_main_win.pack(anchor = "nw")


# Text控件
'''
Text文本框控件，用于显示多行文本
width 宽度，单位是字符（汉字 和 英文都算1字符）
height 高度，单位是行
'''
text_1 = tkinter.Text(
        main_win,
        width = 30,
        height = 10,
        bg = "#282923",
        fg = "#E79622"
    )
text_1.pack(anchor = "nw")
text_str = '''
          千字文
【作者】周兴嗣  【朝代】南北朝
    天地玄黄，宇宙洪荒。
    日月盈昃，辰宿列张。
    寒来暑往，秋收冬藏。
    闰余成岁，律吕调阳。
    云腾致雨，露结为霜。
    金生丽水，玉出昆冈。
'''
text_1.insert(tkinter.INSERT, text_str)

# 带滚动条的Text
    # 创建滚动条
scroll_on_text_2 = tkinter.Scrollbar()
    # 创建文本框
text_2 = tkinter.Text(
        main_win,
        width = 30,
        height = 10,
        bg = "#282923",
        fg = "#E79622"
    )
    # 把滚动条放在文本框上
scroll_on_text_2.pack(side = tkinter.LEFT, fill = tkinter.Y)
    # 再把文本框放在主窗口上
text_2.pack(side=tkinter.LEFT, fill=tkinter.Y)
    # 把滚动条与文本框关联起来
scroll_on_text_2.config(
        command = text_2.yview
    )
text_2.config(
        yscrollcommand = scroll_on_text_2.set
    )
text_2_str = '''
千字文

【作者】周兴嗣 【朝代】南北朝

天地玄黄，宇宙洪荒。
日月盈昃，辰宿列张。
寒来暑往，秋收冬藏。
闰余成岁，律吕调阳。
云腾致雨，露结为霜。
金生丽水，玉出昆冈。
剑号巨阙，珠称夜光。
果珍李柰，菜重芥姜。
海咸河淡，鳞潜羽翔。
龙师火帝，鸟官人皇。
始制文字，乃服衣裳。
推位让国，有虞陶唐。
吊民伐罪，周发殷汤。
坐朝问道，垂拱平章。
爱育黎首，臣伏戎羌。
遐迩一体，率宾归王。
鸣凤在竹，白驹食场。
化被草木，赖及万方。
盖此身发，四大五常。
恭惟鞠养，岂敢毁伤。
女慕贞洁，男效才良。
知过必改，得能莫忘。
罔谈彼短，靡恃己长。
信使可覆，器欲难量。
墨悲丝染，诗赞羔羊。
景行维贤，克念作圣。
德建名立，形端表正。
空谷传声，虚堂习听。
祸因恶积，福缘善庆。
尺璧非宝，寸阴是竞。
资父事君，曰严与敬。
孝当竭力，忠则尽命。
临深履薄，夙兴温凊。
似兰斯馨，如松之盛。
川流不息，渊澄取映。
容止若思，言辞安定。
笃初诚美，慎终宜令。
荣业所基，籍甚无竟。
学优登仕，摄职从政。
存以甘棠，去而益咏。
乐殊贵贱，礼别尊卑。
上和下睦，夫唱妇随。
外受傅训，入奉母仪。
诸姑伯叔，犹子比儿。
孔怀兄弟，同气连枝。
交友投分，切磨箴规。
仁慈隐恻，造次弗离。
节义廉退，颠沛匪亏。
性静情逸，心动神疲。
守真志满，逐物意移。
坚持雅操，好爵自縻。
都邑华夏，东西二京。
背邙面洛，浮渭据泾。
宫殿盘郁，楼观飞惊。
图写禽兽，画彩仙灵。
丙舍旁启，甲帐对楹。
肆筵设席，鼓瑟吹笙。
升阶纳陛，弁转疑星。
右通广内，左达承明。
既集坟典，亦聚群英。
杜稿钟隶，漆书壁经。
府罗将相，路侠槐卿。
户封八县，家给千兵。
高冠陪辇，驱毂振缨。
世禄侈富，车驾肥轻。
策功茂实，勒碑刻铭。
盘溪伊尹，佐时阿衡。
奄宅曲阜，微旦孰营。
桓公匡合，济弱扶倾。
绮回汉惠，说感武丁。
俊义密勿，多士实宁。
晋楚更霸，赵魏困横。
假途灭虢，践土会盟。
何遵约法，韩弊烦刑。
起翦颇牧，用军最精。
宣威沙漠，驰誉丹青。
九州禹迹，百郡秦并。
岳宗泰岱，禅主云亭。
雁门紫塞，鸡田赤诚。
昆池碣石，钜野洞庭。
旷远绵邈，岩岫杳冥。
治本于农，务兹稼穑。
俶载南亩，我艺黍稷。
税熟贡新，劝赏黜陟。
孟轲敦素，史鱼秉直。
庶几中庸，劳谦谨敕。
聆音察理，鉴貌辨色。
贻厥嘉猷，勉其祗植。
省躬讥诫，宠增抗极。
殆辱近耻，林皋幸即。
两疏见机，解组谁逼。
索居闲处，沉默寂寥。
求古寻论，散虑逍遥。
欣奏累遣，戚谢欢招。
渠荷的历，园莽抽条。
枇杷晚翠，梧桐蚤凋。
陈根委翳，落叶飘摇。
游鹍独运，凌摩绛霄。
耽读玩市，寓目囊箱。
易輶攸畏，属耳垣墙。
具膳餐饭，适口充肠。
饱饫烹宰，饥厌糟糠。
亲戚故旧，老少异粮。
妾御绩纺，侍巾帷房。
纨扇圆洁，银烛炜煌。
昼眠夕寐，蓝笋象床。
弦歌酒宴，接杯举殇。
矫手顿足，悦豫且康。
嫡后嗣续，祭祀烝尝。
稽颡再拜，悚惧恐惶。
笺牒简要，顾答审详。
骸垢想浴，执热愿凉。
驴骡犊特，骇跃超骧。
诛斩贼盗，捕获叛亡。
布射僚丸，嵇琴阮箫。
恬笔伦纸，钧巧任钓。
释纷利俗，并皆佳妙。
毛施淑姿，工颦妍笑。
年矢每催，曦晖朗曜。
璇玑悬斡，晦魄环照。
指薪修祜，永绥吉劭。
矩步引领，俯仰廊庙。
束带矜庄，徘徊瞻眺。
孤陋寡闻，愚蒙等诮。
谓语助者，焉哉乎也。
'''
text_2.insert(tkinter.INSERT, text_2_str)

# CheckButton 复选框
def checkbox_update():
    message = ""
    if checkbox_001.get() == True:
        message += "checkbox_001 checked\n"
    if checkbox_002.get() == True:
        message += "checkbox_002 checked\n"
    if checkbox_003.get() == True:
        message += "checkbox_003 checked\n"
    # 清空显示文本框中的值
    text_3.delete(0.0, tkinter.END)
    # 在显示文本框中插入字符串
    text_3.insert(tkinter.INSERT, message)

    # 定义复选框每个选项绑定的变量，为布尔值
checkbox_001 = tkinter.BooleanVar()
checkbox_002 = tkinter.BooleanVar()
checkbox_003 = tkinter.BooleanVar()
    # 定义复选框的每个选项
check_001 = tkinter.Checkbutton(
        main_win,
        text = "checkbox_001",
        variable = checkbox_001,
        command = checkbox_update
    )
check_001.pack(anchor = "w")
check_002 = tkinter.Checkbutton(
        main_win,
        text = "checkbox_002",
        variable = checkbox_002,
        command = checkbox_update
    )
check_002.pack(anchor = "w")
check_003 = tkinter.Checkbutton(
        main_win,
        text = "checkbox_003",
        variable = checkbox_003,
        command = checkbox_update
    )
check_003.pack(anchor = "w")
    # 显示文本框
text_3 = tkinter.Text(
        main_win,
        width = 20,
        height = 4,
        bg = "#282923",
        fg = "#E79622"
    )
text_3.pack(anchor = "w")

# RadioButton单选按钮
def radiobutton_update():
    print(radio_var.get())
    # 一组单选按钮绑定一个变量
radio_var = tkinter.IntVar()
    # 定义单选按钮的每个选项
radio_001 = tkinter.Radiobutton(
        main_win,
        text = "radio_001",
        value = 1, # 这个值必须是floating-point
        variable = radio_var,
        command = radiobutton_update
    )
radio_001.pack(anchor = "w")
radio_002 = tkinter.Radiobutton(
        main_win,
        text = "radio_002",
        value = 2,
        variable = radio_var,
        command = radiobutton_update
    )
radio_002.pack(anchor = "w")
radio_003 = tkinter.Radiobutton(
        main_win,
        text = "radio_003",
        value = 3,
        variable = radio_var,
        command = radiobutton_update
    )
radio_003.pack(anchor = "w")


# ListBox 列表框 第一种(列表展示框)
listbox_001 = tkinter.Listbox(main_win, selectmode = tkinter.BROWSE)
listbox_001.pack(anchor = "w")
    # 为下拉列表的每一项添加内容
list_content = ["list_content_001", ["list_content_002_1", "list_content_002_2"], "list_content_003"]
for item in list_content:
    listbox_001.insert(tkinter.END, item)
    # 在列表开始添加内容
def insert_at_start_func():
    listbox_001.insert(tkinter.ACTIVE, "listbox_insert_at_start")
    print("listbox_001_insert_at_start_button 按下")
listbox_001_insert_at_start_button = tkinter.Button(
    main_win,
    text="insert_at_start",
    command=insert_at_start_func,
    width=12,
    height=1
    # , anchor = "nw"
)
listbox_001_insert_at_start_button.pack(anchor = "w")

    # 在列表尾部添加一个列表
def insert_at_end_func():
    listbox_001.insert(tkinter.END, ["list_insert_end_1", "list_insert_end_2"])
    print("listbox_001_insert_at_end_button 按下")
listbox_001_insert_at_end_button = tkinter.Button(
    main_win,
    text="insert_at_end",
    command=insert_at_end_func,
    width=12,
    height=1
    # , anchor = "nw"
)
listbox_001_insert_at_end_button.pack(anchor = "w")
    # 删除：第一个参数为开始的索引，第二个参数为结束的索引，如果不指定第二个参数，只删除第一个索引处的内容
def delete_front_two():
    listbox_001.delete(0, 1)
    print("listbox_001_delete_front_two_button 按下")
listbox_001_delete_front_two_button = tkinter.Button(
    main_win,
    text="delete_front_two",
    command=delete_front_two,
    width=12,
    height=1
    # , anchor = "nw"
)
listbox_001_delete_front_two_button.pack(anchor = "w")
    # 选中
def selected_front_three():
    listbox_001.select_set(0, 2)
    print("listbox_001_selected_front_three_button 按下")
listbox_001_selected_front_three_button = tkinter.Button(
    main_win,
    text="selected_front_three",
    command=selected_front_three,
    width=12,
    height=1
    # , anchor = "nw"
)
listbox_001_selected_front_three_button.pack(anchor = "w")
    # 取消选中
# listbox_001.select_clear()
# 进入消息循环
main_win.mainloop()