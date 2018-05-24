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

	elif elemento[0] == "marcianito1":
		print ("Cargando grafico " + str(elemento[0]) + " => " , elemento[1])


	contador = contador + 1

while True:

    pygame.display.update()
    fpsClock.tick(30)

