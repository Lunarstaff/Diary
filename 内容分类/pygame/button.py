# button.py
import pygame
class Button():
    """docstring for Button"""
    def __init__(self, set_args, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的属性
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮上的文本
        self.prep_msg(msg)

    def prep_msg(self, msg):
        # 将msg渲染为图像
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        # 获取msg_image 的rect对象
        self.msg_image_rect = self.msg_image.get_rect()
        # 将msg图片置于按钮的中间
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        