# EJEMPLO DE COMO ANIMAR UN OBJETO
# EN ESTE CASO, QUE REBOTE UN CUADRADO

import pygame, sys
pygame.init()

size = (800,500)

NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL =  (0,0,255)

screen = pygame.display.set_mode(size)
#Para controlar los FPS
reloj = pygame.time.Clock()

# Esto debe ir fuera del bucle, para poder cambiar las variables
# Coordenadas del cuadrado
cord_x = 400
cord_y = 200
#Velocidad a la que se moverá el cuadrado
speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(BLANCO)

    #Para que "rebote"
    if (cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if (cord_y > 420 or cord_y < 0):
        speed_y *= -1
    #Esta línea hace el "movimiento"
    cord_x += speed_x
    cord_y += speed_y

    ###--- Zona de dibujo

    pygame.draw.rect(screen,ROJO,(cord_x,cord_y,80,80))

    ###--- Zona de dibujo
    reloj.tick(60)
    pygame.display.flip()