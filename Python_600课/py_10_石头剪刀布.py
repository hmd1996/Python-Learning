import random

player = int(input('玩家出，石头（1）剪刀（2）布（3）：'))
computer = random.randint(1,3)
if (player < 1) or (player >3):
    print('只能输入1，2，3哦')
else:
    print('玩家出%d-电脑出%d' % (player, computer))
    if ((player == 1 and computer == 2)
            or (player == 2 and computer == 3)
            or (player ==3 and computer == 1)):
        print('玩家获胜！')
    elif player == computer:
        print('平局！再来一局')
    else:
        print('电脑获胜！')