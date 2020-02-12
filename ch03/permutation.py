'''
Created on Feb 12, 2020

@author: zhangwei
'''

count = 1
print("\tRed \tBlue \tYellow \tGreen")
for r in [0,1]:
    for b in [0,1]:
        for y in [0,1]:
            for g in [0,1]:
                print( "#", count, "\t", r,"\t", b,"\t", y,"\t", g)
                count = count + 1