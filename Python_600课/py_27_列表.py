name_list = ['heda','songdanyang','wangyuchan']

# 取值
print(name_list[0])


# 取索引
print(name_list.index('songdanyang'))


# 修改
name_list[2] = 'huangpengyuan'
print(name_list)


# 增加
# append方法可以向列表的末尾追加数据
name_list.append('jiangyilun')
print(name_list)

# insert方法可以在列表的指定索引位置插入数据
name_list.insert(1,'sb')
print(name_list)

# extend方法可以把其他列表中的完整内容追加到当前列表末尾
test_list = ['sd','sx']
name_list.extend(test_list)
print(name_list)

# 删除
# remove方法可以从列表中删除指定数据
name_list.remove('heda')
print(name_list)

# pop方法默认把列表中最后一个参数删除
name_list.pop()
print(name_list)

# del方法可以删除列表元素
# del关键字本质上是用来将一个变量从内存中删除的
del name_list[2]
print(name_list)

# clear方法可以清空列表
name_list.clear()
print(name_list)


# 长度
names_list = ['aaa','bbb','ccc','aaa']
list_len = len(names_list)
print(list_len)

# count方法可以统计列表中某一个数据出现的次数
count = names_list.count('aaa')
print('aaa出现了%d次'%count)

# remove：从列表中删除第一次出现的数据，如果数据不存在，程序会报错
names_list.remove('aaa')
print(names_list)

# 排序(升序)
namelist = ['aaa','ddd','eee','aggg']
num_list = [3,23,15,67,43]

namelist.sort()
num_list.sort()
print(namelist)
print(num_list)

# 降序
namelist.sort(reverse=True)
num_list.sort(reverse=True)
print(namelist)
print(num_list)

# 逆序
namelist.reverse()
print(namelist)
print(num_list)