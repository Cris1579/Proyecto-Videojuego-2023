
import pygame, sys
pygame.init() #Con este comando se inicia la lib pygame

size = (800,500) #Tupla (Lista que no se puede modificar), tamaño de la ventana

#Crear ventana
screen = pygame.display.set_mode(size)

#Un juego no es más que un bucle gigante, por ende, creamos un bucle "infinito"
#Bucle Principal, Estructura para cerrar la ventana
while True:
    for event in pygame.event.get():
        #print(event) #Colocando el print, en el terminal se nos muestra TODO lo que hagamos(Mouse,Teclado)
        if event.type == pygame.QUIT: #pygame.QUIT quiere decir que si apretamos la X de la ventana, se cierra, duh.
            sys.exit()

