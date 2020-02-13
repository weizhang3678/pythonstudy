'''
Created on Feb 13, 2020

@author: zhangwei
'''
import time
import random
# 让用户注册
name = input('input your name：')
age = input("Hello {}, how old are you? ".format(name))
user_info = {'name': name, 'age': int(age)}  
user_properties = ['X 1-5']  # save tools
properties = ['X3 (250G)', 'X1-5 (300G)']  # tools

# assign coins base on your age
if 10 < user_info['age'] < 18:
    glod = 1000
elif 18 <= user_info['age'] <= 30:
    glod = 1500
else:
    glod = 500
user_info['glod'] = glod


print("Hello {}，welcome to this game，you have initial coins：{} ".format(user_info['name'], user_info['glod']))
print("\n")
time.sleep(1)
print('game introduction'.center(50, '*'))
print('*'.ljust(53), '*')
print('*', end='')
print("Computer will toss 3 dices，if sum of marks >= 10 the result is big，otherwise, the result is small".center(32), end='')
print('*')
print('*'.ljust(53), '*')
print('*' * 54)
print("\n")


result = input('start a game? yes or no :  ')
go = True
if (result.lower() == 'yes'):
    while go:
        dices = []
     
        for i in range(0, 3):
            dices.append(random.randint(1, 6))
        total = sum(dices) 
        user_input = input('please input big OR small : ')  
        u_input = user_input.strip().lower()
        time.sleep(1)
       
        print('marks：{}'.format(dices), end=' ')
        if (total >= 10 and u_input == 'big') or (total < 10 and u_input == 'small'):
            print('you win!!!')
            multi = 1  
            if len(user_properties) > 0:  
                use_pro = input('use tool or not： ')
                if use_pro.lower() == 'yes':
                    use_pro = int(input('choose which tool you want to use{} ：'.format(user_properties)))
                    use_pro -= 1
                    if user_properties[use_pro] == 'X 3':
                        multi = 3
                        print('3 times of reward')
                    elif user_properties[use_pro] == 'X 1-5':
                        multi = random.randint(1, 5)
                        print('{} times of reward'.format(multi))
                    user_properties.remove(user_properties[use_pro])  

            user_info['glod'] += 100 * multi;  
        else:
            print('You lose!')
            user_info['glod'] -= 100;  

       
        if (user_info['glod'] <= 0):
            print('You coins is used out. Thanks for your playing')
            break

        if user_info['glod'] % 1000 == 0:  
            shop = input('Currently you have coins:{}，do you want to buy tools? yes or no: '.format(user_info['glod']))
            if shop.lower() == 'yes':
                good_num = int(input('Which one do you want to buy {}'.format(properties)))
                if good_num == 1:
                    user_properties.append('X 3') 
                    user_info['glod'] -= 250
                    print('successful！use 250 coins')
                elif good_num == 2:
                    user_properties.append('X 1-5') 
                    user_info['glod'] -= 300 
                    print('successful！use 300 coins')
                else:
                    print('There are no this kind of tool. You waste a opportunity!')
        else:
            # conti = input('Currently you have coins:{}，continue to play this game? yes or no: '.format(user_info['glod']))
            print('Currently you have coins:{} '.format(user_info['glod']))
else:
    print('Bye！')
