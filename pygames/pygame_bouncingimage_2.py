'''
Created on Feb 13, 2020

@author: zhangwei
'''

import pygame, sys


pygame.init()
screen =  pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
logo = pygame.image.load("../images/skier_tree.png")
x=50
y=50
x_speed = 10
y_speed = 10

while True:
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255,255,255], [x,y,90,90], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 90 or x < 0:
        x_speed = -x_speed
    if y > screen.get_height() - 90 or y < 0:
        y_speed = -y_speed
    screen.blit(logo,[x,y])
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
