import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((1008,630))
catSurfaceObj = pygame.image.load('background.jpg')

while True:
    windowSurfaceObj.blit(catSurfaceObj, (0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
    pygame.display.update()
    fpsClock.tick(30)
