'''
access
'''
import pandas as pd

df = pd.read_csv('data.csv')
# search by index
#print(df.loc[1])

scores= {
    'language':[90,78,98],
    'math':[97,70,68],
    'name':['Evan','Ellen','Wei'],
}
df = pd.DataFrame(scores,index = ['one','two','threr'])
#print(df.index)
#print(df.loc['one'])
# index is 'one', df.loc[1] is error
#print(df.iloc[1])

# new function ix combine loc & iloc
# print(df.ix[0])

df = pd.read_csv('data.csv')
# access more lines
# df[0] illegal to access one line by []
# df[0:2] legal to access more lines, slice is legal
print(df.loc[:1])
print(df.values)
print(df.score.values)

# statistic
print(df.score.value_counts)

# more column
new = df[['id','score']].head()
print(new*2)

#map function
def func(score):
    if score >=80:
        return 'a'
    elif score>=79:
        return 'b'
    elif score>=60:
        return 'c'
    else:
        return 'd'
df['level'] = df.score.map(func)
print(df.head())

#applymap
def func1(number):
    return number + 10
func = lambda number: number + 10

df.applymap(lambda x: str(x)+'*')
print(df.head())

# drop a column
