'''
Created on Feb 13, 2020

@author: zhangwei
'''
import pygame, sys

pygame.init()
screen =  pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
logo = pygame.image.load("../images/skier_tree.png")
x = 50
y = 50
x_speed = 5

while True:
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255,255,255], [x,y,90,90], 0)
    x = x + x_speed
    if x > screen.get_width():
        x = 0
    screen.blit(logo,[x,y])
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
