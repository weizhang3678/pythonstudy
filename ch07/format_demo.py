'''
Created on Feb 13, 2020

@author: zhangwei
'''
# str
print("a\\b")
print("a\tb")
print("a\nb")
print("My name is %s and I am a %s." %("Wei Zhang","Student instructor"))

# interger
print("My name is %s and I am %i years old." %("Wei Zhang", 38))
tem = 12.345
print("%i" % tem)
print(int(tem))

# float
print("My name is %s and I have %f deposit." %("Wei Zhang", 300.0))
tem = 12.3456
print("It is %.2f degrees today." %tem)
print("My name is %s and I have %.0f deposit." %("Wei Zhang", 300.0))

num = -12.3456
print("It is %+F degrees today." %tem)
print("It is %+f degrees today." %num)
print("It is %F degrees today." %tem)
print("It is %f degrees today." %num)

print("It is %e degrees today." %num)
print("It is %.3e degrees today." %num)

per = 87.9
print("The percent is %.1f%%." %per)
