'''
Created on Feb 12, 2020

@author: zhangwei
'''
import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print('Hi, I am a robot and I have a secret!')
print('It is a number between 1 to 99. I will give you 6 tries.')
while guess != secret and tries < 6:
    guess = int(input('What is your guess?'))
    if guess < secret:
      print('too low!')
    elif guess > secret:
      print('too hign')
    tries = tries + 1
if guess == secret:
    print('You got it! Found my secret!')
else:
    print('no more guess! Better luck next time.')
    print('The secret number was ', secret) 
        