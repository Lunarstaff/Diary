# game_stats.py
class GameStats():
    def __init__(self, set_args):
        self.set_args = set_args
        self.reset_stats()

        # 游戏状态
        self.game_active = False # 游戏一开始为非活动状态

    def reset_stats(self):
        self.ship_left = self.set_args.ship_limit
        # 游戏实时得分
        self.score = 0
