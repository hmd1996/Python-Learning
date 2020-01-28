class Dad:
    def english(self):
        print('英语天赋')
class Mum:
    def chinese(self):
        print('语文天赋')
class Son(Dad,Mum):
    def math(self):
        print('数学天赋')
son = Son()
son.chinese()
son.english()
son.math()