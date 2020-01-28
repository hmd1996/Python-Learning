class Cat:
    def __init__(self,new_name):
        self.name = new_name
        print('%s我来了'%self.name)
    def __del__(self):
        print('%s我没了'%self.name)
    def __str__(self):
        return "我是小猫:%s" % self.name
tom = Cat('tom')
print(tom)