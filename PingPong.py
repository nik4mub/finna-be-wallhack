# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 720
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (255, 0, 255)
CYAN = (0, 255, 255)

font_name = pygame.font.match_font('times')
def text(surf,text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topright = (x,y)
    surf.blit(text_surface, text_rect)
#Creates Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        #Required by pygames---Runs the built in Sprite classes initializer
        pygame.sprite.Sprite.__init__(self)
        #Define image propery -sprite requires image-
        self.image = pygame.Surface((15,100))
        self.image.fill(WHITE)
        #Defines the sprite's rect -sprite requires rect-
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH /2, HEIGHT/2)
        #Sets intial speed in the y direction
        self.speedy = 0

    def update(self):
        self.speedy = 0
        #Gets list of keyboard buttons
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_DOWN]:
            self.speedy = -5
        if keystate[pygame.K_UP]:
            self.speedy = 5
        self.rect.y += self.speedy
        #Makes the length
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
    def shoot(self):
        #where the bullet will be fired from --bottom bulet on top of left side of buler
        bullet = Bullet( self.rect.centerx, self.rect.left)
        all_sprites.add(bullet)
        bullets.add(bullet)
#Creates enemies
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        #Required by pygames---Runs the built in Sprite classes initializer
        pygame.sprite.Sprite.__init__(self)
        #Define image propery -sprite requires image-
        self.image = pygame.Surface((25,25))
        self.image.fill(CYAN)
        #Defines the sprite's rect -sprite requires rect-
        self.rect = self.image.get_rect()
        #Randomizes enemies
        self.rect.y= random.randrange(WIDTH - self.rect.width)
        self.rect.x = random.randrange(-100, 140)
        self.speedx = random.randrange(1,8)
        self.speedy = random.randrange(-5,5)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH + 10 or self.rect.top > HEIGHT + 20 or self.rect.bottom > HEIGHT + 20:
        #Rerandomizes somewhere on the side
            self.rect.y= random.randrange(WIDTH - self.rect.width)
            self.rect.x = random.randrange(-100, 140)
            self.speedx = random.randrange(1,8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(VIOLET)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = -10
    def update(self):
        self.rect.x += self.speedx
        #kill it if not on screen
        if self.rect.left < 0:
            self.kill()

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Explosive Ping Pong")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
#Hold Group of mobs to tell if we hit the mobs
mobs = pygame.sprite.Group()
#Hold Group of bullets to tell if we hit the mobs
bullets = pygame.sprite.Group()
#Add player Object
player = Player()
#Addd player sprite
all_sprites.add(player)

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
# Game loop
score = 0
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

    # Update
    all_sprites.update()

    #Check to see if bullet hits mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    #Spawns more enemies after killing range(8)
    for hit in hits:
        score += 1
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    #Checks to see if mob hits player
    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        running = True

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    text(screen, str(score), 20, WIDTH/ 4, 10)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
