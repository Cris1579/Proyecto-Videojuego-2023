#Para agregar un fondo/imagen en la ventana

import pygame,sys

size = (700,700) #Aquí dependiendo del tamaño de la imagen, se redimensiona la ventana
screen = pygame.display.set_mode(size)

#Para incluir la imagen

fondo = pygame.image.load("../The Moon.jpeg").convert()
# .convert() facilita el trabajo para pygame para usar imágenes
# pygame.image.load() carga una imagen de algún archivo
# IMPORTANTE: La imagen y el archivo.py deben estar en la misma carpeta

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(fondo,[0,0]) # (variable, [Pos_X, Pos_Y])
    # Se utiliza .blit , ya que dibuja la imagen en la pantalla
    # .fill solo rellena algo con un color en especifico
    pygame.display.flip()
    #NOTA: Pygame no redimensiona imágenes