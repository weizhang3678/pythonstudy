'''
Created on Feb 13, 2020

@author: zhangwei
'''

import pygame, sys


pygame.init()
screen =  pygame.display.set_mode([640, 640])
screen.fill([255,255,255])
background = pygame.image.load("../images/timg4.jpg")
screen.blit(background,[65,60])

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()