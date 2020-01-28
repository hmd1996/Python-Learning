class Cat:
    def eat(self):
        print('%s吃饭饭'%self.name)
    def drink(self):
        print('%s喝水水'%self.name)
tom = Cat()
tom.name = 'tom'
tom.drink()
tom.eat()