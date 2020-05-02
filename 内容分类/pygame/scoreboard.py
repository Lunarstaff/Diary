# scoreboard.py

import pygame.font

class Scoreboard(object):
    """记分板"""
    def __init__(self, set_args, screen, stats):
        """初始化分数和一些属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.set_args = set_args
        self.stats = stats

        # 显示分数的字体属性
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # 将 要显示的分数 转换成图像
        self.prep_score()


    def prep_score(self):
        """
        将 要显示的分数 转换成图像
        """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.set_args.bg_color)

        # 将分数图像放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        """在屏幕上显示分数"""
        self.screen.blit(self.score_image, self.score_rect)
      