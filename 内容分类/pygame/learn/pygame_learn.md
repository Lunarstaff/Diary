# 标题

## 第一章
Pygame 是在SDL基础上进行的封装。SDL是各种操作系统中可以与各种外设交互的第三方库。
在Python环境中安装好pygame之后可以执行`python -m pygame.examples.aliens`运行自带的小游戏

### 第1-1
pygame的安装
pygame是Python最经典的2D游戏开发第三方库，也支持3D游戏开发。适合用于游戏逻辑验证、游戏入门及系统演示验证。
pygame的最小开发框架

```python
# pygame的最小开发框架
import pygame as pg, sys

# 初始化及设置
pg.init()   # 初始化
main_win = pg.display.set_mode((600, 400))  # 实例化主窗体，设置大小
pg.display.set_caption('主窗体名称')     # 设置主窗体名称

# 循环获取事件并响应
while True:
    for event_i in pg.event.get():   # 不断获取事件列表
        if event_i.type == pg.QUIT:  # 获得事件类型；QUIT是pygame中定义的退出事件常量
            sys.exit()
    pg.display.update()             # 刷新屏幕，默认窗口全部重绘
```

### 第1-2
pygame中图像的基本使用
ball = pg.image.load(ball_image)    # 载入图像，实例化为一个surface对象
ball_rect = ball.get_rect()         # get_rect()获得surface对象外切的矩形对象
Rect对象有表示这个矩形的上、下、左、右、宽度、高度等很多属性

### 第1-3
屏幕帧率设置

### 第1-4
响应键盘的操作


## 第二章
