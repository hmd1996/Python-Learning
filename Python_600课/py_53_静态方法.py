class Dog(object):
    @staticmethod
    def run():
        print('跑跑跑')
    def __init__(self,name):
        self.name = name

Dog.run()
dog = Dog('wangcai')
print(dog.name)