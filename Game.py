import pygame, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

# ===== Open file ===== #
filePool = open ('filePool.txt').readlines()
animPool = open ('AnimPool.txt').readlines()
# ===== Load main files ===== #
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
# ===== Load animations files ===== #
MotorAnimList = []
motorImgPos = 0
ExpAnimList = []
animCounter = 0
while animCounter < len(animPool):

    file = animPool[animCounter].split()

    if file[0] == "PlayerAnim":
        PlayerAnimSize_X, PlayerAnimSize_Y = int(file[2]), int(file[4])
        PlayerAnim_img = pygame.image.load(file[1])
        PlayerAnim_img = pygame.transform.scale(PlayerAnim_img, (PlayerAnimSize_X, PlayerAnimSize_Y))

        MotorAnimList.append(PlayerAnim_img)
    
    if file[0] == "ExplosionAnim":
        ExplosionAnimSize_X, ExplosionAnimSize_Y = int(file[2]), int(file[4])
        ExplosionAnim_img = pygame.image.load(file[1])
        ExplosionAnim_img = pygame.transform.scale(ExplosionAnim_img, (ExplosionAnimSize_X, ExplosionAnimSize_Y))

        ExpAnimList.append(ExplosionAnim_img)

    animCounter = animCounter + 1
# ===== Player Var ===== #
player_posX = screenSize_X/2 - playerSize_X/2
player_posY = screenSize_Y/2 - playerSize_Y/2
player_vel = 10
# ===== Martians Var ===== #
mart_posX = 0
mart_posY = 0
mars_Dir = 1
# ===== Check Keys Var ===== #
Left = False
Right = False
IsPushed = []
# ===== Martians ===== #

martNum = 4
martOnScreen = 0

mart1List = []
Mart1_pos = []

ini_posX = 0
ini_posY = 0
cur_posY = 0

while martOnScreen < martNum:

    mart1List.append(pygame.image.load(mart1_file))

    ini_posX = random.randint(0,screenSize_X - playerSize_X)
    ini_posY = random.randint(screenSize_Y , screenSize_Y + ini_posY)

    #cur_posY = ini_posY
    Mart1_pos.append((ini_posX , ini_posY))

    martOnScreen = martOnScreen + 1

# ===== Background ===== # 
background1_posY = screenSize_Y/2
background2_posY = screenSize_Y/2 - screenSize_Y
background_vel = player_vel/4
# ===== Shoot ===== # 
shooted = False
shoot_posX = -1000
shoot_posY = -1000
shootSpeed = 30
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
# ===== Explosion ===== # 
Explosion = False
Exp_posX = -1000
Exp_posY = -1000
def Explosion (x, y):
    global Exp_posX
    global Exp_posY

    if Exp_posX == -1000:
        Exp_posX = x - ExplosionAnimSize_X/2
        if Exp_posY == -1000:
            Exp_posY = y - ExplosionAnimSize_Y/2
# ========== # 
exitGame = False
# ===== Print Window ===== #
surface = pygame.display.set_mode((screenSize_X, screenSize_Y))
# ===== Game ===== # 
while not exitGame:

    print ("IsPushed " + str(IsPushed))
    print ("Mart1_pos " + str(Mart1_pos[1]))
    # Player Animation
    motorImgPos +=1
    if motorImgPos > len(MotorAnimList)-1:
        motorImgPos = 0
    motorAnim = MotorAnimList[motorImgPos]

    # Clean window filling of color
    surface.fill((0,0,0))
# =====  Scrolling background ===== #
    background1_posY += 1 * background_vel
    background2_posY += 1 * background_vel
    # Print background
    surface.blit(background_img, (0, background1_posY ))
    surface.blit(background_img, (0, background2_posY))
    if background1_posY >= screenSize_Y:
        background1_posY = screenSize_Y - screenSize_Y*2
    if background2_posY >= screenSize_Y:
        background2_posY = screenSize_Y - screenSize_Y*2
#===================#
   
    # Print Marts 1
    martCount = 0 
    while martCount < martNum:
        surface.blit(mart1List[martCount], (Mart1_pos[martCount]))
        martCount = martCount + 1

    # Martians movement
    #Mart1_pos[(1,1)] = cur_posY
#    mart_posY = mart_posY + mars_Dir * player_vel/2
#    if mart_posY >= screenSize_Y + martSize_Y:
#        Mart1_pos = random.randint(0, screenSize_X - mart_posX)
#        mart_posY = 0

# ===== Print Player ===== #
    surface.blit(player_img, (player_posX, player_posY))
# ===== Print Animations ===== #
    # Main Motor
    surface.blit(motorAnim, (player_posX + playerSize_X/2 - PlayerAnimSize_X/2, player_posY + playerSize_Y)) 
    # Side Motors
    motorAnim = pygame.transform.scale(motorAnim, (PlayerAnimSize_X - 20,PlayerAnimSize_Y - 20))
    if Left == True and IsPushed[len(IsPushed)-1] == "Left":
        motorLeft_posX = player_posX + playerSize_X/2 - 35
        motorRight_posX = player_posX + playerSize_X/2 + 38
    if Right == True and IsPushed[len(IsPushed)-1] == "Right":
        motorLeft_posX = player_posX + playerSize_X/2 - 53
        motorRight_posX = player_posX + playerSize_X/2 + 20
    if Left == False and Right == False:
        motorLeft_posX = player_posX + playerSize_X/2 - 53
        motorRight_posX = player_posX + playerSize_X/2 + 38
    surface.blit(motorAnim, (motorLeft_posX, player_posY + playerSize_Y))
    surface.blit(motorAnim, (motorRight_posX, player_posY + playerSize_Y))
# ===== Inputs ===== #    
    key = pygame.key.get_pressed()
    # Move Left
    if key[pygame.K_LEFT] and IsPushed[len(IsPushed)-1] == "Left":
        player_img = turnL_img
        player_posX = player_posX - player_vel
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
    elif key[pygame.K_RIGHT] and IsPushed[len(IsPushed)-1] == "Right":
        player_img = turnR_img
        player_posX = player_posX + player_vel
        # move up
        if key[pygame.K_UP]:
            player_posY = player_posY - player_vel
            # upper limit
            if player_posY <= 0:
               player_posY = 0
        # move down
        if key[pygame.K_DOWN]:
            player_posY = player_posY + player_vel
            # lower limit
            if player_posY >= screenSize_Y - playerSize_Y:
               player_posY = screenSize_Y - playerSize_Y
        # right limit
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
# ===== Check Keys ===== #
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            IsPushed.append("Left")
            Left = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            IsPushed.remove("Left")
            Left = False
            player_img = idle_img
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            Right = True
            IsPushed.append("Right")
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            Right = False
            IsPushed.remove("Right")
            player_img = idle_img
# ===== Update Window ===== #
    pygame.display.update()
    fpsClock.tick(30)
# ===== Close ===== #
    if event.type == pygame.QUIT:
        pygame.quit()
        exitGame = True
# ================= #