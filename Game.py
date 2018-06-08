import pygame, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

# ===== Open file ===== #
filePool = open ('filePool.txt').readlines()
animPool = open ('AnimPool.txt').readlines()
# ===== Load files ===== #
counter = 0
while counter < len(filePool):

    file = filePool[counter].split()

    if file[0] == "Player":
        print ("Load file " + str(file[0]) + " => ", file[1] + " - tamaño => " + file[2] + " x " + file[4])
        playerSize_X, playerSize_Y = int(file[2]), int(file[4])
        player_img = pygame.image.load(file[1])
        player_img = pygame.transform.scale(player_img, (playerSize_X,playerSize_Y))

    elif file[0] == "idle":
        print ("Load file " + str(file[0]) + " => ", file[1] + " - tamaño => " + file[2] + " x " + file[4])
        idle_img = pygame.image.load(file[1])
        idle_img = pygame.transform.scale(idle_img, (playerSize_X,playerSize_Y))

    elif file[0] == "turnR":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - tamaño => " + file[2] + " x " + file[4])
        turnR_img = pygame.image.load(file[1])
        turnR_img = pygame.transform.scale(turnR_img, (playerSize_X,playerSize_Y))

    elif file[0] == "turnL":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - tamaño => " + file[2] + " x " + file[4])
        turnL_img = pygame.image.load(file[1])
        turnL_img = pygame.transform.scale(turnL_img, (playerSize_X,playerSize_Y))

    elif file[0] == "shoot":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - tamaño => " + file[2] + " x " + file[4])
        shootSize_X, shootSize_Y = int(file[2]), int(file[4])
        shoot_img = pygame.image.load(file[1])
        shoot_img = pygame.transform.scale(shoot_img, (shootSize_X,shootSize_Y))

    elif file[0] == "Martian1":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - tamaño => " + file[2] + " x " + file[4])

        mart1_file = file[1]
        mart1_img = pygame.image.load(file[1])

        martSize_X, martSize_Y = int(file[2]), int(file[4])
        mart1_img = pygame.image.load(file[1])
        mart1_img = pygame.transform.scale(mart1_img, (martSize_X,martSize_Y))

    elif file[0] == "Background":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - tamaño => " + file[2] + " x " + file[4])
        screenSize_X, screenSize_Y = int(file[2]), int(file[4])
        background_img = pygame.image.load(file[1])
        background_img  = pygame.transform.scale(background_img , (screenSize_X,screenSize_Y))

    counter = counter + 1
# ===== Animations ===== #
PlayerAnimList = []
ExpAnimList = []
animCounter = 0
while animCounter < len(animPool):

    file = animPool[animCounter].split()

    if file[0] == "PlayerAnim":
        PlayerAnimSize_X, PlayerAnimSize_Y = int(file[2]), int(file[4])
        PlayerAnim_img = pygame.image.load(file[1])
        PlayerAnim_img = pygame.transform.scale(PlayerAnim_img, (PlayerAnimSize_X, PlayerAnimSize_Y))

        PlayerAnimList.append(PlayerAnim_img)
    
    if file[0] == "ExplosionAnim":
        ExplosionAnimSize_X, ExplosionAnimSize_Y = int(file[2]), int(file[4])
        ExplosionAnim_img = pygame.image.load(file[1])
        ExplosionAnim_img = pygame.transform.scale(ExplosionAnim_img, (ExplosionAnimSize_X, ExplosionAnimSize_Y))

        ExpAnimList.append(ExplosionAnim_img)

    animCounter = animCounter + 1
# ===== Martians ===== #
martNum = 4
martOnScreen = 0

mart1List = []
Mart1_pos = []

ini_posX = 0
cur_posX = 0

ini_posY = 0

DelayBtwMart = 10

while martOnScreen < martNum:

    mart1List.append(pygame.image.load(mart1_file))

    ini_posX = random.randint(0,screenSize_X - playerSize_X)
    ini_posY = random.randint(0 , screenSize_Y)

    Mart1_pos.append((ini_posX , ini_posY))

    martOnScreen = martOnScreen + 1

# ===== Positions & bools ===== #

player_posX = 0
player_posY = screenSize_Y - playerSize_Y

player_vel = 10

mart_posX = 0
mart_posY = 0

mars_Dir = 1

posImagen = 0

animOffset = 28

exitGame = False

shooted = False
shoot_posX = -1000
shoot_posY = -1000
shootSpeed = 20

Left = False
Right = False

# ===== Shoot ===== # 
def Shoot(x, y):

    global shoot_posX
    global shoot_posY
    global shootSpeed
    global shooted

    if shoot_posX == -1000:
        shoot_posX = x - shootSize_X/2
        shoot_posY = y

    surface.blit(shoot_img, (shoot_posX, shoot_posY - 35))

    contador = 0
        #while contador < len ()

#        if shootX >= mart1_posX and shootX <= mart1_posX + martSize_X:
#            if shootY >= mart1_posY and shootY <= mart + martSize_Y:
#                print("Muerto")

 #       contador = contador + 1
 #       
    shoot_posY = shoot_posY - shootSpeed

    if shoot_posY <= 0:
        shooted = False
        shoot_posX = -1000
        shoot_posY = -1000

# ===== Print Window ===== #
surface = pygame.display.set_mode((screenSize_X, screenSize_Y))



# ===== Game ===== # 
while not exitGame:

    print("Left " + str(Left))
    print("Right " + str(Right))

    # Player Animation
    posImagen +=1
    if posImagen > len(PlayerAnimList)-1:
        posImagen = 0
    imagenAnim = PlayerAnimList[posImagen]

    # Clean window filling of color
    surface.fill((0,0,0))

    # Print background
    surface.blit(background_img, (0, screenSize_Y - screenSize_Y))

    # Print Marts 1
    martCount = 0 
    while martCount < martNum:
        surface.blit(mart1List[martCount], (Mart1_pos[martCount]))
        martCount = martCount + 1

    # Print Player
    surface.blit(player_img, (player_posX, player_posY))    
    # Print Animations
    surface.blit(imagenAnim, (player_posX + playerSize_X/2 - PlayerAnimSize_X/2, player_posY + playerSize_Y)) 
    if Left == False :
        imagenAnim = pygame.transform.scale(imagenAnim, (PlayerAnimSize_X - 20,PlayerAnimSize_Y - 20))
        surface.blit(imagenAnim, (player_posX + 10, player_posY + playerSize_Y))

    if Right == False :
        imagenAnim = pygame.transform.scale(imagenAnim, (PlayerAnimSize_X - 20,PlayerAnimSize_Y - 20))
        surface.blit(imagenAnim, (player_posX + playerSize_X - PlayerAnimSize_X + 6, player_posY + playerSize_Y))


    # Martians movement
#    Mart1_pos[1] = mart_posY + mars_Dir * player_vel/2
#    mart_posY = mart_posY + mars_Dir * player_vel/2
#    if mart_posY >= screenSize_Y + martSize_Y:
#        Mart1_pos = random.randint(0, screenSize_X - mart_posX)
#        mart_posY = 0

 
# ===== Inputs ===== #    
    key = pygame.key.get_pressed()
    # Move Left
    if key[pygame.K_LEFT] and Left == True:
        player_img = turnL_img
        player_posX = player_posX - player_vel
        imagenAnim = pygame.transform.scale(imagenAnim, (PlayerAnimSize_X - 20,PlayerAnimSize_Y - 20))
        surface.blit(imagenAnim, (player_posX + animOffset + 12, player_posY + playerSize_Y))       
        # Move up
        if key[pygame.K_UP]:
            player_posY = player_posY - player_vel
            # Upper limit
            if player_posY <= 0:
               player_posY = 0
        # Move down
        if key[pygame.K_DOWN]:
            player_posY = player_posY + player_vel
            # Lower limit
            if player_posY >= screenSize_Y - playerSize_Y:
               player_posY = screenSize_Y - playerSize_Y
        # Left limit
        if player_posX <= 0:
            player_posX = 0
    # Move Right
    elif key[pygame.K_RIGHT] and Right == True:
        player_img = turnR_img
        player_posX = player_posX + player_vel
        imagenAnim = pygame.transform.scale(imagenAnim, (PlayerAnimSize_X - 20,PlayerAnimSize_Y - 20))
        surface.blit(imagenAnim, (player_posX + playerSize_X -animOffset - PlayerAnimSize_X + 4, player_posY + playerSize_Y))
        # Move up
        if key[pygame.K_UP]:
            player_posY = player_posY - player_vel
            # Upper limit
            if player_posY <= 0:
               player_posY = 0
        # Move down
        if key[pygame.K_DOWN]:
            player_posY = player_posY + player_vel
            # Lower limit
            if player_posY >= screenSize_Y - playerSize_Y:
               player_posY = screenSize_Y - playerSize_Y
        # Right limit
        if player_posX >= screenSize_X - playerSize_X:
           player_posX = screenSize_X - playerSize_X
    # Move up
    elif key[pygame.K_UP]:
        player_posY = player_posY - player_vel
        # Upper limit
        if player_posY <= 0:
           player_posY = 0
    # Move down
    elif key[pygame.K_DOWN]:
        player_posY = player_posY + player_vel
        # Lower limit
        if player_posY >= screenSize_Y - playerSize_Y:
           player_posY = screenSize_Y - playerSize_Y
# ===== Shoot ===== #
    if key[pygame.K_SPACE]:
        if not shooted:
            shooted = True
    if shooted:        
        Shoot(player_posX + playerSize_X/2, player_posY)
# ===== Update Window ===== #
    pygame.display.update()
    fpsClock.tick(30)
# ===== Check Keys ===== #
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            Left = True
            Right = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            Left = False
            Right = True
            player_img = idle_img
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            Left = False
            Right = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            Left = True
            Right = False
            player_img = idle_img
# ===== Close ===== #
    if event.type == pygame.QUIT:
        pygame.quit()
        exitGame = True
# ================= #
    