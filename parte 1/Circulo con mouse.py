import pygame
# Inicializar Pygame
pygame.init()

NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL =  (0,0,255)
# Definir las dimensiones de la ventana de visualización
width = 640
height = 480

# Crear la ventana de visualización
screen = pygame.display.set_mode((width, height))

# Definir las variables del círculo
circle_pos = [width // 2, height // 2]
circle_radius = 50

# Crear un bucle principal
running = True
while running:
    # Manejar los eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Actualizar la posición del círculo con el movimiento del ratón
            circle_pos = list(event.pos)
    screen.fill(AZUL)
    # Dibujar el círculo en la ventana de visualización
    pygame.draw.circle(screen, (255, 255, 255), circle_pos, circle_radius)

    # Actualizar la ventana de visualización
    pygame.display.flip()

# Salir de Pygame
pygame.quit()