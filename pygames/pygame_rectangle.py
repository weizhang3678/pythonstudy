'''
Created on Feb 13, 2020

@author: zhangwei
'''
import pygame, sys, random
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])

for i in range(100):
    width = random.randint(0,250)
    height = random.randint(0,100)
    top = random.randint(0,400)
    left = random.randint(0,400)
    color = THECOLORS[random.choice(list(THECOLORS.keys()))]
    pygame.draw.rect(screen, color, [left,top,width,height], 1) # last 2 is width of line
    
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()