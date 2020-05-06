'''
np.reshape
np.sort
np.concat
'''

import numpy as np

# reshape
arr1 = np.full((2,10), 1, dtype = float)
print(arr1)
arr2 = arr1.reshape(10,2)
print(arr2)

# sort
arr3 = np.array([
    [11,2,32],
    [47,52,16],
    [71,8,19]
    ])
print(arr3)
print(np.sort(arr3))
print(arr3.sort(axis = 0))
print(arr3)

# concat
arr4 = np.array([[1,2,3]])
print(np.concatenate((arr4,arr3),axis = 0))

