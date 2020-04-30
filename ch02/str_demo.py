string1 = "I am a student."
string2 = "Iam"
string3 = "1.014"
#slice
print(string1[0])
print(string1[:4])
print(string1[-1])
print(string1[0:8:2])
print(string1[::-1])

#function
print(string1.capitalize())
print(string1.casefold())
print(string1.center(20))
print(string1.center(20,'%'))
print(string1.count('a'))
print(string1.endswith('t.'))
print(string1.startswith('i'))

print(string1.find('a'))
print(string1.find('a',4))
print(string1.index('a',4))

print(string1.upper())
print(string1.lower())

print(string1.istitle())
print(string1.isupper())
print(string1.islower())
print(string1.strip())
print(string1.lstrip())
print(string1.rstrip())
print(string1.swapcase())

print(string3.isalpha())
print(string3.isnumeric())
print(string3.isdecimal())
print(string3.isdigit())
