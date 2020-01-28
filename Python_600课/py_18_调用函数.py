def multiple_table():

    row = 1
    number = int(input('请输入一个整数'))
    while row <= number:
        col = 1
        while col <= row:
            result = row * col
            print('%d*%d=%d'%(col,row,result),end=' ')
            col += 1
        print('')
        row += 1