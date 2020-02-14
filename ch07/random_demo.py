'''
Created on Feb 13, 2020

@author: zhangwei
'''

import random
num = random.random()
print(num)

num = random.randint(0,100)
print(num)

list = ['Diamond VIP', 'Gold VIP', 'Silver VIP', 'Not a Member'] 
type = random.choice(list)
print(type)