'''
Created on Feb 13, 2020

@author: zhangwei
'''


def summary(n):
    number = 0;
    for i in range(n+1):
        number = number + i;
    return number

number = summary(100)  
print("the addition from 0 to 100 is " , number)


def max(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2
max = max(35*25,46*13)
print( max)