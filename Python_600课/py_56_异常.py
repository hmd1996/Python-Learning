try:
    num = int(input('请输入整数'))
    result = 8/num
    print(result)
except ValueError:
    print('输入类型错误！')
except ZeroDivisionError:
    print('输入数字不能为零')
except Exception as result:
    print('未知错误%s'% result)
else:
    print('尝试成功')
finally:
    print('一定出')