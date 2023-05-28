# MOVER UN OBJETO CON EL MOUSE/RATÓN

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

pygame.mouse.set_visible(1) # 1 = visible, 0 = invisible

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLANCO)

    #Para mover objetos con el mouse(en este ejemplo, un cuadrado)
    Pos_Mouse = pygame.mouse.get_pos()
    x = Pos_Mouse[0]
    y = Pos_Mouse[1]
    pygame.draw.rect(screen,AZUL,(x,y,100,100))
    pygame.display.flip()
    reloj.tick(60)
    #Se debería ver el puntero a la hora de mover el cuadrado por defecto