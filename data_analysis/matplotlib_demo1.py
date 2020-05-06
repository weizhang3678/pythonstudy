'''
matplotlib drawing
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('data.csv')

## notebook
#%matplotlib inline
x = np.linspace(0,10,20)
y = np.sin(x)
plt.plot(x,y)
plt.plot(x,y,'--') # ---
plt.plot(x,y,'o')  # ...
plt.plot(x,y,'o', color='black')  # colors
plt.plot(x,np.cos(x))

fig = plt.figure()
plt.plot(x,y,'--')
fig.savefig('test1.png')



## subplot, ,ulti-lines
