from pygame.locals import *
import pygame, sys, random, math



class Hunter(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, imageLeft, imageRight):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.hunterLeft = pygame.image.load(imageLeft).convert()    #Set hunter sprites
        self.hunterRight = pygame.image.load(imageRight).convert()
        self.hunterLeft.set_colorkey(self.hunterLeft.get_at((0,0)))            #Set hunter background transparency
        self.hunterRight.set_colorkey(self.hunterRight.get_at((0,0)))
        self.inventory =  pygame.sprite.Group()
        self.effects =  pygame.sprite.Group()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = self.hunterRight

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.hunterMax = (1000-self.rect.x, 630-self.rect.y)   #Variable used to prevent Hunter from leaving screen
        self.rect.x += self.hunterMax[0]/2   #Hunter's start position(in the middle of the screen!!!)
        self.rect.y += self.hunterMax[1]/2   #Hunter's start position

        self.movex = 0
        self.movey = 0
        self.choice = range(-5,6)        #Made a list of -5 to 5

    def update(self):
        self.move(self.movex, self.movey)
        for item, x in zip(self.inventory, range(len(self.inventory))):
            item.rect.x = x*70
            item.rect.y = 635

    def move(self, dx ,dy):
        mspd = 1
        for item in self.effects:
            if item.active:
                mspd += item.getMovementMod()
                item.active -= 1
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

        if random.randint(0,10) == 10:
            hchange = (random.choice(self.choice),random.choice(self.choice))
        # Calculate the new position based on randomness plus the control direction
        if dx < 0:
            self.image = self.hunterLeft
        elif dx > 0:
            self.image = self.hunterRight
    def consume(self, invNum):
        invList = self.inventory.sprites()
        if len(invList) > invNum:
            invList[invNum].use()
            self.effects.add(invList[invNum])
            self.inventory.remove(invList[invNum])
            
            

