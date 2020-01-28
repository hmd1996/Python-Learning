gl_list = [6,3,9]
# 升序,revere为缺省参数，为false
gl_list.sort()
print(gl_list)
# 降序
gl_list.sort(reverse=True)
print(gl_list)

# 缺省参数应该在末尾 
def print_info(name,gender=True):
    """

    :param name: 同学姓名
    :param gender: True男，False女
    """
    gender_text = '男生'
    if not gender:
        gender_text = '女生'
    print('%s是%s'%(name,gender_text))
print_info('小明')
print_info('小妹',False)