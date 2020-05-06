# bullet.py
import pygame
from pygame.sprite import Sprite
 

class Bullet(Sprite):
    def __init__(self, set_args, screen, ship):
        """
            set_args:设置参数
            screen:要显示在的surface对象
            ship:是哪个飞机的
        """
        super().__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形,再设置正确的位置
        self.rect = pygame.Rect(0, 0, set_args.bullet_width,
                                set_args.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 子弹的位置(y坐标),浮点型
        self.y = float(self.rect.y)
        self.color = set_args.bullet_color
        self.speed_factor = set_args.bullet_speed_factor

    # 更新飞机子弹
    def update(self):
        # 更新表示子弹y坐标的小数的值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    # 绘制飞机子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
