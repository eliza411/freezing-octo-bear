import pygame, sys, random, math, eat_a_snake, time, hunterclass, snakeclass
from pygame.locals import *
from locals import *

class InventoryItem(pygame.sprite.Sprite):
    def __init__(self, image):
        self.active = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, DOMAIN['x'])
        self.rect.y = random.randint(50, DOMAIN['y'])
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
        self.allowed_target_types = (hunterclass.Hunter, snakeclass.Snake)

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
                fireball = Fireball(self.target.rect.topleft, self.target.movex, self.target.movement_speed, self.target) 
                self.target.projectiles.add(fireball)
                self.firetimer = time.time() + 0.45
            if self.endtime < time.time():
                self.kill()


class Fireball(pygame.sprite.Sprite):
    def __init__(self, origin, direction, fireball_speed, owner):
        pygame.sprite.Sprite.__init__(self)
        self.owner = owner
        self.fireball_speed = fireball_speed
        self.direction = direction
        self.image = pygame.image.load('assets/images/fireball.png')
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.topleft = origin
        self.duration = 5
        self.target = None

        
    def update(self):
        if self.direction == 0:
            self.direction = -1
        if self.target:
            #burn the target
            self.rect.center = self.target.rect.center
            self.rect.x += random.choice((-10,0,10))
            if time.time() > self.endtime:
                self.target.movement_speed += 2
                self.kill()
        else:
            #fly around
            print(self.direction, self.fireball_speed)
            self.rect.x += (self.direction * self.fireball_speed) + (10 * self.direction) #fireball speed
            
    def use(self, target):
        if target == self.owner:
            return 0
        self.target = target
        self.image = pygame.transform.rotate(self.image,-270)
        target.movement_speed -= 2
        self.endtime = time.time() + self.duration


class AimedFireball(Fireball):
    def __init__(self, origin, direction, aimed_at):
        Fireball.__init__(self, origin, direction, 0, 0)
        self.aimed_at = aimed_at
        self.dest = aimed_at.rect.copy()

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
            if self.rect.x > self.dest.x:
                self.rect.x -= 5
            elif self.rect.x < self.dest.x:
                self.rect.x += 5
            if self.rect.y > self.dest.y:
                self.rect.y -= 5
            elif self.rect.y < self.dest.y:
                self.rect.y += 5


class FireBloom(InventoryItem):
    def __init__(self):
        InventoryItem.__init__(self, 'assets/images/firebloom.bmp')
        self.duration = 10
        self.chargetime = 1
        self.firetimer = 0
        self.allowed_target_types = (hunterclass.Hunter,)

    def use(self, target):
        if type(target) not in self.allowed_target_types:
            self.kill()
            return
        self.setTarget(target)
        self.active = True
        self.sound = pygame.mixer.Sound("assets/audio/door.wav")
        self.endtime = time.time() + self.duration
        self.starttime = time.time() + self.chargetime
        self.sound.set_volume(1.0)
        self.sound.play(maxtime=self.duration*1000) #Play time is in milliseconds
        self.rect.topleft = target.rect.topleft
        self.target.solidSprites.add(self)

    def update(self):
        if self.active:
            if time.time() > self.starttime:
                if self.firetimer < time.time():
                    fireball = AimedFireball(self.rect.topleft, -1, self.target)
                    self.target.projectiles.add(fireball)
                    self.firetimer = time.time() + 0.45
            if self.endtime < time.time():
                self.kill()
