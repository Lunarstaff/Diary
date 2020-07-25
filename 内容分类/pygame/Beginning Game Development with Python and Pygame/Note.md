# Beginning Game Development with Python and Pygame From Novice（新手） to Professional

## 有利于游戏的一些Python标准库
- math模块
>math模块中的一些方法

|方法|描述|例子|
|:---|:---|:---|
|sin|正弦函数|sin(angle)|
|cos|余弦函数|cos(angle)|
|tan|正切函数|sin(angle)|
|ceil|向上取整，返回整型|ceil(3.4323)|
|fabs|求绝对值，返回浮点型|fabs(–2.65)|
|floor|向下取整|floor(7.234)|
|pi|圆周率，常量|pi*radius**2|

- [datetime模块](https://www.cnblogs.com/awakenedy/articles/9182036.html)  

|类|描述|
|:---|:---|
|timedelta|计算二个datetime对象的差值|
|date|日期类，由year年份、month月份及day日期三部分构成|
|time|时间类，由hour小时、minute分钟、second秒、microsecond毫秒和tzinfo五部分组成|
|datetime|日期时间类，可以看做是date类和time类的合体|

- random模块
>random模块中的一些方法

|方法|描述|
|:---|:---|
|seed|指定一组随机数的种子，适用于下面的随机生成方法|
|randint|返回在两个整数之前的随机整数|
|choice|从一个集合中选择一个随机的元素|
|random|返回一个在0到1之间的浮点数|
我们调用random.random()生成随机数时，每一次生成的数都是随机的。
但是，当我们预先使用 random.seed(x) 设定好种子之后，其中的 x 可以是任意数字，如10，
这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。  
注意：seed()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

## 介绍Pygame
- Pygame有许多模块可以独立使用  
[Pygame官方文档](https://www.pygame.org/docs/)

|模块|描述|
|:---|:---|
|pygame.cdrom|访问和控制光驱|
|pygame.cursors|加载光标图像|
|pygame.display|访问显示器|
|pygame.draw|绘制点、线、形|
|pygame.event|管理（计算机）外部事件|
|pygame.font|使用系统字体|
|pygame.image|加载保存图像|
|pygame.joystick|使用手柄操纵杆或模拟设备|
|pygame.key|从键盘读取按键|
|pygame.mixer|加载播放声音|
|pygame.mouse|管理鼠标|
|pygame.movie|播放视频文件|
|pygame.music|同时处理音乐和音频|
|pygame.overlay|访问高级视频覆盖？|
|pygame|包含高级的Pygame方法|
|pygame.rect|管理矩形区域|
|pygame.sndarray|处理声音数据|
|pygame.sprite|管理移动中的图像|
|pygame.surface|管理图像和屏幕|
|pygame.surfarray|处理图像和像素数据|
|pygame.sprite|管理移动中的图像|
|pygame.time|管理时序和帧率|
|pygame.transform|调整图像的大小和位置|

- 模块详细  
1、pygame.display模块
>这个模块提供了pygame的显示控制，不管是窗口模式还是全屏模式pygame都只有一个显示窗口。  
>所有的改变都不会立刻在显示窗口上更新，需要调用一个或两个flip方法更新实际显示。  
>display初始位置是在(0, 0)  
>display实际上可以被多个模块之一初始化。  
>可以向pygame.display.set_mode()传递参数来启用硬件加速或OpenGL支持的模式。  
>Pygame在任何时刻只有一个活动的显示窗口，如果使用pygame.display.set_mode()新建一个显示窗口，就会关闭先前的显示窗口。  
>如果需要精确控制显示象素和分辨率可以使用pygame.display.mode_ok()、pygame.display.list_modes()、和pygame.display.Info()方法查询显示器的信息。  
>
    - pygame.display.init()










# 问题
- Surface 是个什么类

# 生词
- a number of  
许多, 若干  
- independently  
adv. 独立地,自立地;无关地  
- breeze  
n. 微风；轻而易举的事；煤屑；焦炭渣；小风波  
vi. 吹微风；逃走
- external  
adj. 外部的；表面的；外面的；[药]外用的；外国的  
n. 外部；外面；外观
- rectangular  
adj. 〈数〉长方形的; 矩形的  
- precise  
adj. 精确的；明确的；严格的  
[名 词]: preciseness
- flip
vt. 轻击；掷  
vi. 用指轻弹；蹦跳  
adj. 无礼的；轻率的  
n. 筋斗；弹  
- acceleration 
n. 加速；加快  
(车辆)加速能力,加速的幅度  
<物>加速度  
(优秀学生的)跳级  
- previous 
adj. 以前的；早先的；过早的  
adv. 在…以前；在先  
