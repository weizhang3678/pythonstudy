list1 = zip([1,2,3,4],['2','3'])
print(list1)
list1 = list(list1)
print(list1)
dict1 = dict(list1)
print(dict1)

names=['Maty', 'Bob', 'Lin']
dict2 = dict.fromkeys(names)
print(dict2)
print(dict2['Bob'])
print(dict2.get('Bob',100))
print(dict2)

dict2.pop('Bob')
print(dict2)

dict2['Lin'] = 200
dict2.setdefault('Maty', 1000)
dict2['Mary'] = 1000
print(dict2)