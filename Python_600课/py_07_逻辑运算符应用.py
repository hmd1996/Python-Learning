age = int(input('请您输入您的年龄'))

if age <0 or age > 120:
    print('怪胎？')
elif age >= 0 and age <=18:
    print('您还不能进网吧哟')
else:
    print('网吧欢迎您！')

is_vip = False

if not is_vip :
    print('不是VIP')