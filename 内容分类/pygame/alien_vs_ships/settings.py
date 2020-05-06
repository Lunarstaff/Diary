# Settings

class Settings():
    """
    存储所有的设置类
    """
    def __init__(self):
        """
        初始化游戏的静态设置
        """
        self.game_title_name = "飞机大战1.0"
        self.screen_width = 450
        self.screen_height = 750
        self.bg_color = (112, 146, 190) 
        self.bg_image_path = "resources/"
        
        # 飞机设置
        # 飞机数量
        self.ship_limit = 3
        
        # 子弹设置
        # self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (237, 28, 36)
        # self.bullet_image_path = "resources/bullet_001.png"
        self.bullets_allowed = 5 # 同屏子弹最大数量

        # alien设置
        self.alien_image_path = "resources/alien_001.png"
        self.alien_speed_factor = 0.2

        # 游戏加速因子
        self.speedup_scale = 1.5

        # 初始化活动参数
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''
        初始化活动参数
        '''
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.5

        # 每击落一个外星人得分
        self.alien_point = 1

    def speed_up(self):
        '''
        随着游戏的进行(当游戏分数达到某一数值时) 加速
        '''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
