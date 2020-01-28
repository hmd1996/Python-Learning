class Animal:
    def __init__(self):
        pass
    def eat(self):
        print('吃吃吃')
    def drink(self):
        print('喝喝喝')
    def run(self):
        print('跑跑跑')
    def sleep(self):
        print('睡睡睡')


class Dog(Animal):
    def bark(self):
        print('汪汪汪')

class XiaoTianQuan(Dog):
    def fly(self):
        print('我会飞')
dog = XiaoTianQuan()

dog.fly()