import py_35_2_tools

while True:
    # TODO 显示系统菜单
    py_35_2_tools.show_menu()

    action_str = input('请选择操作功能：')
    print('您选择的操作是【%s】'%action_str)

    # TODO 增加1,2,3操作
    if action_str in ['1','2','3']:

        if action_str == '1':
            py_35_2_tools.new_card()
        elif action_str == '2':
            py_35_2_tools.show_all()
        elif action_str == '3':
            py_35_2_tools.search_card()
        pass
    elif action_str == '0':
        print('欢迎下次再次使用')
        break
    else:
        print('您输入的不正确，请重新选择')