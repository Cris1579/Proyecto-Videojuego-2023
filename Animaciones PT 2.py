# EJEMPLO DE COMO ANIMAR EL AMBIENTE
# EN ESTE CASO, QUE HAYA UN EFECTO NIEVE EN LA PANTALLA

import pygame, sys, random
pygame.init()

size = (800,500)
screen = pygame.display.set_mode(size)
reloj = pygame.time.Clock()

NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL =  (0,0,255)

#Un bucle para el efecto "nieve"
coor_list = []
for i in range(70):
    x = random.randint(0,800)
    y = random.randint(0,500)
    coor_list.append([x,y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLANCO)

    #Para el efecto "nieve"
    for coord in coor_list:
        pygame.draw.circle(screen,AZUL,coord,2)
        coord[1] += 1       #Movimiento en Y
        if coord[1] > 500:  #Cuando la "nieve" toque la parte baja de la ventana, se generan nuevos
            coord[1] = 0

    pygame.display.flip()
    reloj.tick(60)