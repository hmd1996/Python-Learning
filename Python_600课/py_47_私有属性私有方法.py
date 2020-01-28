class Women:
    def __init__(self,name,__age):
        self.name = name
        self.__age = __age
    def __secret(self):
        print('%s的年龄是%d'% (self.name,self.__age))

xiaofang = Women('小芳',60)
xiaofang._Women__secret()
print(xiaofang._Women__age)