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
            

def animate(group):
    screen.fill([255,255,255])
    for tree in group:
        group.remove(tree)
        if pygame.sprite.spritecollide(tree, group, False):
            tree.speed[0] = -tree.speed[0]
            tree.speed[1] = -tree.speed[1]
        group.add(tree)
        tree.move()
        screen.blit(tree.image, tree.rect)
    pygame.display.flip()
    pygame.time.delay(20)  
    
    
size = width, height = [640, 480]
screen =  pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "../images/skier_tree.png"
group  = pygame.sprite.Group()

for row in range(0,2):
    for column in range(0 , 2):
        location = [column * 180 + 10, row * 180 +10]
        speed = [random.choice([-2,2]), random.choice([-2,2])]
        tree = MyTree(img_file, location , speed)
        group.add(tree)
        
while True:
    animate(group)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()