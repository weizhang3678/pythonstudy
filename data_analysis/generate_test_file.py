import csv
import random
file = open("data.csv",'w',newline='')
try:
    writer=csv.writer(file)
    writer.writerow(('id','name','class','score-math','score-language'))
    for i in range(10):
        name = 'name'+str(i)
        score = str(random.randint(40,100))
        score1 = str(random.randint(40,100))
        writer.writerow((i, name, 'G6-C1', score, score1))
finally:
    file.close()
