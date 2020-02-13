'''
Created on Feb 12, 2020

@author: zhangwei
'''
grades = ["G1","G2","G3","G4","G5","G6"]
mix = [3,6,5,"Good",grades]

if "Good" in mix:
    print("find 'Good' in the list")
    print(mix.index("Good"))
else:
    print("can not find 'Good' in the list")
    
print("Good" in mix)