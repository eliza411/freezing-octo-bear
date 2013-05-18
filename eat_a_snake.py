import pygame, sys, random, math 
from pygame.locals import *

class InventoryItem(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.POS = (random.randint(0,1008), random.randint(0,630))
        self.rect = self.image.get_rect()
    def setMovementMod(self, mod):
        self.movemod = mod
    def getMovementMod(self):
        return self.movemod

class Hunter(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, image):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = image

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

pygame.init()
fpsClock = pygame.time.Clock()

snakeSound = pygame.mixer.Sound('slither.wav')
hunterSound = pygame.mixer.Sound('hunt.wav')

snakeChannel = pygame.mixer.Channel(1)
snakeChannel.play(snakeSound, -1)
snakeChannel.pause()
hunterChannel = pygame.mixer.Channel(2)
hunterChannel.play(hunterSound, -1)
hunterChannel.pause()

windowSurfaceObj = pygame.display.set_mode((1008,700))      #Set window size
catSurfaceObj = pygame.image.load('background.jpg')         #Set background sprite
snakeLeft = pygame.image.load('snake_left.png').convert()   #Set Snake sprites
snakeRight = pygame.image.load('snake_right.png').convert()
snakeLeft.set_colorkey(snakeLeft.get_at((0,0)))             #Choose one pixel and make all pixels that color transparent
snakeRight.set_colorkey(snakeRight.get_at((0,0)))

Inventory = pygame.image.load('Inventory.png')
#Load inventory sprites
invItems = []
invItems.append(InventoryItem('RaccoonLeaf.gif'))

invItems[0].setMovementMod(6)


hunterLeft = pygame.image.load('ash_left.png').convert()    #Set hunter sprites
hunterRight = pygame.image.load('ash_right.png').convert()
hunterLeft.set_colorkey(snakeLeft.get_at((0,0)))            #Set hunter background transparency
hunterRight.set_colorkey(snakeLeft.get_at((0,0)))

hunter = Hunter(hunterLeft) #Hunter starts the game looking left

snakePOS = (0,0)            #Initial snake position

choice = range(-5,6)        #Made a list of -5 to 5
change = (random.choice(choice),random.choice(choice))      
hchange = (random.choice(choice),random.choice(choice))
windowSurfaceObj.blit(catSurfaceObj, (0,0))                 #Draw the background

hunterMax = (1000-hunterLeft.get_size()[0], 630-hunterLeft.get_size()[1])   #Variable used to prevent Hunter from leaving screen
hunterPOS = hunterMax   #Hunter's start position


snake = snakeLeft #Snake starts the game looking left

control_direction = [0,0]   #variable used to move hunter
invItemsPossessed = []


spriteGroup = pygame.sprite.Group()
for item in invItems:
    spriteGroup.add(item)

while True:
    windowSurfaceObj.blit(catSurfaceObj, (0,0))             #Constantly draw background
    oldPOS = snakePOS       #Snake's position of the last frame
    if random.randint(0,10) == 10:
        change = (random.choice(choice),random.choice(choice))

    windowSurfaceObj.blit(Inventory, (0,630))
    for item in invItemsPossessed:
        windowSurfaceObj.blit(item.image, (3,633))

    for item in invItems:
        windowSurfaceObj.blit(item.image, item.POS)

    #Snake stuffs    
    snakePOS = (snakePOS[0]+change[0],snakePOS[1]+change[1])
    
    #Changing left/right sprite depending on where it moved
    if snakePOS[0] < 0:             
        snakePOS = (0,snakePOS[1])
    if snakePOS[1] < 0:         
        snakePOS = (snakePOS[0],0)
    if snakePOS[0] > hunterMax[0]:
        snakePOS = (hunterMax[0], snakePOS[1])
    if snakePOS[1] > hunterMax[1]:
        snakePOS = (snakePOS[0],hunterMax[1])
        
    if oldPOS[0] > snakePOS[0]:
        snake = snakeLeft
    elif oldPOS[0] < snakePOS[0]:
        snake = snakeRight
    windowSurfaceObj.blit(snake, snakePOS)

    
    #Hunter's stuffs
    oldHPOS = hunterPOS
    
    if random.randint(0,10) == 10:
        hchange = (random.choice(choice),random.choice(choice))
    # Calculate the new position based on randomness plus the control direction
    for item in invItemsPossessed:
        if item.getMovementMod():
            control_direction[0] += item.getMovementMod()
    hunterPOS = (hunterPOS[0]+hchange[0]+control_direction[0],hunterPOS[1]+hchange[1]+control_direction[1])
    if hunterPOS[0] > hunterMax[0]:
        hunterPOS = (hunterMax[0], hunterPOS[1])
    if hunterPOS[1] > hunterMax[1]:
        hunterPOS = (hunterPOS[0],hunterMax[1])
    if hunterPOS[0] < 0:
        hunterPOS = (0, hunterPOS[1])
    if hunterPOS[1] < 0:
        hunterPOS = (hunterPOS[0],0)

    if oldHPOS[0] > hunterPOS[0]:
        hunter.image = hunterLeft
    elif oldHPOS[0] < hunterPOS[0] :
        hunter.image = hunterRight
    windowSurfaceObj.blit(hunter.image, hunterPOS)
    
        

    for item in pygame.sprite.spritecollide(hunter,spriteGroup,False):
        print item
        if item == invItems[0]:
            sys.exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_RIGHT:
                control_direction[0] = 3
            if event.key == K_LEFT:
                control_direction[0] = -3
            if event.key == K_DOWN:
                control_direction[1] = 3
            if event.key == K_UP:
                control_direction[1] = -3

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                control_direction[0] = 0
            if event.key == K_LEFT:
                control_direction[0] = 0
            if event.key == K_DOWN:
                control_direction[1] = 0
            if event.key == K_UP:
                control_direction[1] = 0

    ydiff = abs(snakePOS[1] - hunterPOS[1])
    xdiff = abs(snakePOS[0] - hunterPOS[0])
    if ydiff == 0:
        ydiff = 1
    dist = math.sqrt(xdiff**2 + ydiff**2)
    distRatio = 1.0 - (dist/math.sqrt(1008**2 + 630**2))
    if abs(dist) > 200:
        hunterChannel.pause()
        # Make the volume softer when the hunter is more distant.
        snakeChannel.set_volume(distRatio)
        snakeChannel.unpause()
    elif abs(dist) < 200:
        snakeChannel.pause()
        hunterChannel.unpause()
    print(distRatio)

    pygame.display.update()
    fpsClock.tick(30)
#y1-x1/y2-x2
