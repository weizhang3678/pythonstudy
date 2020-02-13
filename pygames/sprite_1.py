'''
Created on Feb 13, 2020

@author: zhangwei
'''
import pygame, sys



class MyTree(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    
img_file = "../images/skier_tree.png"

size = width, height = [640, 480]
screen =  pygame.display.set_mode(size)
screen.fill([255,255,255])

trees = []

for row in range(0,3):
    for column in range(0 , 3):
        location = [column * 180 + 10, row * 180 +10]
        tree = MyTree(img_file, location)
        trees.append(tree)
        
for tree in trees:
    screen.blit(tree.image, tree.rect)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()