'''
Created on Feb 13, 2020

@author: zhangwei
'''
import pygame
pygame.init()
pygame.mixer.init()

m = pygame.mixer.Sound("../videos/11.wav") 
m.play()

#player = pygame.mixer.music.load("../videos/music.mp3")
#pygame.mixer.music.play()