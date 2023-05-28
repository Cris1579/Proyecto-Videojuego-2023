#MOVER OBJETOS CON EL KEYBOARD/TECLADO

import pygame, sys
pygame.init()

NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL =  (0,0,255)

size = (800,500)

screen = pygame.display.set_mode(size)
reloj = pygame.time.Clock()

#Coordenadas del cuadrado
coord_x = 10
coord_y = 10
#Velocidad
speed_x = 0
speed_y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # EVENTOS TECLADO
        if event.type == pygame.KEYDOWN: #Cuando se presiona una tecla, en este caso, las flechas
            if event.key == pygame.K_LEFT:
                speed_x = -3
            elif event.key == pygame.K_RIGHT:
                speed_x = 3
            elif event.key == pygame.K_UP:
                speed_y = -3
            elif event.key == pygame.K_DOWN:
                speed_y = 3
        if event.type == pygame.KEYUP: #Cuando se deja de presionar una tecla
            if event.key == pygame.K_LEFT:
                speed_x = 0
            elif event.key == pygame.K_RIGHT:
                speed_x = 0
            elif event.key == pygame.K_UP:
                speed_y = 0
            elif event.key == pygame.K_DOWN:
                speed_y = 0
    screen.fill(BLANCO)

    #Movimiento
    coord_x += speed_x
    coord_y += speed_y

    #Para mover objetos con el teclado(en este ejemplo, un cuadrado)
    pygame.draw.rect(screen,VERDE,(coord_x,coord_y,100,100))
    pygame.display.flip()
    reloj.tick(60)
