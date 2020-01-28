def sum_two_number(number1,number2):#这两个为形参，形参接收数据，作为变量使用
    """对两个数字的求和"""

    result = number1 + number2
    print("%d + %d = %d"%(number1,number2,result))

sum_two_number(20,30)#这两个叫实参，用来把数据传到函数内部