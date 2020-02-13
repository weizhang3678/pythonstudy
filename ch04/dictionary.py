'''
Created on Feb 13, 2020

@author: zhangwei
'''
# method 1 to assign value
phone = {}
phone['Mary'] = 3065153678
phone['Bob'] = 306391888
phone['Julia'] = 78799990103
print(phone)

# method 2 to assign value

phone = { 'Mary' : 3065153678 , 'Bob' : 306391888, 'Julia': 78799990103 }
print(phone)


names = phone.keys()
numbers = phone.values()
items = phone.items()
print(names)
print(numbers)
print(items)

for key in sorted(phone.keys()):
    print(key, phone[key])
    
for value in sorted(phone.values()):
    for key in phone.keys():
      if phone[key] == value:
          print(key, value)
          continue; 
      
# find out if a key exist
print('Bob' in phone)      
      
# delete 
del phone['Mary']
# delete all
phone.clear()
 
 

