'''
Created on Feb 12, 2020

@author: zhangwei
'''
import easygui

book = easygui.enterbox("What is your favorite book?", default = 'Snow White and the Seven Dwarfs')
easygui.msgbox("You input " + book)