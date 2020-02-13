'''
Created on Feb 12, 2020

@author: zhangwei
'''
grades = ["G1","G2","G3","G4","G5","G6"]
mix = [3,6,5,"Good",grades]
print(mix[1:4])
print(mix[4][1:3])

print(mix[1:2])
print(mix[1])

print(type(mix[1:2]))
print(type(mix[1]))

#shorthand
print(mix[:2])
print(mix[2:])
print(mix[:])
print(mix)