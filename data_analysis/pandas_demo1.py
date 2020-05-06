# pandas
'''
read csv file
filter
sort
'''

import pandas as pd
df = pd.read_csv('data.csv')
# read 2 lines
print(df.head(2))
# column name
print(df.columns)
# indexs
print(df.index)
# ???
print(df.loc[0])

# filter by value
print(df.score>60)

print(df[df.score>60])

# filter complex
print(df[(df.score>60) & (df.id > 5)])

# sort
print(df.sort_values(['score','id'],ascending = False))