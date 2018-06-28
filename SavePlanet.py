import pygame, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

pygame.font.init()

# ===== Open file ===== #
main_files = open ('filePool.txt').readlines()
fx_files = open ('AnimPool.txt').readlines()
# ===== Load main files ===== #
counter = 0
while counter < len(main_files):

    file = main_files[counter].split()

    if file[0] == "Player":
        print ("Load file " + str(file[0]) + " => ", file[1] + " - Size => " + file[2] + " x " + file[4])
        playerSize_X, playerSize_Y = int(file[2]), int(file[4])
        player_img = pygame.image.load(file[1])
        player_img = pygame.transform.scale(player_img, (playerSize_X,playerSize_Y))

    elif file[0] == "idle":
        print ("Load file " + str(file[0]) + " => ", file[1] + " - Size => " + file[2] + " x " + file[4])
        idle_img = pygame.image.load(file[1])
        idle_img = pygame.transform.scale(idle_img, (playerSize_X,playerSize_Y))

    elif file[0] == "turnR":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - Size => " + file[2] + " x " + file[4])
        turnR_img = pygame.image.load(file[1])
        turnR_img = pygame.transform.scale(turnR_img, (playerSize_X,playerSize_Y))

    elif file[0] == "turnL":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - Size => " + file[2] + " x " + file[4])
        turnL_img = pygame.image.load(file[1])
        turnL_img = pygame.transform.scale(turnL_img, (playerSize_X,playerSize_Y))

    elif file[0] == "shoot":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - Size => " + file[2] + " x " + file[4])
        shootSize_X, shootSize_Y = int(file[2]), int(file[4])
        shoot_img = pygame.image.load(file[1])
        shoot_img = pygame.transform.scale(shoot_img, (shootSize_X,shootSize_Y))

    elif file[0] == "Martian1":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - Size => " + file[2] + " x " + file[4])

        mart1_file = file[1]
        mart1_img = pygame.image.load(file[1])

        martSize_X, martSize_Y = int(file[2]), int(file[4])
        mart1_img = pygame.image.load(file[1])
        mart1_img = pygame.transform.scale(mart1_img, (martSize_X,martSize_Y))

    elif file[0] == "Background":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - Size => " + file[2] + " x " + file[4])
        screenSize_X, screenSize_Y = int(file[2]), int(file[4])
        background_img = pygame.image.load(file[1])
        background_img  = pygame.transform.scale(background_img , (screenSize_X,screenSize_Y))
    elif file[0] == "FX":
        print ("Load file " + str(file[0]) + " => " , file[1] + " - Size => " + file[2] + " x " + file[4])
        screenSize_X, screenSize_Y = int(file[2]), int(file[4])
        FX_img = pygame.image.load(file[1])
        FX_img  = pygame.transform.scale(FX_img , (screenSize_X,screenSize_Y))

    counter = counter + 1
# ===== Print Window ===== #
surface = pygame.display.set_mode((screenSize_X, screenSize_Y))
# ===== Colors Var ===== #
White = (255,255,255)
Black = (0,0,0)
Red = (190,0,30)
# ===== Game fonts ===== #
def GameFont(txt, color, fontSize):

    return pygame.font.Font("Resources/Font.ttf", fontSize).render(txt, True, color)
# ===== Update Window ===== #
def Update():
    pygame.display.update()
    fpsClock.tick(30)
# ===== Close ===== #
def QuitGame():
    for quitGame in pygame.event.get():
        if quitGame.type == pygame.QUIT:
            pygame.quit()
            quit()
# ===== Player ===== #

player_posX = screenSize_X/2 - playerSize_X/2
player_posY = screenSize_Y + playerSize_Y
player_vel = 10
animStart = True

def PlayerPrint():

    global player_posX	
    global player_posY
    global animStart

    # ===== Anim Start ===== #
    if animStart == True:

        animStart_txt = GameFont("Save the planet !!!", Red, 40)

        if player_posY > 500:
            player_posY = player_posY - 1 * player_vel/2

                
        else:
            animStart = False

        animStart_x, animStart_y = animStart_txt.get_rect().size[0], animStart_txt.get_rect().size[1]
        surface.blit(animStart_txt, (screenSize_X/2 - animStart_x/2, screenSize_Y/2 - animStart_y/2))

    # ===== Print Player ===== #
    surface.blit(player_img, (player_posX, player_posY))

# ===== Shoot ===== #

#shooted = False
#shoot_posX = -1000
#shoot_posY = -1000
#shootSpeed = 30

#def Shoot(x, y):

#    global shoot_posX
#    global shoot_posY
#    global shootSpeed
#    global shooted
#    global score
#    global score_txt

#    IsDead = False
#    contador = 0

#    if shoot_posX == -1000:
#        shoot_posX = x - shootSize_X/2
#        shoot_posY = y

#    surface.blit(shoot_img, (shoot_posX, shoot_posY - 35))

#    while contador < len(MartList_pos) and not IsDead:

#        x_mart, y_mart = MartList_pos[contador] 

#        if shoot_posX >= x_mart and shoot_posX <= x_mart + martSize_X:
#            if shoot_posY >= y_mart and shoot_posY <= y_mart + martSize_Y:

#                shooted = False
#                shoot_posX = -1000
#                shoot_posY = -1000

#                Exp_posX = x_mart
#                Exp_posY = y_mart

#                #del MartList[contador]
#                #del MartList_pos[contador]
                
#                MartList_pos[contador] = (random.randint(0,screenSize_X - martSize_X), -500)

#                y_mart = y_mart + y_mart

#                #Explosion(x_mart, y_mart)

#                IsDead = True

#                score = score + 1
#                score_txt = GameFont("Score: " + str(score), Red, 32)

#        contador = contador + 1
       
#    shoot_posY = shoot_posY - shootSpeed

#    if shoot_posY <= 0:
#        shooted = False
#        shoot_posX = -1000
#        shoot_posY = -1000

# ===== Background ===== # 
background1_posY = screenSize_Y/2
background2_posY = screenSize_Y/2 - screenSize_Y
background_vel = player_vel/4
def Background():

    global background1_posY
    global background2_posY

    # =====  Scrolling background ===== #
    if not intro:
        background1_posY += 1 * background_vel
        background2_posY += 1 * background_vel

    # Print background
    surface.blit(background_img, (0, background1_posY ))
    surface.blit(background_img, (0, background2_posY))

    if background1_posY >= screenSize_Y:
        background1_posY = screenSize_Y - screenSize_Y*2
    if background2_posY >= screenSize_Y:
        background2_posY = screenSize_Y - screenSize_Y*2

# ===== Button ===== #

def Button(txt, x, y, action = None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    bttn_txt = GameFont(txt, White, 70)
    bttnSize_x, bttnSize_y = bttn_txt.get_rect().size[0], bttn_txt.get_rect().size[1]

    bttnPosX = x - bttnSize_x/2
    bttnPosY = y - bttnSize_y/2

    if bttnPosX + bttnSize_x > mouse[0] > bttnPosX and bttnPosY + bttnSize_y > mouse[1] > bttnPosY:

        bttn_txt = GameFont(txt, Red, 70)
        
        if click[0] == 1 and action != None:
            action()
    else:
        bttn_txt = GameFont(txt, White, 70)

    surface.blit(bttn_txt, (bttnPosX, bttnPosY))
# ===== Inputs ===== #



def Inputs():

    Left = False
    Right = False
    IsPushed = []

    global player_img
    global player_posX
    global player_posY
    global shooted

    key = pygame.key.get_pressed()
    print('entra a input')
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

## ===== Shoot ===== #
#    if key[pygame.K_SPACE]:
#        if not shooted:
#            shooted = True
#    if shooted:        
#        Shoot(player_posX + playerSize_X/2, player_posY)

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

# ===== Game Control Var ===== #

intro = True
game = True
gameOver = True

def Scenes():

	global intro
	global game
	global gameOver

	key = pygame.key.get_pressed()

	if key[pygame.K_SPACE]:

		intro = False

# ===== Intro ===== #
def IntroScene():

    global intro
    global game
    global gameOver

    while intro == True:

        # Clean window filling of color
        surface.fill(Black)

        Background()
        Button('START', screenSize_X/2, screenSize_Y/3, GameScene)

        txt = ''
        HiScore_txt = GameFont(txt, White, 32)

        HiScore_x, HiScore_y = HiScore_txt.get_rect().size[0], HiScore_txt.get_rect().size[1]
        surface.blit(HiScore_txt, (screenSize_X/2 - HiScore_x/2, screenSize_Y/2 - HiScore_y/2))

        Update()
        Scenes()
        QuitGame()
        print('Estas en Intro')

# ===== Game ===== #
def GameScene():

    global intro
    global game
    global gameOver

    while game:

        # Clean window filling of color
        surface.fill(Black)

        Background()

        Game_x, Game_y = Game_txt.get_rect().size[0], Game_txt.get_rect().size[1]
        surface.blit(Game_txt, (screenSize_X/2 - Game_x/2, screenSize_Y/2 - Game_y/2))

        PlayerPrint()
        #Inputs()
        #Shoot()
        Update()
        #Scenes()
        QuitGame()
        print('Game ' + str(game))

# ===== GameOver ===== #
def GameOverScene():

	global intro
	global game
	global gameOver

	while gameOver:

		# Clean window filling of color
		surface.fill(Black)

		GameOver_txt = GameFont('GameOver', White, 32)

		GameOver_x, GameOver_y = GameOver_txt.get_rect().size[0], GameOver_txt.get_rect().size[1]
		surface.blit(GameOver_txt, (screenSize_X/2 - GameOver_x/2, screenSize_Y/2 - GameOver_y/2))

		Update()
		QuitGame()
		print('GameOver ' + str(gameOver))


IntroScene()
GameScene()
GameOverScene()
Update()
QuitGame()