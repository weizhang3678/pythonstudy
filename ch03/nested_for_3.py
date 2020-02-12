'''
Created on Feb 12, 2020

@author: zhangwei
'''

blockNum = int(input("How many blocks of starts do you want?"))
lineNums = int(input("How many lines in each block?"))
starNums = int(input("How many stars per line?"))

for block in range(blockNum):
    for line in range(lineNums):
        for star in range(starNums):
            print("*", end = " ")
        print()
    print()