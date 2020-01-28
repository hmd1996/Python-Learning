string = ' '
print(string.isspace())

num_str = '一'
# 都不能判断小数
print(num_str.isdecimal())#可以判断全角数字
print(num_str.isdigit())#可以判断全角数字、（1）、\uoob2
print(num_str.isnumeric())#可以判断全角数字、汉字数字