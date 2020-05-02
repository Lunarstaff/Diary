# alien.py
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, set_args, screen):
        super().__init__()
        self.screen = screen
        self.set_args = set_args

        # 加载外星人图片
        self.image = pygame.image.load(set_args.alien_image_path)
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # 更新外星人位置
    def update(self):
        # 更新表示外星人y坐标的小数的值
        self.y += self.set_args.alien_speed_factor
        # 更新表示外星人的rect的y坐标
        self.rect.y = self.y

    # 在指定位置绘制外星人
    def blitme(self):
        self.screen.blit(self.image, self.rect)
