'''
Created on Feb 13, 2020

@author: zhangwei
'''

marymarks=[100,100,100,99]
johnmarks=[90,80,89,98]
tedmarks=[97,98,99,95]
classmarks = [marymarks,johnmarks,tedmarks]
print(classmarks)

for mark in classmarks:
    print(mark)
    
print(classmarks[0])
print(classmarks[1][2])
print(classmarks[4])