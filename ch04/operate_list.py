'''
Created on Feb 12, 2020

@author: zhangwei
'''
grades = ["G1","G2","G3","G4","G5","G6"]
mix = [3,6,5,"Good",grades]
print(mix)

# modify
mix[1] = "Happy"

# add element
mix.append("Who am I")
mix.extend(["Paris","London"])
mix.insert(0, "New York")
print(mix)

#delete element
mix.remove("Good")
del mix[0]
print(mix)

#pop
e = mix.pop()
print(e)
print(mix)

e = mix.pop(1)
print(e)
print(mix)