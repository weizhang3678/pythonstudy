t1 = tuple()
t2 = ()

my_tuple=(1,2,3,1,'1','33','a')
print(type(my_tuple))

a_tuple = 10,120,33,55,'66'
print(type(a_tuple))

print(my_tuple.count('1'))
print(my_tuple.index(1))

a=()
print(type(a))
a=(1)
print(type(a))
a=(1,)
print(type(a))