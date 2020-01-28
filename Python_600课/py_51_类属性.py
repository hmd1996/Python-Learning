class Tools(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Tools.count +=1

tool1 = Tools('斧头')
print(Tools.count)