#Imports
import pygame as py
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        #initilaize game window, etc
        py.init()
        py.mixer.init()
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        py.display.set_caption(TITLE)
        self.clock = py.time.Clock()
        self.running = True

    def new(self):
        #start new Game
        self.all_sprites = py.sprite.Group()
        self.platforms = py.sprite.Group()
        #Reference-link to game
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plats in PLATFORM_List:
            p = Platform(*plats)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #Game Loop update
        self.all_sprites.update()
        #when player collides with platform when falling
        if self.player.vel.y > 0:
            hits = py.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

        #If player reaches top quater of scrren
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
        # if self.player.rect.top <= WIDTH:
        #     self.player.pos.x += abs(self.player.vel.x)
        #     for plat in self.platforms:
        #         plat.rect.x += abs(self.player.vel.x)

    def events(self):
        #Game Loop events
        for event in py.event.get():
            # check for closing window
            if event.type == py.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    self.player.jump()

    def draw(self):
        #Draw Game Loops
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        py.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        #Game Over/Continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

py.quit()
