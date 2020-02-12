'''
Created on Feb 12, 2020

@author: zhangwei
'''
import easygui
book = easygui.buttonbox("What is your favorite book?", choices=['Snow White and the Seven Dwarfs', 'The Little Mermaid', 'The Snow Queen'])
easygui.msgbox("You picked " + book)