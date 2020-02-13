'''
Created on Feb 13, 2020

@author: zhangwei
'''

import pygame, sys
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
# location, the first is for vertical, the second is for horizon
pygame.draw.circle(screen, THECOLORS["red"], [320,240], 30, 0)
pygame.draw.rect(screen, THECOLORS["red"], [320,240,100,80], 2) # last 2 is width of line

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()