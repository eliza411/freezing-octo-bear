import pygame, sys, random, math, eat_a_snake, time, hunterclass
from pygame.locals import *

class InventoryItem(pygame.sprite.Sprite):
    def __init__(self, image):
        self.active = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 950)
        self.rect.y = random.randint(50, 580)
        self.movemod = 0
        self.target = None
    def setTarget(self, target):
        self.target = target
    def setMovementMod(self, mod):
        self.movemod = mod
    def getMovementMod(self):
        return self.movemod
    def use(self):
        print('Action not defined')
        
class Leaf(InventoryItem):
    def __init__(self):
        InventoryItem.__init__(self, 'assets/images/leaf.png')
        self.setMovementMod(5)
        
    def use(self, target):
        self.rect.bottomright = (0,0) # Hide the sprite when item is used.
        self.setTarget(target)
        self.active = True
        self.sound = pygame.mixer.Sound("assets/audio/zOOOOOOoooOOOOOm.ogg")
        self.endtime = time.time() + self.sound.get_length()
        self.sound.play()
        self.target.movement_speed += self.movemod # Up the target (probably the hunter's) speed
    def update(self):
        # Check for active and duration. Delete at the end because leaves are consumable.
        if self.active and self.endtime < time.time():
            # Reduce the hunter's movement speed before we destroy ourself
            self.target.movement_speed -= self.movemod
            self.kill()
        

class FireEgg(InventoryItem):
    def __init__(self):
        InventoryItem.__init__(self, 'assets/images/fireegg.png')
        self.duration = 3
        self.firetimer = 0
        self.allowed_target_types = (hunterclass.Hunter,)

    def use(self, target):
        if type(target) not in self.allowed_target_types:
            self.kill()
            return
        self.setTarget(target)
        self.active = True
        self.sound = pygame.mixer.Sound("assets/audio/volcanosplode.ogg")
        self.endtime = time.time() + self.duration
        self.sound.set_volume(1.0)
        self.sound.play(maxtime=self.duration*1000) #Play time is in milliseconds

    def update(self):
        if self.active:
            if self.firetimer < time.time():
                fireball = Fireball(self.target.rect.topleft, -1) # -1 is left
                self.target.projectiles.add(fireball)
                self.firetimer = time.time() + 0.45
            if self.endtime < time.time():
                self.kill()

class Fireball(pygame.sprite.Sprite):
    def __init__(self, origin, direction):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.image = pygame.image.load('assets/images/fireball.png')
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.topleft = origin
        self.duration = 5
        self.target = None
    def update(self):
        if self.target:
            #burn the target
            self.rect.center = self.target.rect.center
            self.rect.x += random.choice((-10,0,10))
            if time.time() > self.endtime:
                self.target.movement_speed += 2
                self.kill()
        else:
            #fly around
            self.rect.x += self.direction*10
    def use(self, target):
        self.target = target
        self.image = pygame.transform.rotate(self.image,-90)
        target.movement_speed -= 2
        self.endtime = time.time() + self.duration



