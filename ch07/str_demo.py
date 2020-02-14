'''
Created on Feb 13, 2020

@author: zhangwei
'''

math_score = 95.5
science_score = 99.7
print("My math is %.1f and my science is %.1f." %(math_score, science_score))
print("My math is {0:.1f} and my science is {1:.1f}".format(math_score, science_score))
 
print("My math is {0:.1e} and my science is {1:.1e}".format(math_score, science_score))
print("My math is {0:.1f}% and my science is {1:.1f}%".format(math_score, science_score))

mobile = " 3065153678, 3063938888, 3063918888 "
mobiles = mobile.split(",")
for part in mobiles:
    print(part)
    
words = ['I', 'am', 'a', 'student', 'instructor.']
whole_word = ' '.join(words)
print(whole_word)

print(mobile.startswith('306'))
print(mobile.endswith('306'))

print("306515" in mobile)
print(mobile.index("306515"))

print(mobile.strip(' 306'))
print(mobile.strip())

print(whole_word.upper())
print(whole_word.lower())