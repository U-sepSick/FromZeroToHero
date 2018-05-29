import pygame
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

screen_w = 1280
screen_h = 800

surface = pygame.display.set_mode((screen_w, screen_h))

filePool = open ('filePool.txt').readlines()

counter = 0

while counter < len(filePool):

    file = filePool[counter].split()

    if file[0] == "nave":
        print ("Cargando grafico " + str(file[0]) + " => ", file[1])
        nave_img = pygame.image.load(file[1])
        nave_img = pygame.transform.scale(nave_img, (128,96))
        nave_w, nave_h = nave_img.get_rect().size[0],nave_img.get_rect().size[1]

    elif file[0] == "marcianito1":
        print ("Cargando grafico " + str(file[0]) + " => " , file[1])
        mar1_img = pygame.image.load(file[1])
        mar1_img = pygame.transform.scale(mar1_img, (128,96))
        mar1_w, mar1_h = mar1_img.get_rect().size[0],mar1_img.get_rect().size[1]

    elif file[0] == "marcianito2":
        print ("Cargando grafico " + str(file[0]) + " => " , file[1])
        mar2_img = pygame.image.load(file[1])
        mar2_img = pygame.transform.scale(mar2_img, (128,96))
        mar2_w, mar2_h = mar2_img.get_rect().size[0],mar2_img.get_rect().size[1]

    elif file[0] == "marcianito3":
        print ("Cargando grafico " + str(file[0]) + " => " , file[1])
        mar3_img = pygame.image.load(file[1])
        mar3_img = pygame.transform.scale(mar3_img, (128,96))
        mar3_w, mar3_h = mar3_img.get_rect().size[0],mar3_img.get_rect().size[1]

    elif file[0] == "fondo":
        print ("Cargando grafico " + str(file[0]) + " => " , file[1])
        fondo_img = pygame.image.load(file[1])
        fondo_img  = pygame.transform.scale(fondo_img , (1280,800))
        fondo_w, fondo_h = fondo_img.get_rect().size[0],fondo_img.get_rect().size[1]

    counter = counter + 1

nave_x = 0
nave_y = screen_h-nave_h
nave_vel = 5

exitGame = False

while not exitGame:
    # Rellenar de un color para limpiar la pantalla
    surface.fill((0,0,0))
    # Carga de archivos
    surface.blit(fondo_img, (0,screen_h-fondo_h))
    surface.blit(nave_img, (nave_x, nave_y))
    surface.blit(mar1_img, (0,screen_h/2-mar1_h/2))
    surface.blit(mar2_img, (screen_w-mar2_w,screen_h/2-mar2_h/2))
    surface.blit(mar3_img, (0,0))
    
    pygame.display.update()
    fpsClock.tick(30)
  
# Inputs
    keys = pygame.key.get_pressed()

    # Mover izquierda
    if keys[pygame.K_LEFT]:
        nave_x = nave_x - nave_vel

    # Mover derecha
    elif keys[pygame.K_RIGHT]:
        nave_x = nave_x + nave_vel

    # Mover arriba
    elif keys[pygame.K_UP]:
        nave_y = nave_y - nave_vel

    # Mover abajo
    elif keys[pygame.K_DOWN]:
        nave_y = nave_y + nave_vel

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exitGame = True
