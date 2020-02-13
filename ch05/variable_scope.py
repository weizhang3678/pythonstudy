'''
Created on Feb 13, 2020

@author: zhangwei
'''

my_price = 100

def  calculatePrice(price, tax_rate):
    my_price = 150
    return price * (1 + tax_rate)

print(my_price)
calculatePrice(100, 0.13)
print(my_price)


my_price = 100

def  calculatePrice_1(price, tax_rate):
    print(my_price)
    return price * (1 + tax_rate)

calculatePrice(100, 0.13)


def  calculatePrice_2(price, tax_rate):
    global my_price # tell python use global variables ？？
    my_price = 150
    return price * (1 + tax_rate)

print(my_price)
calculatePrice(100, 0.13)
print(my_price)
