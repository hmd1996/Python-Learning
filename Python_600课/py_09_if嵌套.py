train_ticket = str(input('手里拿什么'))

if train_ticket == '火车票':
    package = str(input('行李是否有违禁物品？（yes/no）'))
    if package == 'yes':
        print('收缴')
    else:
        print('通过安检，可以进入')
else:
    print('get out!')