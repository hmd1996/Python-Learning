class Game(object):
    top_score = 0

    def __init__(self,player_name):
        self.player_name = player_name



    @staticmethod
    def show_help():
        print('帮助信息')


    @classmethod
    def show_top_score(cls):
        print('历史记录%d'%cls.top_score)


    def start_game(self):
        print('%s欢迎进入游戏'%  self.player_name)
player = Game('hmd')
Game.show_help()
Game.show_top_score()
player.start_game()
