#Mover imágenes
import pygame, sys
pygame.init()

size = (600,600)
screen = pygame.display.set_mode(size)

fondo = pygame.image.load("../The Moon.jpeg").convert() #Reutilizamos el fondo du merda
Jugador = pygame.image.load("../parte 3/gato.jpg").convert()
Jugador.set_colorkey([0,0,0]) #Para hacer transparente el fondo de la imagen, si fuese .png
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]

    screen.blit(fondo, [0, 0])
    screen.blit(Jugador, [x, y])


    pygame.display.flip()