import pygame as py
from settings import *
vec = py.math.Vector2

class Player(py.sprite.Sprite):
    #initilaize and draw player
    def __init__(self, game):
        py.sprite.Sprite.__init__(self)
        self.game = game
        self.image = py.Surface((30,40))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT /2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        #check if we are standing on something first. Then only jump once
        self.rect.x +=1
        hits = py.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -=1

        if hits:
            self.vel.y = -20

    def update(self):
        #Initial starting point
        self.acc = vec(0,PLAYER_GRAV)
        keys = py.key.get_pressed()
        if keys[py.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[py.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        # if keys[py.K_UP]:
        #     self.acc.y = -PLAYER_ACC
        # if keys[py.K_DOWN]:
        #     self.acc.y = PLAYER_ACC



        #Friction added
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #motion equations
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #wrap around
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        #Center of sprite at new position
        self.rect.midbottom = self.pos

class Platform(py.sprite.Sprite):
    def __init__(self, x, y, w, h):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
