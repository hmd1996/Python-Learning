row = 1
while row <= 9:
    col = 1
    while col <= row:
        result = row * col
        print('%d*%d=%d'%(col,row,result),end=' ')
        col += 1
    print('')
    row += 1