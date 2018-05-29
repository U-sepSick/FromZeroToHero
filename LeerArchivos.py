import pygame
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

width = 1280
height = 800

surface = pygame.display.set_mode((width, height))

contenido = open ('Ficheros.txt').readlines()

contador = 0

while contador < len(contenido):
    elemento = contenido[contador].split()

    if elemento[0] == "nave":
        print ("Cargando grafico " + str(elemento[0]) + " => ", elemento[1])
        nave_img = pygame.image.load(elemento[1])
        nave_w, nave_h = nave_img.get_rect().size[0],nave_img.get_rect().size[1]

    elif elemento[0] == "marcianito1":
        print ("Cargando grafico " + str(elemento[0]) + " => " , elemento[1])
        mar1_img = pygame.image.load(elemento[1])
        mar1_w, mar1_h = mar1_img.get_rect().size[0],mar1_img.get_rect().size[1]

    contador = contador + 1

while True:
    surface.blit(mar1_img, (0,height/2-mar1_h/2))
    surface.blit(nave_img, (width-nave_w, height/2-nave_h/2))

    pygame.display.update()
    fpsClock.tick(30)