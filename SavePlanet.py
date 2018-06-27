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
def PlayerPrint():

	global player_posX
	global player_posY

	# ===== Print Player ===== #
	surface.blit(player_img, (player_posX, player_posY))

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

		Intro_txt = GameFont('Intro', White, 32)

		Intro_x, Intro_y = Intro_txt.get_rect().size[0], Intro_txt.get_rect().size[1]
		surface.blit(Intro_txt, (screenSize_X/2 - Intro_x/2, screenSize_Y/2 - Intro_y/2))

		Update()
		Scenes()
		QuitGame()
        print('Intro ' + str(intro))

# ===== Game ===== #
def GameScene():

	global intro
	global game
	global gameOver

	while game:

		# Clean window filling of color
		surface.fill(Black)

		Background()

		Game_txt = GameFont('Game', White, 32)

		Game_x, Game_y = Game_txt.get_rect().size[0], Game_txt.get_rect().size[1]
		surface.blit(Game_txt, (screenSize_X/2 - Game_x/2, screenSize_Y/2 - Game_y/2))

		Update()
		Scenes()
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