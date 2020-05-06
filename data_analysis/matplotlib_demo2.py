'''
matplotlib drawing
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('data.csv')
#%matplotlib inline
x = np.linspace(0,10,20)
y = np.sin(x)
y1 = np.cos(x)

plt.plot(x,y,'--',label='sin(x)')
#plt.plot(x,y1,'o',label = 'cos(x)', marksize=3, linewidth = 4)//'d', 'o','p','--'
#legend control label format
plt.legend(loc=0) #location of label
#plt.legend?


plt.ylim(-0.5,0.8) # range of y
plt.xlim(2,8)      # range of x


plt.scatter(x, y , s = 10, color = 'red')

x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.randn(100)
sizes = np.random.randn(100)*100
fig = plt.figure()
plt.scatter(x,y, c=colors, s=sizes, alpha = 0.4)
plt.colorbar()
fig.savefig('scatter.png')






