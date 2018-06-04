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
        martSize_X, martSize_Y = int(file[2]), int(file[4])
        mart1_img = pygame.image.load(file[1])
        mart1_img = pygame.transform.scale(mart1_img, (martSize_X,martSize_Y))

    elif file[0] == "Martian2":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - tamaño => " + file[2] + " x " + file[4])
        mart2_img = pygame.image.load(file[1])
        mart2_img = pygame.transform.scale(mart2_img, (martSize_X,martSize_Y))

    elif file[0] == "Martian3":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - tamaño => " + file[2] + " x " + file[4])
        mart3_img = pygame.image.load(file[1])
        mart3_img = pygame.transform.scale(mart3_img, (martSize_X,martSize_Y))

    elif file[0] == "Martian4":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - tamaño => " + file[2] + " x " + file[4])
        mart4_img = pygame.image.load(file[1])
        mart4_img = pygame.transform.scale(mart4_img, (martSize_X,martSize_Y))

    elif file[0] == "Background":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - tamaño => " + file[2] + " x " + file[4])
        screenSize_X, screenSize_Y = int(file[2]), int(file[4])
        background_img = pygame.image.load(file[1])
        background_img  = pygame.transform.scale(background_img , (screenSize_X,screenSize_Y))

    counter = counter + 1
# ===== Animation ===== #
animSize_X, animSize_Y = 32,46
listaImagenes = []
animCounter = 0
while animCounter < len(animPool):

    file = animPool[animCounter].splitlines()

    anim_img = pygame.image.load(file[0])
    anim_img = pygame.transform.scale(anim_img, (animSize_X,animSize_Y))

    listaImagenes.append(anim_img)

    animCounter = animCounter + 1

# ===== Positions & bools ===== #

player_posX = 0
player_posY = screenSize_Y - playerSize_Y

player_vel = 10

mart1_posX = random.randint(0,screenSize_X - playerSize_X)
mart1_posY = -100

mart2_posX = random.randint(0,screenSize_X - playerSize_X)
mart2_posY = -300

mart3_posX = random.randint(0,screenSize_X - playerSize_X)
mart3_posY = -500

mart4_posX = random.randint(0,screenSize_X - playerSize_X)
mart4_posY = -700

mars_Dir = 1

posImagen = 0

animOffset = 28

exitGame = False

shooted = False
shoot_posX = -1000
shoot_posY = -1000
shootSpeed = 20

turnLeft = False
turnRight = False

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

    # Animations
    posImagen +=1
    if posImagen > len(listaImagenes)-1:
        posImagen = 0
    imagenAnim = listaImagenes[posImagen]

    # Clean window filling of color
    surface.fill((0,0,0))

    # Print files
    surface.blit(background_img, (0, screenSize_Y - screenSize_Y))
    surface.blit(player_img, (player_posX, player_posY))    
    surface.blit(mart1_img, (mart1_posX, mart1_posY))
    surface.blit(mart2_img, (mart2_posX, mart2_posY))
    surface.blit(mart3_img, (mart3_posX, mart3_posY))
    surface.blit(mart4_img, (mart4_posX, mart4_posY))
    # Print Animations
    surface.blit(imagenAnim, (player_posX + playerSize_X/2 - animSize_X/2, player_posY + playerSize_Y)) 


    if turnLeft == False :
        imagenAnim = pygame.transform.scale(imagenAnim, (animSize_X - 20,animSize_Y - 20))
        surface.blit(imagenAnim, (player_posX + 10, player_posY + playerSize_Y))

    if turnRight == False :
        imagenAnim = pygame.transform.scale(imagenAnim, (animSize_X - 20,animSize_Y - 20))
        surface.blit(imagenAnim, (player_posX + playerSize_X - animSize_X + 6, player_posY + playerSize_Y))

    # Martians movement
    mart1_posY = mart1_posY + mars_Dir * player_vel/2
    if mart1_posY >= screenSize_Y + martSize_Y:
        mart1_posX = random.randint(0, screenSize_X - mart1_posX)
        mart1_posY = 0

    mart2_posY = mart2_posY + mars_Dir * player_vel/2
    if mart2_posY >= screenSize_Y + martSize_Y:
        mart2_posX = random.randint(0, screenSize_X - mart2_posX)
        mart2_posY = 0

    mart3_posY = mart3_posY + mars_Dir * player_vel/2
    if mart3_posY >= screenSize_Y + martSize_Y:
        mart3_posX = random.randint(0, screenSize_X - mart3_posX)
        mart3_posY = 0

    mart4_posY = mart4_posY + mars_Dir * player_vel/2
    if mart4_posY >= screenSize_Y + martSize_Y:
        mart4_posX = random.randint(0, screenSize_X - mart4_posX)
        mart4_posY = 0


# ===== Inputs ===== #    

    keys = pygame.key.get_pressed()

# Fallo con los inputs, si tienes presionada la LEFT no puedes moverte hacia otra direccion
# las animaciones van raras con varias teclas presionadas.

    # Move left
    if keys[pygame.K_LEFT]:
        player_img = turnL_img
        player_posX = player_posX - player_vel
        turnLeft = True
        if turnLeft == True and turnRight == False:
            surface.blit(imagenAnim, (player_posX + animOffset + 12, player_posY + playerSize_Y))

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
        turnRight = True
        if turnRight == True and turnLeft == False:
            surface.blit(imagenAnim, (player_posX + playerSize_X -animOffset - animSize_X + 4, player_posY + playerSize_Y))


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
        player_posY = player_posY - player_vel
        # Upper limit
        if player_posY <= 0:
           player_posY = 0
    # Move down
    elif keys[pygame.K_DOWN]:
        player_posY = player_posY + player_vel
        # Lower limit
        if player_posY >= screenSize_Y - playerSize_Y:
           player_posY = screenSize_Y - playerSize_Y
    # shoot
    if keys[pygame.K_SPACE]:
        if not shooted:
            shooted = True
    if shooted:        
        Shoot(player_posX + playerSize_X/2, player_posY)

    pygame.display.update()
    fpsClock.tick(30)

    for Event in pygame.event.get():
        if Event.type == pygame.KEYUP:
            player_img = idle_img
            turnLeft = False
            turnRight = False

# ===== Close ===== #
        if Event.type == pygame.QUIT:
            pygame.quit()
            exitGame = True
# ================= #     