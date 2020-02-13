'''
Created on Feb 13, 2020

@author: zhangwei
'''

import random  #导入随机模块

num = 1
yin_num = 0
shu_num = 0
while num <= 3:
    if shu_num == 2 or yin_num == 2:
        break
    user = int(input('Please punch out: 0（Rock） 1（Scissor） 2（Paper）'))
    if user > 2:
        print('no more than 2')
    else:
        data = ['Rock', 'Scissor', 'Paper']
        com = random.randint(0, 2)
        print("You are {}，and PC is {}".format(data[user], data[com]))
        if user == com:
            print('This is a draw.')
            continue
        elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com == 0):
            print('You win!')
            yin_num += 1
        else:
            print('You lose!')
            shu_num += 1
    num += 1
