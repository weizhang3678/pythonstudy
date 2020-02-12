'''
Created on Feb 12, 2020

@author: zhangwei
'''
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
if num1 < num2:
    print("First number is less than second number!")
elif num1 > num2:
    print("First number is greater than second number!")
else:
    print("First number is equal to second number!")
if num1 != num2:
    print("First number is not equal to second number!")

if num1 > 20 and num2 > 20:
    print("First number and second number are both greater than 20!")
if num1 > 20  or num2 > 20:
    print("One of first number and second number is greater than 20!")
if not(num1 > 20 and num2 > 20):
    print("First number and second number are both less than 20!")