import pygame, sys, random, math, eat_a_snake
from pygame.locals import *

class InventoryItem(pygame.sprite.Sprite):
    def __init__(self, image):
        self.active = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 950)
        self.rect.y = random.randint(50, 580)
    def setMovementMod(self, mod):
        self.movemod = mod
    def getMovementMod(self):
        return self.movemod
    def use(self):
        self.active = eat_a_snake.FPS * 10 #seconds
        pygame.mixer.Sound("assets/audio/zOOOOOOoooOOOOOm.ogg").play()
        
        
