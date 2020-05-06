'''
pandas drawing
'''

import pandas as pd
import numpy as np
df = pd.read_csv('data.csv')
df = pd.DataFrame(np.random.rand(10,50,(3,4)), columns = ['A','B','C','D'])
print(df.head())
df.plot()
df.plot.bar()
df.plot(kind = 'bar', stacked = True) # same as previous line

df.hist() # ZHI FANG
df.plot.kde() #line

