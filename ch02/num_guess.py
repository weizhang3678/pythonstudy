'''
Created on Feb 12, 2020

@author: zhangwei
'''
import random, easygui

secret = random.randint(1, 99)
guess = 0
tries = 0
easygui.msgbox("""Hi, I am a robot and I have a secret!
It is a number between 1 to 99. I will give you 6 tries.""")
while guess != secret and tries < 6:
    guess = easygui.integerbox("What is your guess?")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high!")
    tries = tries +1
    
if guess == secret:
    easygui.msgbox("You got it! Found my secret!")
else:
    easygui.msgbox("no more guess! Better luck next time.")
    easygui.msgbox("The secret number was ", secret)
        