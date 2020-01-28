# 普通版
# apple_number = input('购买苹果的个数：')
# apple_price = input('苹果的单价:')
# apple_sumprice = int(apple_number) * float(apple_price)
# print('您一共需要支付：' + str(apple_sumprice) + '元')

# 改进版
apple_number = int(input('请输入苹果数量：'))
apple_price = float(input('请输入苹果的单价：'))
apple_sumprice = apple_number * apple_price
print('您一共需要支付：' + str(apple_sumprice) + '元')