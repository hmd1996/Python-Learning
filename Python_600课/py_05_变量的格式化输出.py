name = input('请输入你的名字：')
print('我的名字是%s,请多多关照' % name)

student_number = int(input('请输入你的学号：'))
def Print_number():
    print('我的学号是%06d' % student_number)
try:
    Print_number()
except ValueError as result:
    result = '格式错误，您需要输入六位整数！'
    print(result)

apple_number = int(input('请输入购买苹果斤数：'))
apple_price = float(input('请输入苹果每斤的价格'))
apple_sumprice = apple_price * apple_number
print('一共购买%.02f斤苹果，每斤%.02f元，一共%.02f元'%(apple_number,apple_price,apple_sumprice))
