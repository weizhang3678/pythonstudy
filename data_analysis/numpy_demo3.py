'''
access array
'''

import numpy as np

# access list elements
var = [[1,2,3],[3,4,5],[5,6,7]]
print(var[0][0])

# access
arr1 = np.full((3,3),9.9, dtype=float)
print(arr1[0])
print(arr1[0][0])

# access
arr2 = np.array(var)
print(arr2[-1][0])

# another method to access
print(arr2[-1,0])

# array slice
print(arr1[:2,:1])

# dimension
print(arr2.ndim)
print(arr2.shape)
print(arr1.size)
print(arr1.dtype)
print(arr1.itemsize)
print(arr1.nbytes)
