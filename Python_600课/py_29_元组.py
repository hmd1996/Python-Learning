info_tuple = ('zhangsan','lisi','wangwu')

print(info_tuple.count('zhangsan'))
print(info_tuple.index('zhangsan'))
print(len(info_tuple))

for item in info_tuple:
    print(item)

infomation = ('zhangsan',18,1.75)
print("%s年龄是%d身高是%.2f"%infomation)

listexchange = list(info_tuple)
print(listexchange)