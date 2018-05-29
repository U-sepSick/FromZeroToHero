import pygame
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

# Sizes
screen_w = 1280
screen_h = 800
nave_size_x, nave_size_y = 128,96
mar_size_x, mar_size_y = 128,96

surface = pygame.display.set_mode((screen_w, screen_h))

filePool = open ('filePool.txt').readlines()

counter = 0

while counter < len(filePool):

    file = filePool[counter].split()

    if file[0] == "nave":
        print ("Cargando grafico " + str(file[0]) + " => ", file[1])
        nave_img = pygame.image.load(file[1])
        nave_img = pygame.transform.scale(nave_img, (nave_size_x,nave_size_y))
        nave_w, nave_h = nave_img.get_rect().size[0],nave_img.get_rect().size[1]

    elif file[0] == "marcianito1":
        print ("Cargando grafico " + str(file[0]) + " => " , file[1])
        mar1_img = pygame.image.load(file[1])
        mar1_img = pygame.transform.scale(mar1_img, (mar_size_x,mar_size_y))
        mar1_w, mar1_h = mar1_img.get_rect().size[0],mar1_img.get_rect().size[1]

    elif file[0] == "marcianito2":
        print ("Cargando grafico " + str(file[0]) + " => " , file[1])
        mar2_img = pygame.image.load(file[1])
        mar2_img = pygame.transform.scale(mar2_img, (mar_size_x,mar_size_y))
        mar2_w, mar2_h = mar2_img.get_rect().size[0],mar2_img.get_rect().size[1]

    elif file[0] == "marcianito3":
        print ("Cargando grafico " + str(file[0]) + " => " , file[1])
        mar3_img = pygame.image.load(file[1])
        mar3_img = pygame.transform.scale(mar3_img, (mar_size_x,mar_size_y))
        mar3_w, mar3_h = mar3_img.get_rect().size[0],mar3_img.get_rect().size[1]

    elif file[0] == "fondo":
        print ("Cargando grafico " + str(file[0]) + " => " , file[1])
        fondo_img = pygame.image.load(file[1])
        fondo_img  = pygame.transform.scale(fondo_img , (screen_w,screen_h))
        fondo_w, fondo_h = fondo_img.get_rect().size[0],fondo_img.get_rect().size[1]

    elif file[0] == "meteo":
        print ("Cargando grafico " + str(file[0]) + " => " , file[1])
        met_img = pygame.image.load(file[1])
        met_img  = pygame.transform.scale(met_img , (screen_w,screen_h))
        met_w, met_h = met_img.get_rect().size[0],met_img.get_rect().size[1]

    counter = counter + 1

# Movement

nave_x = 0
nave_y = screen_h - nave_h

nave_vel = 10

mar1_x = 0
mar2_x = screen_w - mar2_w
mar3_x = 0

marDir = 1

exitGame = False

while not exitGame:

    # Rellenar de un color para limpiar la pantalla
    surface.fill((0,0,0))

    # Carga de archivos
    surface.blit(fondo_img, (0, screen_h - fondo_h))
    surface.blit(nave_img, (nave_x, nave_y))
    surface.blit(mar1_img, (mar1_x, screen_h/2 - mar1_h/2))
    surface.blit(mar2_img, (mar2_x, screen_h/2 - mar2_h/2))
    surface.blit(mar3_img, (mar3_x,0))
    #surface.blit(met_img, (0, screen_h - met_h))


  
# Mars movement

    mar1_x = mar1_x + marDir * nave_vel/2
    mar2_x = mar2_x - marDir * nave_vel/2

    if mar1_x >= screen_w - mar1_w:
        marDir = -1
    elif mar1_x <= 0:
        marDir = 1


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

    # Bloqueo para que no se salga la nave
    if nave_x <= 0:
        nave_x = 0

    elif nave_x >= screen_w - nave_size_x:
        nave_x = screen_w - nave_size_x

    elif nave_y <= 0:
        nave_y = 0

    elif nave_y >= screen_h - nave_size_y:
        nave_y = screen_h - nave_size_y


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exitGame = True
