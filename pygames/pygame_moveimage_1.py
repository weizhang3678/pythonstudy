'''
Created on Feb 13, 2020

@author: zhangwei
'''
import pygame, sys


pygame.init()
screen =  pygame.display.set_mode([640, 640])
screen.fill([255,255,255])
logo = pygame.image.load("../images/skier_tree.png")
x=50
y=50
screen.blit(logo,[x,y])
pygame.display.flip()

while x < screen.get_width() -90:
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255,255,255], [x,y,90,90], 0)
    x = x + 5
    screen.blit(logo,[x,y])
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()