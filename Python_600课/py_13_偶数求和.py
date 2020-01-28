i = 0
x = int(input('请输入一个整数'))
result = 0
while i <= x:
    if i % 2 ==0:
        result += i
        i += 1
    else:
        i += 1
print('0~%d的所有偶数相加的和为%d'%(x,result))
