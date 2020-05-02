# game_function.py
import pygame
import sys
from bullet import Bullet
from alien import Alien
from random import randint
from time import sleep

# 按键按下
def check_keydown_events(event, set_args, screen, ship, bullets):
    if event.key == pygame.K_RIGHT: # 如右箭头键被按下
        ship.moving_right = True  # 飞机的移动标志置为True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:   # 如空格键被按下
        # ship.fire_flag = True
        ship_shot(set_args, screen, ship, bullets)


# 按键释放
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT: # 如右箭头键被释放
        ship.moving_right = False # 飞机的移动标志置为False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    # elif event.key == pygame.K_SPACE:
        # ship.fire_flag = False

# 检查鼠标键盘事件
def check_events(set_args, screen, stats,scoreboard,  
    play_button, ship_o, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 检查到关闭，退出游戏
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, set_args, screen, ship_o, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship_o)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(set_args, screen, stats, scoreboard, play_button, ship_o, aliens, bullets, mouse_x, mouse_y)

    ship_shot_con(set_args, screen, ship_o, bullets)

def check_play_button(set_args, screen, stats, scoreboard, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        # 当点击开始按钮 开始游戏
        button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_click and not stats.game_active:
            # 重置游戏速度
            set_args.initialize_dynamic_settings()

            # 隐藏光标
            pygame.mouse.set_visible(False)

            # 重置游戏统计信息
            stats.reset_stats()
            stats.game_active = True

            # 开始时绘制新的分数
            scoreboard.prep_score()

            # 清空外星人和子弹列表
            aliens.empty()
            bullets.empty()




# 飞机开火
def ship_shot(set_args, screen, ship, bullets):
    # 创建一发子弹，并将其加入到子弹编组bullets中
    # 创建子弹前，检查当前同屏子弹数量是否超过上限
    if len(bullets) < set_args.bullets_allowed:
        new_bullet = Bullet(set_args, screen, ship)
        bullets.add(new_bullet)
    
# 飞机连续开火
def ship_shot_con(set_args, screen, ship, bullets):
    # 创建一发子弹，并将其加入到子弹编组bullets中
    # 创建子弹前，检查当前同屏子弹数量是否超过上限
    if ship.fire_flag:
        new_bullet = Bullet(set_args, screen, ship)
        bullets.add(new_bullet)

# 更新飞机子弹的位置，删除已消失（超出屏幕显示）的子弹
def update_bullets(set_args, screen, stats, scoreboard, ship, aliens_group, bullets_group):
    # 子弹显示
    bullets_group.update()
    # 删除已消失（超出屏幕显示）的子弹
    for bullet in bullets_group.copy():
        if bullet.rect.bottom <= 0:
            bullets_group.remove(bullet)
    # 调试用 显示当前编组中有多少子弹
    # print("len(bullets_group)----" + str(len(bullets_group)))

    # 检查是否有子弹击中了外星人，如果是就删除对应的子弹和外星人
    collisions = pygame.sprite.groupcollide(
        bullets_group, aliens_group, True, True)
    '''
    遍历编组bullets中的每颗子弹，再遍历编组aliens中的每个外星人。
    每当有子弹和外星人的rect重叠时，groupcollide()就在它返回的字典中添加一个键值对.
    两个实参True告诉Pygame删除发生碰撞的子弹和外星人
    '''    

    # 每当有外星人消灭，分数增加
    if collisions:
        # 遍历字典collisions，确保将消灭的每个外星人的点数都记入得分 ？
        for alien_i in collisions.values():
            '''
            字典collisions的每个值都是一个列表，包含被同一颗子弹击中的所有外星人。
            对于每个列表，都将一个外星人的点数乘以其中包含的外星人数量，并将结果加入到当前得分中。
            为测试这一点，请将子弹宽度改为300像素，并核实你得到了更宽的子弹击中的每个外星人的点数，再将子弹宽度恢复到正常值
            '''
            stats.score += set_args.alien_point * len(alien_i)
            # 更新记分板的分数图像
            scoreboard.prep_score()

# 计算每行可容纳外星人的数量
def get_number_aliens_x(set_args, alien_width):
    alien_space_x = set_args.screen_width - 2 * alien_width # 每行可用的空间
    # 每行外星人数量
    alien_num_x = int(alien_space_x / (2 * alien_width))
    return alien_num_x

# 获取屏幕上可容纳多少行外星人
def get_alien_row(set_args, ship_height, alien_height):
    available_space_y = (
        set_args.screen_height - (3 * alien_height) - ship_height
        )
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

# 创建单个外星人
def creat_alien(set_args, screen, aliens, alien_num, row_num):
    alien = Alien(set_args, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
    aliens.add(alien)


# 随机创建单个外星人
def creat_alien_random(set_args, screen, aliens, pos_row):
    alien = Alien(set_args, screen)
    alien_width = alien.rect.width
    alien.x = ((pos_row-1) * 2 + 2) * alien_width
    alien.y = alien_width / 2 + randint(1, 5) * (alien_width/2)
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)
    # 调试
    # print("##################")
    # print("pos_row-----------" + str(pos_row))
    # print("alien.rect.x-----------" + str(alien.rect.x))
    

# 创建一组外星人
def creat_fleet(set_args, screen, ship, aliens):
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(set_args, screen)
    alien_num_x = get_number_aliens_x(set_args, alien.rect.width)
    number_rows = get_alien_row(
        set_args, ship.rect.height, alien.rect.height
        )
    # print("number_rows----" + str(number_rows))
    # print("alien_num_x----" + str(alien_num_x))
    for row_number in range(number_rows):
        for alien_number in range(alien_num_x):
            creat_alien(set_args, screen, aliens, alien_number, row_number)

# 创建随机的外星人组
def creat_random_alien_group(set_args, screen, ship, aliens):
    alien = Alien(set_args, screen)
    # 每行最多可显示多少个
    row_max =  get_number_aliens_x(set_args, alien.rect.width)
    # 进入循环前给一个位置参考
    pos_row = 1
    for pos_i in range(row_max):
        if randint(0,1):
            creat_alien_random(set_args, screen, aliens, pos_row)
        pos_row += 1 
           


# 更新外星人的位置，删除超出屏幕的外星人
def update_aliens(aliens_group, set_args, screen, ship, game_stats, bullets):
    aliens_group.update()
    # 删除已消失的外星人
    for alien in aliens_group.copy():
        # 这里是删除外星人的条件
        if alien.rect.bottom > set_args.screen_height: 
            aliens_group.remove(alien)
        if pygame.sprite.spritecollideany(ship, aliens_group):
            ship_hit(set_args, game_stats, screen, ship, aliens_group, bullets)
    # 调试用 显示当前编组中有多少子弹
    # print("len(aliens_group)----" + str(len(aliens_group)))
    
    
# 更新屏幕
def update_screen(
    set_args, screen, stats, scoreboard, ship, aliens, 
    bullets, play_button):
    # 每次游戏循环都重绘屏幕
    screen.fill(set_args.bg_color)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)

    # 显示得分
    scoreboard.show_score()

    # 如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


# 飞机被撞毁
def ship_hit(set_args, game_stats, screen, ship, aliens, bullets):
    # 飞机被撞后的响应
    if game_stats.ship_left > 1:
        # 1- 剩余减1
        game_stats.ship_left -= 1

        # 2- 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 3- 重置游戏 不重置分数
        creat_random_alien_group(set_args, screen, ship, aliens)
        ship.center_ship()

        # 4- 游戏暂停一会儿
        sleep(2)
    else:
        # 游戏状态为False
        game_stats.game_active = False

        # 显示光标
        pygame.mouse.set_visible(True)
    
