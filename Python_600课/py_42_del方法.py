class Cat:
    def __init__(self,new_name):
        self.name = new_name
        # self.name = 'tom'
    def eat(self):
        print('%s爱吃鱼'%self.name)
    def __del__(self):
        print('%s 我没了'%self.name)
tom = Cat('tom')
lazy_cat = Cat('lazycat') 
tom.eat()
lazy_cat.eat()
