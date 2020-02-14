'''
Created on Feb 13, 2020

@author: zhangwei
'''
import pickle
from ch06 import inheritance

s = inheritance.Square(5)

with open('test', 'wb') as f:
    pickle.dump(s, f)
    
f.close()

with open('test', 'rb') as f:
    s = pickle.load(f)   
    print(s.getPerimeter())
    print(s.getArea())