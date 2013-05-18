import pygame, sys, random, math 
from pygame.locals import *
import hunter, snake, items

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
invItems.append(items.InventoryItem('leaf.png'))

invItems[0].setMovementMod(6)


hunter =  hunter.Hunter('ash_left.png', 'ash_right.png') #Hunter starts the game looking left
AliveSprites = pygame.sprite.Group(hunter)

snakePOS = (0,0)            #Initial snake position

choice = range(-5,6)        #Made a list of -5 to 5
change = (random.choice(choice),random.choice(choice))      
hchange = (random.choice(choice),random.choice(choice))
windowSurfaceObj.blit(catSurfaceObj, (0,0))                 #Draw the background



snake = snake.Snake(snakeLeft) #Snake starts the game looking left
AliveSprites.add(snake)

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
        
    if oldPOS[0] > snakePOS[0]:
        snake.image = snakeLeft
    elif oldPOS[0] < snakePOS[0]:
        snake.image = snakeRight

        
    AliveSprites.draw(windowSurfaceObj) 
    hunter.update()
    snake.update()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_RIGHT:
                hunter.movex = 1
            if event.key == K_LEFT:
                hunter.movex = -1
            if event.key == K_DOWN:
                hunter.movey = 1
            if event.key == K_UP:
                hunter.movey = -1

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                hunter.movex = 0
            if event.key == K_LEFT:
                hunter.movex = 0
            if event.key == K_DOWN:
                hunter.movey = 0
            if event.key == K_UP:
                hunter.movey = 0

    pygame.display.flip()
    
    fpsClock.tick(30)
#y1-x1/y2-x2
