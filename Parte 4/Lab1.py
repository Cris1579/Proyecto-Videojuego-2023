import pygame
pygame.init()

NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
MARRON = (150, 70, 10)

Lab1 = [
    "XXXXXXXXX XXXXXXXXXXX",
    "X       X     X     X",
    "X XXXXX XXX X X X XXX",
    "X   X   X   X X X   X",
    "X X X XXX X XXX XXX X",
    "X X X     X X   X   X",
    "XXX XXX XXXXX XXX X X",
    "X   X   X     X X X X",
    "X XXXXXXX XXXXX X XXX",
    "X       X       X   X",
    "X XXXXX XXXXXXX XXX X",
    "X X         X   X   X",
    "X X X XXXXXXX XXX XXX",
    "X X X X       X X   X",
    "X X XXX XXXXXXX XXX X",
    "X X     X         X X",
    "X XXXXXXX XXXXXXXXX X",
    "X   X     X         X",
    "XXX XXXXX X XXXXXXX X",
    "X         X X       X",
    "XXXXXXXXXXX XXXXXXXXX",
]


def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, MARRON, rectangulo)


def dibujar_personaje(superficie, forma):
    pygame.draw.rect(superficie, AZUL, forma)
    # pygame.draw.circle(superficie, AZUL, (285,15),10, 10)
    # pygame.draw.circle(superficie, AZUL, center, radius)

def construir_mapa(mapa):
    muros = []
    x = 0
    y = 0
    for muro in mapa:
        for ladrillo in muro:
            if ladrillo == "X":
                muros.append(pygame.Rect(x, y, 30, 30))
            x += 30
        x = 0
        y += 30
    return muros


def dibujar_muros(superficie, muros):
    for m in muros:
        dibujar_muro(superficie, m)


# Ventana
ventana = pygame.display.set_mode((1280, 720))
reloj = pygame.time.Clock()

# Datos

muros = construir_mapa(Lab1)
center = (275, 15)
radius = 10
personaje = pygame.Rect(275, 10, 20, 20)
# personaje = pygame.draw.circle(ventana, AZUL,(275,10), 20, 0) # (Centro), radio)
# personaje = pygame.Rect(center[0] - radius, center[1] - radius, radius * 2, radius * 2)

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
                personaje_vel_x = 5
            if event.key == pygame.K_LEFT:
                personaje_vel_x = -5
            if event.key == pygame.K_DOWN:
                personaje_vel_y = 5
            if event.key == pygame.K_UP:
                personaje_vel_y = -5
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

    if personaje.x > 1280 - personaje.width:
        personaje.x = 1280 - personaje.width
    if personaje.x < 0:
        personaje.x = 0
    if personaje.y > 720 - personaje.height:
        personaje.y = 720 - personaje.height
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