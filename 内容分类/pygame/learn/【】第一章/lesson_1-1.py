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
