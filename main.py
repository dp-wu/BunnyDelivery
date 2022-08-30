import sys
import pygame

from settings import *
from Scene.scene1 import Scene1

# 1 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 2 - Load assets: image(s), sounds,  etc.
background = Scene1('Asset/Sprites/bg_scene1.png', (0, WINDOW_HEIGHT-SCENE_HEIGHT))

# 3 - Initialize variables


# 4 - Loop forever
while True:

    # 5 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 6  Do any "per frame" actions

    # 7 - Clear the window
    window.fill(WHITE)
    window.blit(background.image, background.rect)

    # 8 - Draw all window elements

    # 9 - Update the window
    pygame.display.update()

    # 10 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
