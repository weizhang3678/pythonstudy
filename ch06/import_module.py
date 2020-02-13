'''
Created on Feb 13, 2020

@author: zhangwei
'''
import os
from ch06 import person_5
from ch05 import math_functions

print(os.path.abspath(__file__))

print(person_5.mary)

ss = math_functions.summary(100)
print(ss)