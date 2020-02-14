'''
Created on Feb 14, 2020

@author: zhangwei
'''


import random

# toss 2 dices with 6 sides
total_marks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1000):
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    mark = die_1 + die_2
    total_marks[mark] += 1
    
for i in range(2,13):
    print("Mark ", i, "came up", total_marks[i], " times." )
    
print("************************************************")
print("*********** change numbers of dices ************")
print("************************************************")
# toss 1 dice with 12 sides
total_marks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1000):
    die_1 = random.randint(1,12)
    total_marks[die_1] += 1
    
for i in range(1,13):
    print("Mark ", i, "came up", total_marks[i], " times." )