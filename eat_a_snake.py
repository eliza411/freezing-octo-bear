import pygame, sys, random, math 
from pygame.locals import *
import hunterclass, snakeclass, items

FPS = 30
def main():
    pygame.init()
    fpsClock = pygame.time.Clock()

    snakeSound = pygame.mixer.Sound('assets/audio/slither.wav')
    hunterSound = pygame.mixer.Sound('assets/audio/hunt.wav')

    snakeChannel = pygame.mixer.Channel(1)
    snakeChannel.play(snakeSound, -1)
    snakeChannel.pause()
    hunterChannel = pygame.mixer.Channel(2)
    hunterChannel.play(hunterSound, -1)
    hunterChannel.pause()

    windowSurfaceObj = pygame.display.set_mode((1008,700))      #Set window size
    catSurfaceObj = pygame.image.load('assets/images/background.jpg')         #Set background sprite

    hunter =  hunterclass.Hunter('assets/images/ash_left.png', 'assets/images/ash_right.png') #Hunter starts the game looking left
    AliveSprites = pygame.sprite.Group(hunter)

    Inventory = pygame.image.load('assets/images/Inventory.png')
    #Load inventory sprites
    itemSprites = pygame.sprite.Group()
    for x in range(10):
        leaf = items.InventoryItem('assets/images/leaf.png')
        itemSprites.add(leaf)
        AliveSprites.add(leaf)
        leaf.setMovementMod(6)
        if hunter.rect.colliderect(leaf.rect): #If we start with a collision move the leaf
            leaf.rect.x = random.randint(50, 950)
            leaf.rect.y = random.randint(50, 580)

    windowSurfaceObj.blit(catSurfaceObj, (0,0))                 #Draw the background

    snakes = pygame.sprite.Group()
    for x in range(5):
        snakeActor = snakeclass.Snake() #Create one snake
        AliveSprites.add(snakeActor)
        snakes.add(snakeActor)

    while True:
        windowSurfaceObj.blit(catSurfaceObj, (0,0)) #Constantly draw background
        windowSurfaceObj.blit(Inventory, (0,630)) #Draw the iventory boxes every refresh
        collide =  pygame.sprite.spritecollide(hunter, itemSprites, True)
        if collide:
            hunter.inventory.add(collide)

        AliveSprites.draw(windowSurfaceObj) 
        hunter.inventory.draw(windowSurfaceObj)
        hunter.update()
        snakes.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    hunter.consume(0)
                if event.key == K_2:
                    hunter.consume(1)
                if event.key == K_3:
                    hunter.consume(2)
                if event.key == K_4:
                    hunter.consume(3)
                if event.key == K_5:
                    hunter.consume(4)
                if event.key == K_6:
                    hunter.consume(5)
                if event.key == K_7:
                    hunter.consume(6)
                if event.key == K_8:
                    hunter.consume(7)
                if event.key == K_9:
                    hunter.consume(8)
                if event.key == K_0:
                    hunter.consume(9)

                if event.key == K_PERIOD:
                    pygame.mixer.Sound("assets/audio/flawless_victory.wav").play()
                
                
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
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()
