import pygame, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((1008,630))
catSurfaceObj = pygame.image.load('background.jpg')
snakeLeft = pygame.image.load('snake_left.png').convert()
snakeRight = pygame.image.load('snake_right.png').convert()
snakeLeft.set_colorkey(snakeLeft.get_at((0,0)))
snakeRight.set_colorkey(snakeRight.get_at((0,0)))

snakePOS = (0,0)

choice = range(-5,5) 
change = (random.choice(choice),random.choice(choice))
windowSurfaceObj.blit(catSurfaceObj, (0,0))
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
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
    pygame.display.update()
    fpsClock.tick(30)
