import pygame, sys, random, math
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

soundObj = pygame.mixer.Sound('slither.wav')
hunterSound = pygame.mixer.Sound('hunt.wav')

windowSurfaceObj = pygame.display.set_mode((1008,630))
catSurfaceObj = pygame.image.load('background.jpg')
snakeLeft = pygame.image.load('snake_left.png').convert()
snakeRight = pygame.image.load('snake_right.png').convert()
snakeLeft.set_colorkey(snakeLeft.get_at((0,0)))
snakeRight.set_colorkey(snakeRight.get_at((0,0)))

hunterLeft = pygame.image.load('ash_left.png').convert()
hunterLeft.set_colorkey(snakeLeft.get_at((0,0)))
hunterRight = pygame.image.load('ash_right.png').convert()
hunterRight.set_colorkey(snakeLeft.get_at((0,0)))

snakePOS = (0,0)

choice = range(-5,6) 
change = (random.choice(choice),random.choice(choice))
hchange = (random.choice(choice),random.choice(choice))
windowSurfaceObj.blit(catSurfaceObj, (0,0))

hunterMax = (1000-hunterLeft.get_size()[0], 630-hunterLeft.get_size()[1])
hunterPOS = hunterMax

while True:
    windowSurfaceObj.blit(catSurfaceObj, (0,0))
    oldPOS = snakePOS
    if random.randint(0,10) == 10:
        change = (random.choice(choice),random.choice(choice))
    snakePOS = (snakePOS[0]+change[0],snakePOS[1]+change[1])
    
    if snakePOS[0] < 0:
        snakePOS = (0,snakePOS[1])
    if snakePOS[1] < 0:
        snakePOS = (snakePOS[0],0)
    #If position right then show snake right
    if oldPOS[1] > snakePOS[1]:
        snake = snakeLeft
    else:
        snake = snakeRight
    windowSurfaceObj.blit(snake, snakePOS)
    

    oldHPOS = hunterPOS
    
    if random.randint(0,10) == 10:
        hchange = (hchange[0],hchange[1])
    hunterPOS = (hunterPOS[0]+hchange[0],hunterPOS[1]+hchange[1])
    if hunterPOS[0] > hunterMax[0]:
        hunterPOS = (hunterMax[0], hunterPOS[1])
    if hunterPOS[1] > hunterMax[1]:
        hunterPOS = (hunterPOS[0],hunterMax[1])
    if hunterPOS[0] < 0:
        hunterPOS = (0, hunterPOS[1])
    if hunterPOS[1] < 0:
        hunterPOS = (hunterPOS[0],0)

    if oldHPOS[1] > hunterPOS[1]:
        hunter = hunterLeft
    else:
        hunter = hunterRight
    windowSurfaceObj.blit(hunter, hunterPOS)
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_RIGHT:
                hchange = (15,hchange[1])
            if event.key == K_LEFT:
                hchange = (-15,hchange[1])
            if event.key == K_DOWN:
                hchange = (hchange[0], 15)
            if event.key == K_UP:
                hchange = (hchange[0], -15)

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                hchange = (0,hchange[1])
            if event.key == K_LEFT:
                hchange = (0,hchange[1])
            if event.key == K_DOWN:
                hchange = (hchange[0], 0)
            if event.key == K_UP:
                hchange = (hchange[0], 0)

    ydiff = abs(snakePOS[1] - hunterPOS[1])
    xdiff = abs(snakePOS[0] - hunterPOS[0])
    if ydiff == 0:
        ydiff = 1
    dist = math.sqrt(xdiff**2 + ydiff**2)
    if abs(dist) > 200 and not pygame.mixer.get_busy():
        soundObj.play()
    elif abs(dist) < 200 and not pygame.mixer.get_busy():
        hunterSound.play()
    print(dist)

    pygame.display.update()
    fpsClock.tick(30)
#y1-x1/y2-x2
