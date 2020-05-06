###numpy
'''
1. array VS list
list: store different types data
array: same type
2. import array
3. import numpy
'''

import array
import numpy as np
a1 = array.array('i', range(10))
# a1[1] = 'aa'  not valid
print(a1[0])

# from list to array
a_list = range(10)
a2 = np.array(a_list)
type(a2)

# generate array
a3 = np.zeros(10)
print(type(a3))
print(a3.dtype)

# generate int array
a4 = np.zeros(10, dtype = int)
print(a4.dtype)

# multi-dimension
a5 = np.ones((4,4), dtype = int)
print(a5)
print(a5.dtype)

# specific value
a6 = np.full((3,3), 3.14)
print(a6)
print(a6.dtype)

# like
a7 = np.full_like(a6, 4.2)
#a7 = np.full_like(a6, 4.2, dtype = float)
print(a7)
print(a7.dtype)

