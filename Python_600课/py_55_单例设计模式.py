class Musicplayer(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

player= Musicplayer()
player2 = Musicplayer()
print(player)
print(player2)