import pygame, sys, random, math 
from pygame.locals import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.snakeLeft = pygame.image.load('assets/images/snake_left.png').convert()   #Set Snake sprites
        self.snakeRight = pygame.image.load('assets/images/snake_right.png').convert()
        self.snakeLeft.set_colorkey(self.snakeLeft.get_at((0,0)))             #Choose one pixel and make all pixels that color transparent
        self.snakeRight.set_colorkey(self.snakeRight.get_at((0,0)))
        self.image = self.snakeLeft #Snake starts the game looking left
        self.rect = self.image.get_rect()
        self.choice = range(-5,6)        #Made a list of -5 to 5
        self.change = (0,0)
        self.effects = pygame.sprite.Group()
        self.movement_speed = 2

    def update(self):
        self.effects.update()
        self.effects.draw(self.surface)
        self.move(self.change[0], self.change[1])
        if random.randint(0,10) == 10:
            self.change = (random.choice(self.choice),random.choice(self.choice))
    
    def move(self, dx, dy):
        mspd = self.movement_speed
        if mspd < 0:
            mspd = 0
        
        self.rect.x += dx*mspd
        self.rect.y += dy*mspd
        if self.rect.bottomright[0] > 1007:
            self.rect.x -= dx*mspd

        if self.rect.bottomright[1] > 630:
            self.rect.y -= dy*mspd

        if self.rect.topleft[0] < 0:
            self.rect.x -= dx*mspd

        if self.rect.topleft[1] < 0:
            self.rect.y -= dy*mspd

        # Calculate the new position based on randomness plus the control direction
        if dx < 0:
            self.image = self.snakeLeft
        elif dx > 0:
            self.image = self.snakeRight
