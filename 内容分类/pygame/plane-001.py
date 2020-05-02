from sys import exit
from settings import Settings
from ship import Ship
import game_function as gf
import pygame
from pygame.sprite import Group # 用于子弹编组
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    game_setings = Settings()   # 实例化设置

    screen = pygame.display.set_mode(
        (game_setings.screen_width, game_setings.screen_height))  # 对象screen 是一个图层（surface ）
    
    pygame.display.set_caption(game_setings.game_title_name)

    # 创建用于存储游戏数据的实例
    game_stat_data = GameStats(game_setings)

    # 背景颜色
    bg_color = (game_setings.bg_color)

    # 创建一个飞机
    ship_001 = Ship(game_setings, screen) # 入参1为 设置类的对象 入参2为 飞机要显示的地方
    # print("ship_speed" + str(game_setings.ship_speed_factor))

    # 创建一个用于存储子弹的编组
    bullets_of_ship_001 = Group()

    # 创建外星人编组
    alien_group = Group()

    # 创建一个外星人
    # alien_001 = Alien(game_setings, screen)

    # 创建一组外星人
    gf.creat_random_alien_group(game_setings, screen, ship_001, alien_group)

    # 创建Player按钮
    play_button = Button(game_setings, screen, "Game Start")

    # 创建记分板实例
    score_board_000 = Scoreboard(game_setings, screen, game_stat_data)

    # 开始游戏的主循环
    while True:
        # 不停创建外星人
        if len(alien_group) == 0:
            gf.creat_random_alien_group(game_setings, screen, ship_001, alien_group)

        # 监听键盘和鼠标事件
        gf.check_events(game_setings, screen, game_stat_data, score_board_000, play_button, ship_001, alien_group, bullets_of_ship_001)
        if game_stat_data.game_active: # 游戏状态
            ship_001.update()
            # 更新飞机子弹的位置，删除已消失（超出屏幕显示）的子弹，删除击中外星人的子弹，增加得分
            gf.update_bullets(game_setings, screen, game_stat_data, score_board_000, ship_001, alien_group, bullets_of_ship_001)
            # 更新外星人位置
            gf.update_aliens(
                alien_group, game_setings, screen, ship_001, game_stat_data, bullets_of_ship_001)
        
        # 更新屏幕
        gf.update_screen(
            game_setings, screen, game_stat_data, score_board_000, ship_001,
            alien_group, bullets_of_ship_001, play_button)


# 主函数
if __name__ == "__main__":
    run_game()
                
