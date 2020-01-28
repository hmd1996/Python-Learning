class Gun:
    def __init__(self,model):
        self.model = model
        self.bullte_count = 0

    def add_bullet(self,count):
        self.bullte_count += count
    def shoot(self):
        if self.bullte_count <= 0:
            print('[%S]没子弹啦！'%self.model)
            return
        self.bullte_count -= 3
        print('突突突。。。[子弹还剩[%d]]'%self.bullte_count)


class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None
    def fire(self):
        if self.gun is None:
            print('%s还没有枪哦'%self.name)
            return
        print('[%s]!冲啊！！！'% self.name)

        # self.gun.add_bullet(50)
        self.gun.shoot()
# 创建枪对象
ak47 = Gun('AK47')
ak47.add_bullet(50)
# 创建许三多
xsd = Soldier('许三多')
xsd.gun = ak47
print(xsd.gun)
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()
xsd.fire()