import pygame
from MazeGeneratorDFS import *
def is_collide(x, y):
    tmp_rect = player_rect.move(x, y)
    if tmp_rect.collidelist(colision_muros_lista) == -1:
        return False
    return True
# Datos
FPS = 60
pygame.init()
game_surface = pygame.Surface(size)
ventana = pygame.display.set_mode((ANCHO + 300, ALTO))
reloj = pygame.time.Clock()




#Fondo
bg_game = pygame.image.load('../bg_1.jpg').convert()
bg = pygame.image.load('../bg_main.jpg').convert()

#Consiguiendo el laberinto
laberinto = genera_Lab()

#Personaje

player_speed = 5
player_img = pygame.image.load('../gato.jpg').convert_alpha()
player_img = pygame.transform.scale(player_img, (TILE - 2 * laberinto[0].thickness, TILE - 2 * laberinto[0].thickness))
player_rect = player_img.get_rect()
player_rect.center = TILE // 2, TILE // 2
directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
keys = {'a': pygame.K_a, 'd': pygame.K_d, 'w': pygame.K_w, 's': pygame.K_s}
direction = (0, 0)

#Lista de la colisión
colision_muros_lista = sum([cell.get_rects() for cell in laberinto], [])

# Bucle principal

while True:
    ventana.blit(bg, (ANCHO, 0))
    ventana.blit(game_surface, (0, 0))
    game_surface.blit(bg_game, (0, 0))
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # Controles
    pressed_key = pygame.key.get_pressed()
    for key, key_value in keys.items():
        if pressed_key[key_value] and not is_collide(*directions[key]):
            direction = directions[key]
            break
    if not is_collide(*direction):
        player_rect.move_ip(direction)

    # --------Dibujos-----------

    #Dibujando el laberinto
    [cell.draw(game_surface) for cell in laberinto]
    #Dibujando al personaje
    game_surface.blit(player_img, player_rect)

    # Actualizar
    pygame.display.flip()
    reloj.tick(FPS)
