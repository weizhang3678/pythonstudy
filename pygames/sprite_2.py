'''
Created on Feb 13, 2020

@author: zhangwei
'''
import pygame, sys , random


class MyTree(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
            
         
        
    


size = width, height = [640, 480]
screen =  pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "../images/skier_tree.png"
trees = []

for row in range(0,5):
    for column in range(0 , 5):
        location = [column * 180 + 10, row * 180 +10]
        speed = [random.choice([-2,2]), random.choice([-2,2])]
        tree = MyTree(img_file, location , speed)
        trees.append(tree)
        
for tree in trees:
    screen.blit(tree.image, tree.rect)
pygame.display.flip()

while True:
    pygame.time.delay(20)
    screen.fill([255, 255, 255])
    for tree in trees:
        tree.move()
        screen.blit(tree.image, tree.rect)
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()