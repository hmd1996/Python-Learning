xiaoming = {"name" :'小明',
            'age': 18,
            'gender':True,
            'height':1.75,
            'weight':142.23}
print(xiaoming)

# 取值
print(xiaoming["name"])
# 增加/修改
xiaoming['age'] = 15
print(xiaoming)
# 删除
xiaoming.pop('height')
print(xiaoming)

# 统计键值对数量
print(len(xiaoming))
# 合并字典
test_dic = {'height':1.75}
xiaoming.update(test_dic)
print(xiaoming)
# 清空字典
xiaoming.clear()
print(xiaoming)