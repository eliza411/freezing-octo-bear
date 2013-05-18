import pygame, sys, random, math
from pygame.locals import *

class InventoryItem(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.POS = (random.randint(0,1008), random.randint(0,630))
        self.rect = self.image.get_rect()
    def setMovementMod(self, mod):
        self.movemod = mod
    def getMovementMod(self):
        return self.movemod

