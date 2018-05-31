import pygame, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

# ===== Sizes ===== #
#Window
screenSize_X, screenSize_Y = 1280, 800
#Player
playerSize_X, playerSize_Y = 128, 96
#Martians
martSize_X, martSize_Y = 128, 96

# Print Window
surface = pygame.display.set_mode((screenSize_X, screenSize_Y))

# ===== Load files ===== #
# Open file
filePool = open ('filePool.txt').readlines()

counter = 0

while counter < len(filePool):

    file = filePool[counter].split()

    if file[0] == "Player":
        print ("Load file " + str(file[0]) + " => ", file[1])
        player_img = pygame.image.load(file[1])
        player_img = pygame.transform.scale(player_img, (playerSize_X,playerSize_Y))

    elif file[0] == "idle":
        print ("Load file " + str(file[0]) + " => ", file[1])
        idle_img = pygame.image.load(file[1])
        idle_img = pygame.transform.scale(idle_img, (playerSize_X,playerSize_Y))

    elif file[0] == "upDown":
        print ("Load file " + str(file[0]) + " => " , file[1])
        upDown_img = pygame.image.load(file[1])
        upDown_img = pygame.transform.scale(upDown_img, (playerSize_X,playerSize_Y))

    elif file[0] == "turnR":
        print ("Load file " + str(file[0]) + " => " , file[1])
        turnR_img = pygame.image.load(file[1])
        turnR_img = pygame.transform.scale(turnR_img, (playerSize_X,playerSize_Y))

    elif file[0] == "turnL":
        print ("Load file " + str(file[0]) + " => " , file[1])
        turnL_img = pygame.image.load(file[1])
        turnL_img = pygame.transform.scale(turnL_img, (playerSize_X,playerSize_Y))

    elif file[0] == "Martian1":
        print ("Load file " + str(file[0]) + " => " , file[1])
        mart1_img = pygame.image.load(file[1])
        mart1_img = pygame.transform.scale(mart1_img, (martSize_X,martSize_Y))

    elif file[0] == "Martian2":
        print ("Load file " + str(file[0]) + " => " , file[1])
        mart2_img = pygame.image.load(file[1])
        mart2_img = pygame.transform.scale(mart2_img, (martSize_X,martSize_Y))

    elif file[0] == "Martian3":
        print ("Load file " + str(file[0]) + " => " , file[1])
        mart3_img = pygame.image.load(file[1])
        mart3_img = pygame.transform.scale(mart3_img, (martSize_X,martSize_Y))

    elif file[0] == "Martian4":
        print ("Load file " + str(file[0]) + " => " , file[1])
        mart4_img = pygame.image.load(file[1])
        mart4_img = pygame.transform.scale(mart4_img, (martSize_X,martSize_Y))

    elif file[0] == "Background":
        print ("Load file " + str(file[0]) + " => " , file[1])
        background_img = pygame.image.load(file[1])
        background_img  = pygame.transform.scale(background_img , (screenSize_X,screenSize_Y))

    counter = counter + 1

# ===== Positions ===== #

player_posX = 0
player_posY = screenSize_Y - playerSize_Y

player_vel = 10

mart1_posX = []

mart1_posX = random.randint(0,screenSize_X - playerSize_X)
mart1_posY = -100

mart2_posX = random.randint(0,screenSize_X - playerSize_X)
mart2_posY = -300

mart3_posX = random.randint(0,screenSize_X - playerSize_X)
mart3_posY = -500

mart4_posX = random.randint(0,screenSize_X - playerSize_X)
mart4_posY = -700

mars_Dir = 1

exitGame = False

# ===== Game ===== # 
while not exitGame:

    # Clean window filling of color or image
    surface.fill((0,0,0))

    # Carga de archivos
    surface.blit(background_img, (0, screenSize_Y - screenSize_Y))
    surface.blit(player_img, (player_posX, player_posY))    
    surface.blit(mart1_img, (mart1_posX, mart1_posY))
    surface.blit(mart2_img, (mart2_posX, mart2_posY))
    surface.blit(mart3_img, (mart3_posX, mart3_posY))
    surface.blit(mart4_img, (mart4_posX, mart4_posY))

    # Martians movement
    mart1_posY = mart1_posY + mars_Dir * player_vel/2
    if mart1_posY >= screenSize_Y + martSize_Y:
        mart1_posX = random.randint(0, screenSize_X - playerSize_X)
        mart1_posY = 0

    mart2_posY = mart2_posY + mars_Dir * player_vel/2
    if mart2_posY >= screenSize_Y + martSize_Y:
        mart2_posX = random.randint(0, screenSize_X - playerSize_X)
        mart2_posY = 0

    mart3_posY = mart3_posY + mars_Dir * player_vel/2
    if mart3_posY >= screenSize_Y + martSize_Y:
        mart3_posX = random.randint(0, screenSize_X - playerSize_X)
        mart3_posY = 0

    mart4_posY = mart4_posY + mars_Dir * player_vel/2
    if mart4_posY >= screenSize_Y + martSize_Y:
        mart4_posX = random.randint(0, screenSize_X - playerSize_X)
        mart4_posY = 0

    #if mart1_posX >= screenSize_X - martSize_X:
     #   mars_Dir = -1
    #elif mart1_posX <= 0:
     #   mars_Dir = 1


    pygame.display.update()
    fpsClock.tick(30)

# ===== Inputs ===== #    

    keys = pygame.key.get_pressed()

    # Move left
    if keys[pygame.K_LEFT]:
        player_img = turnL_img
        player_posX = player_posX - player_vel
        if keys[pygame.K_DOWN]:
            player_posY = player_posY + player_vel
            # Lower limit
            if player_posY >= screenSize_Y - playerSize_Y:
               player_posY = screenSize_Y - playerSize_Y
        if keys[pygame.K_UP]:
            player_posY = player_posY - player_vel
            # Upper limit
            if player_posY <= 0:
               player_posY = 0
        # Left limit
        if player_posX <= 0:
           player_posX = 0
    # Move right
    elif keys[pygame.K_RIGHT]:
        player_img = turnR_img
        player_posX = player_posX + player_vel
        if keys[pygame.K_DOWN]:
            player_posY = player_posY + player_vel
            # Lower limit
            if player_posY >= screenSize_Y - playerSize_Y:
               player_posY = screenSize_Y - playerSize_Y
        if keys[pygame.K_UP]:
            player_posY = player_posY - player_vel
            # Upper limit
            if player_posY <= 0:
               player_posY = 0
        # Right limit
        if player_posX >= screenSize_X - playerSize_X:
           player_posX = screenSize_X - playerSize_X
    # Move up
    elif keys[pygame.K_UP]:
        player_img = upDown_img
        player_posY = player_posY - player_vel
        # Upper limit
        if player_posY <= 0:
           player_posY = 0
    # Move down
    elif keys[pygame.K_DOWN]:
        player_img = upDown_img
        player_posY = player_posY + player_vel
        # Lower limit
        if player_posY >= screenSize_Y - playerSize_Y:
           player_posY = screenSize_Y - playerSize_Y

    for Event in pygame.event.get():
        if Event.type == pygame.KEYUP:
            player_img = idle_img

# ===== Close ===== #

        if Event.type == pygame.QUIT:
            pygame.quit()
            exitGame = True
# ================= #     