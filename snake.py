import pygame, sys, random, math 
from pygame.locals import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.choice = range(-5,6)        #Made a list of -5 to 5 

    def update(self):
        self.move(random.choice(self.choice), random.choice(self.choice))
    
    def move(self, dx, dy):
        
        
        self.rect.x += dx*4
        self.rect.y += dy*4
        if self.rect.bottomright[0] > 1007:
            self.rect.x -= dx*4

        if self.rect.bottomright[1] > 630:
            self.rect.y -= dy*4

        if self.rect.topleft[0] < 0:
            self.rect.x -= dx*4

        if self.rect.topleft[1] < 0:
            self.rect.y -= dy*4
