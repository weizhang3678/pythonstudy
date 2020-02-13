'''
Created on Feb 12, 2020

@author: zhangwei
'''


mix = [3,6,5,78,44,67,47,33]
mix.sort()
print(mix)

mix.reverse()
print(mix)

mix.sort(reverse = True)
print(mix)


cities = ["Paris","London","New York","Peking","Toronto"]
# a new reference
new = cities
cities.sort(reverse=True)
print(new)

cities.sort()
print(new)

# if you only want a copy of array
anothernew = cities[:]