'''
+ = add()，
- = subtract()，
* = multiply()
/ = divide()
// = floor_divide
** = power
% = np.mod
sin()
cos()
...
'''

import numpy as np
arr1 = np.array(list(range(10)))
print(arr1)
arr2 = arr1 + 10
print(arr2)
print(arr1*10)


arr3 = np.full((3,3), 1.0, dtype=float)
arr4 = arr3 + 10
print(arr3)
print(arr4)

arr5 = np.linspace(0, np.pi, 20)
print(arr5)
b = np.sin(arr5)
print(b)

