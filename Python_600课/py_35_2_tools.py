card_list = []


def show_menu():
    print('*********名片管理系统*********')
    print('1.新建名片')
    print('2.显示全部名片')
    print('3.查询名片')
    print('0.退出系统')
    print('****************************')

def new_card():
    print('----------------------------')
    print('||         新增名片         ||')
    print('----------------------------')
    # 提示用户输入名片信息
    name_str = input('请输入姓名:')
    phone_str = input('请输入手机号:')
    qq_str = input('请输入qq:')
    # 使用用户输入的信息建立字典
    card_dict = {'name' : name_str,
                'phone' : phone_str,
                'qq' : qq_str}
    # 将字典添加到列表
    card_list.append(card_dict)
    print(card_list)
    # 提示用户输出成功
    print('添加%s的名片成功！'%name_str)

def show_all():
    print('----------------------------')
    print('||       显示所有名片       ||')
    print('----------------------------')
    # 判断是否存在名片记录，如果没有，提示用户并返回
    if len(card_list) == 0:
        print('无名片，请使用新增功能！')
    else:
        # 打印表头
        for name in ['姓名','电话','qq']:
            print(name, end='\t\t')
        print('')
        # 打印分割线
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        # 遍历字典
        for card_dirt in card_list:
            print("%s\t\t%s\t\t%s" % (card_dirt['name'],
                                      card_dirt['phone'],
                                      card_dirt['qq']))

def search_card():
    print('----------------------------')
    print('||        搜索名片         ||')
    print('----------------------------')

    # 提示用户输入要搜索的名字
    find_name = input('请输入您要搜索的姓名：')

    # 遍历列表，查询，如果没有，提醒用户
    for card_dirt in card_list:
        if card_dirt['name'] == find_name:
            print('姓名\t\t电话\t\tqq\t\t')
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
            print("%s\t\t%s\t\t%s" % (card_dirt['name'],
                                      card_dirt['phone'],
                                      card_dirt['qq']))

            # TODO 针对找到的名片记录增加修改和删除的功能
            deal_card(card_dirt )
            break
    else:
            print('没找到%s'%(find_name))

def deal_card(find_dict):
    action_str = input('请输入对名片的操作'
                       '【1】：修改   【2】：删除   【0】：返回上一级')

    if action_str == '1':
        find_dict['name'] = input_card_info(find_dict['name'],'姓名：')
        find_dict['phone'] = input_card_info(find_dict['phone'],'phone：')
        find_dict['qq'] = input_card_info(find_dict['qq'],'qq：')
        print('修改成功！')
    elif action_str == '2':
        card_list.remove(find_dict)
        print('删除成功！')

def input_card_info(dict_value,tip_message):
    """
    输入名片信息
    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容，就返回内容，否则就返回原有值
    """

    # 提示用户输入内容
    result_str = input(tip_message)
    # 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
    # 如果用户没有输入，返回字典原有的值
    pass
