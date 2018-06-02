import pygame, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

# ===== Sizes ===== #
#Window
screenSize_X, screenSize_Y = 600, 800

# Print Window
surface = pygame.display.set_mode((screenSize_X, screenSize_Y))

exitGame = False

while not exitGame:

    pygame.display.update()
    fpsClock.tick(30)

# ===== Close ===== #
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            pygame.quit()
            exitGame = True
# ================= #     
