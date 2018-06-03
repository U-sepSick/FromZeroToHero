import pygame, sys, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
# ===== Sizes ===== #
#Window
screenSize_X, screenSize_Y = 600, 800
#Player
playerSize_X, playerSize_Y = 64, 64 


# Print Window
surface = pygame.display.set_mode((screenSize_X, screenSize_Y))

# ===== Load files ===== #
# Open file
animPool = open ('AnimPool.txt').readlines()
animCounter = 0

listaImagenes = []

while animCounter < len(animPool):

    file = animPool[animCounter].splitlines()

    anim_img = pygame.image.load(file[0])
    anim_img = pygame.transform.scale(anim_img, (playerSize_X,playerSize_Y))

    listaImagenes.append(anim_img)

    animCounter = animCounter + 1

# ===== Positions ===== #
anim_posX = screenSize_X/2 - playerSize_X/2
anim_posY = screenSize_Y/2 - playerSize_Y/2

exitGame = False

resetAnim = False

posImagen = 0
#tiempoCambio = 1

tiempoCambio = 1

velocidad = 10

# ===== Game ===== # 
while not exitGame:

#    tiempo = int(pygame.time.get_ticks()/1000)

 #   if tiempoCambio == tiempo:
    posImagen +=1
        #tiempoCambio += 1

    if posImagen > len(listaImagenes)-1:
        posImagen = 0
   
    #tiempo = int(pygame.time.get_ticks()/1000)

    #if tiempoCambio == tiempo:
    #    posImagen +=1
    #    tiempoCambio += 1

    #    if posImagen > len(listaImagenes)-1:
    #        posImagen = 0
                   
    #print ("Tiempocambio " + str(tiempoCambio))
#    print ("Tiempo " + str(tiempo))

    print ("Posicion Imagen " + str(posImagen))
    print ("======================")

    imagenAnim = listaImagenes[posImagen]

    # Clean window filling of color
    surface.fill((0,0,0))

    # Print files
    surface.blit(imagenAnim, (anim_posX, anim_posY))   
    
    pygame.display.update()
    fpsClock.tick(30)

# ===== Close ===== #
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            pygame.quit()
            exitGame = True
# ================= #     
