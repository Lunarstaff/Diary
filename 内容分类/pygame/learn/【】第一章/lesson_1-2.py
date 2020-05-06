# 图像的基本使用
import pygame as pg, sys

# 初始化
pg.init()
main_win_size = width, height = 600, 400
speed = [1, 1]
BLACK = 0, 0, 0
main_win = pg.display.set_mode(main_win_size)
pg.display.set_caption("主窗体名称")
ball_image = "../resources/EggBlue.png"
ball = pg.image.load(ball_image)    # 载入图像，实例化为一个surface对象
ball_rect = ball.get_rect()         # get_rect()获得surface对象的外切矩形

# 循环
while True:
    for event_i in pg.event.get():
        if event_i.type == pg.QUIT:
            sys.exit()
    ball_rect = ball_rect.move(speed[0], speed[1])
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    # 更新屏幕
    main_win.fill(BLACK)    # 小球移动过的地方，系统默认会填充白色
    main_win.blit(ball, ball_rect) # 将一个图像绘制在另一个图像上，使小球的图像一直绘制在Rect对象的矩形内
    pg.display.update()