import pygame, sys, random, math 
from pygame.locals import *
import hunter, snake

class Snake(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

