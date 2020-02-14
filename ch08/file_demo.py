'''
Created on Feb 13, 2020

@author: zhangwei
'''
# write file append
my_second_file = open('test','a')
my_second_file.write('\ntest' )
my_second_file.close()


# read method 1
my_file = open('test','r')
lines = my_file.readlines() # a list
for line in lines:
    print(line)
    
# read method 2
my_file = open('test','r')
lines = my_file.read() # a str
print(lines)
    
# read method 3
with open('test', 'r') as f1:
    line1 = f1.readline()
    line2 = f1.readline()
    print("location = ", f1.tell())
    my_file.seek(0)
    print("location = ", f1.tell())
print("line 1 = "+line1)
print("line 2 = "+line2)
my_file.seek(0)

# write file 
my_second_file = open('test','w')
my_second_file.write('test\ntest' )
my_second_file.close()

# read method 2
my_file = open('test','r')
lines = my_file.read() # a str
print(lines)

# write file 
my_second_file = open('test','w')
my_second_file.writelines(['test-1\n','test-2'] )
my_second_file.close()

# write 
my_second_file = open('test','w')
print("test-2\ntest-2",file=my_second_file)
