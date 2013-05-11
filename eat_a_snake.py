import pygame, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((1008,630))
catSurfaceObj = pygame.image.load('background.jpg')
snakeLeft = pygame.image.load('snake_left.png').convert()
snakeRight = pygame.image.load('snake_right.png').convert()
snakeLeft.set_colorkey(snakeLeft.get_at((0,0)))

snakePOS = (0,0)
choice = range(-5,5) 
windowSurfaceObj.blit(catSurfaceObj, (0,0))
while True:
    snakePOS = (snakePOS[0]+random.choice(choice),snakePOS[1]+random.choice(choice))
    if snakePOS[0] < 0:
        snakePOS = (0,snakePOS[1])
    if snakePOS[1] < 0:
        snakePOS = (snakePOS[0],0)
    windowSurfaceObj.blit(snakeLeft, snakePOS)
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
    pygame.display.update()
    fpsClock.tick(30)
