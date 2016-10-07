#Game Options/Settings
TITLE = "Platformer"
WIDTH = 480
HEIGHT = 600
FPS = 60

#Player properities

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.5

#Starting platforms
PLATFORM_List = [(0,  HEIGHT-40, WIDTH, 40),
                 (WIDTH /2 - 50, HEIGHT *3/4, 100,20),
                 (100, HEIGHT- 250, 100, 20),
                 (220, 280, 75, 20 ),
                 (325, 300, 50, 20),
                 (400, 200, 50, 20),
                 (200, 400, 50, 20)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (255, 0, 255)
CYAN = (0, 255, 255)
