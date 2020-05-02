# Ship
import pygame
import game_function as gf
class Ship():
    def __init__(self, set_args, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ship_seting = set_args # 飞机的设置数据

        # 加载飞机图像并获取其外形矩形
        self.image = pygame.image.load("resources/plane_001.png") # 返回飞机对应的图层
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 飞机的初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom - (self.rect.height)/2

        # 飞机的中心位置改成 浮点数，便于调节速度
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        # 飞机移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.fire_flag = False

    # 更新飞机的位置
    def update(self):
        '''
        根据飞机移动标志调整飞船的位置
        '''
        # 右移之前判断边界
        if self.moving_right and self.rect.centerx < self.screen_rect.right: 
            self.centerx += self.ship_seting.ship_speed_factor
        # 左移之前判断边界
        if self.moving_left and self.rect.centerx > 0: 
            self.centerx -= self.ship_seting.ship_speed_factor
        # 上移
        if self.moving_up and self.centery > 0:
            self.centery -= self.ship_seting.ship_speed_factor

        # 下移
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ship_seting.ship_speed_factor     

        # 飞机连续开火

        
        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    # 在指定的位置画飞机
    def blitme(self):
        self.screen.blit(self.image, self.rect)


    # 重置飞机的位置
    def center_ship(self):
        self.center = self.screen_rect.centerx

