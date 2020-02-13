'''
Created on Feb 13, 2020

@author: zhangwei
'''
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 640])
screen.fill([255,255,255])
pygame.draw.circle(screen, [255,0,0], [100,100], 30, 0)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()