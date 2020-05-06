'''
==  np.equal
< np.less
> np.greater
np.all
np.any
'''
import numpy as np

# numpy sum VS sum
# numpy.sum is faster than sum
arr1 = np.full((2,3),2.3)
arr2 = np.array(list(range(10)))
arr3 = np.array([[1,2],[3,4]])
print(sum(arr1))
print(sum(arr2))
print(sum(arr3))
print(np.sum(arr1))
print(np.sum(arr2))
print(np.sum(arr3))
print(np.sum(arr3, axis= 1))
print(np.max(arr3, axis= 1))

# notebook:%timeit check program
#%timeit sum(arr1)

# >,<,!=.==
print(arr1 > 2)

print(np.all(arr1>-1))
print(np.any(arr1>-1))