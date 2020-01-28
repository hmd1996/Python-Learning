class Dog(object):
    def __init__(self,name):
        self.name = name

    def game(self):
        print('%s玩玩玩'%self.name)


class Xiaotianquan(Dog):
    def game(self):
        print('%s上天玩玩玩玩玩'%self.name)


class Person(object):
    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):
        print('%s和%s快乐的玩耍'%(self.name,dog.name))
        dog.game()

wangcai = Dog('旺财')
xiaoming = Person('小明')
xiaotian = Xiaotianquan('飞天犬')
xiaoming.game_with_dog(xiaotian)