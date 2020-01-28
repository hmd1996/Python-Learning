def sum_number(*args):
    num = 0
    print(args)
    for n in args:
        num += n
    return num
result = sum_number(1,2,3,4,5 )
print(result)