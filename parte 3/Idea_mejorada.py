#TOMANDO LA IDEA 1, REALIZARLO PARA UN LABERINTO SIMPLE
#CÓDIGO EXTRAÍDO DE VIDEO TUTORIAL
import pygame

# Inicializar
pygame.init()

# Medidas
ANCHO = 1280
ALTO = 720

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
MARRON = (150, 70, 10)

# Mapas

mapa = [
    "XXXXXXXXXXXXXXXX",
    "X              X",
    "X XXXXXX XXXXX X",
    "X X            X",
    "X XXXX XXXXXXX X",
    "X X    X       X",
    "X XX XXXXX XXX X",
    "X              X",
    "XXXXXXXXXXXXXXXX"
]


# Funciones

def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, MARRON, rectangulo)


def dibujar_personaje(superficie, rectangulo):
    pygame.draw.rect(superficie, AZUL, rectangulo)


def construir_mapa(mapa):
    muros = []
    x = 0
    y = 0
    for muro in mapa:
        for ladrillo in muro:
            if ladrillo == "X":
                muros.append(pygame.Rect(x, y, 80, 80))
            x += 80
        x = 0
        y += 80
    return muros


def dibujar_muros(superficie, muros):
    for m in muros:
        dibujar_muro(superficie, m)


# Ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Datos

muros = construir_mapa(mapa)

personaje = pygame.Rect(100, 400, 40, 40)
personaje_vel_x = 0
personaje_vel_y = 0

# Bucle principal
jugando = True
while jugando:

    reloj.tick(60)

    # Eventos de movimiento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
            if event.key == pygame.K_RIGHT:
                personaje_vel_x = 10
            if event.key == pygame.K_LEFT:
                personaje_vel_x = -10
            if event.key == pygame.K_DOWN:
                personaje_vel_y = 10
            if event.key == pygame.K_UP:
                personaje_vel_y = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                personaje_vel_x = 0
            if event.key == pygame.K_LEFT:
                personaje_vel_x = 0
            if event.key == pygame.K_DOWN:
                personaje_vel_y = 0
            if event.key == pygame.K_UP:
                personaje_vel_y = 0

                # Lógica

    personaje.x += personaje_vel_x
    personaje.y += personaje_vel_y

    #Colisión

    if personaje.x > ANCHO - personaje.width:
        personaje.x = ANCHO - personaje.width
    if personaje.x < 0:
        personaje.x = 0
    if personaje.y > ALTO - personaje.height:
        personaje.y = ALTO - personaje.height
    if personaje.y < 0:
        personaje.y = 0

    for muro in muros:
        if personaje.colliderect(muro):
            personaje.x -= personaje_vel_x
            personaje.y -= personaje_vel_y

    # Dibujos

    ventana.fill(NEGRO)

    dibujar_muros(ventana, muros)

    dibujar_personaje(ventana, personaje)

    # Actualizar
    pygame.display.update()

# Salir
pygame.quit()