class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return '我的名字是%s 体重是 %.2f公斤'% (self.name,self.weight)
    def run(self):
        self.weight -= 0.5
    def eat(self):
        self.weight +=1
xiaoming = Person('小明',75)
xiaomei = Person('小美',45)
xiaoming.run()
xiaoming.eat()
xiaoming.eat()
xiaomei.run()
xiaomei.run()
print(xiaoming)
print(xiaomei)