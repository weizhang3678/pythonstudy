'''
Created on Feb 14, 2020

@author: Zhang Wei
'''
import random

coin = ["Head", "Tail"]
heads_num = 0
tails_num = 0
for i in range(100000):
    if random.choice(coin) == "Head":
        heads_num += 1
    else:
        tails_num += 1

print('We got head %i times and tail %i times in 100000 tries.' %(heads_num, tails_num))
