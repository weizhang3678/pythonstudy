'''
Created on Feb 12, 2020

@author: zhangwei
'''

# list is mutable
grades = ["G1","G2","G3","G4","G5","G6"]
scores =[79,90,77,89,97,100,99,100]
mix = [3,6,5,"Good",grades]

friends = []
friends = list()
friends.append("Mary")
print(friends)
friends.append("Rose")
print(friends)
print(friends[1])

friends[0] = 'wei'
print(grades[::-1])
print(type(friends))

print(scores + grades)
print(scores)
scores.extend(grades)
print(scores)
print(len(friends))
scores.clear()
print(scores)

new_scores = grades.copy()
print(id(new_scores))
print(id(grades))
print(new_scores)