

import pygame, sys
from button import Button
from MazeGeneratorDFS import *
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game 1.0")

BG = pygame.image.load("Background.png")


def get_font(size):  # Tamaño de la fuente de la letra a utilizar
    return pygame.font.Font("font.ttf", size)



def lvlSelection():  # Pantalla de juego
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black") #Si quitas esto, se sobrepone el otro texto

        PLAY_TEXT = get_font(45).render("Selecciona un nivel.", True, "White") #Prueba cambiando el n° de "get_font"
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 180)) #Posición del texto
        SCREEN.blit(PLAY_TEXT, PLAY_RECT) #Revisa "Fondo(6).py" si no recuerdas que hace '.blit'

        #Aquí se crea el botón agregandole una posible imagen, su posicion inicial, que texto contiene, tamaño fuente
        #Color inicial y el color al sobreponer el puntero


        lvlOne = Button(image=None, pos=(640, 300),
                           text_input="Nivel 1", font=get_font(40), base_color="Blue", hovering_color="Green")
        lvlOne.changeColor(PLAY_MOUSE_POS)  # Cambia el color al colocar el puntero sobre el botón
        lvlOne.update(SCREEN)  # Actualiza la pantalla


        lvlTwo = Button(image=None, pos=(640, 380),
                           text_input="Nivel 2", font=get_font(40), base_color="Blue", hovering_color="Green")
        lvlTwo.changeColor(PLAY_MOUSE_POS)  # Cambia el color al colocar el puntero sobre el botón
        lvlTwo.update(SCREEN)  # Actualiza la pantalla


        lvlThree = Button(image=None, pos=(640, 460),
                           text_input="Nivel 3", font=get_font(40), base_color="Blue", hovering_color="Green")
        lvlThree.changeColor(PLAY_MOUSE_POS)  # Cambia el color al colocar el puntero sobre el botón
        lvlThree.update(SCREEN)  # Actualiza la pantalla


        PLAY_BACK = Button(image=None, pos=(640, 600),
                           text_input="Volver", font=get_font(55), base_color=(61,3,39), hovering_color="Purple")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS) #Cambia el color al colocar el puntero sobre el botón
        PLAY_BACK.update(SCREEN) #Actualiza la pantalla

        for event in pygame.event.get():  #Loop principal ya conocido
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvlOne.checkForInput(PLAY_MOUSE_POS):
                    LabOne()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvlTwo.checkForInput(PLAY_MOUSE_POS):
                    LabTwo()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvlThree.checkForInput(PLAY_MOUSE_POS):
                    print("wena 3") # aca ejecutar el nivel como lvl3()

        pygame.display.update()

def LabOne():

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
        "XXXXXXXXXXXFXXXXXXXXX",
    ]

    def dibujar_muro(superficie, rectangulo):
        pygame.draw.rect(superficie, MARRON, rectangulo)

    def dibujar_personaje(superficie, forma):
        pygame.draw.rect(superficie, AZUL, forma)

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
    personaje = pygame.Rect(275, 10, 20, 20)


    personaje_vel_x = 0
    personaje_vel_y = 0

    # Bucle principal
    Fin = False
    while True:

        reloj.tick(60)

        # VOLVER


        # Eventos de movimiento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                # sys.exit()
                main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK1.checkForInput(PLAY_MOUSE_POS):
                    lvlSelection()

            if event.type == pygame.KEYDOWN:
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

        # Colisión

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

        # if pygame.Rect(personaje_vel_x, personaje_vel_y, player_size, player_size).colliderect(
        #         pygame.Rect(target_x, target_y, target_size, target_size)):
        #     target_x, target_y = screen_width / 2 - target_size / 2, screen_height / 2 - target_size / 2
        #     Fin = True

        # Dibujos

        ventana.fill(NEGRO)

        dibujar_muros(ventana, muros)

        dibujar_personaje(ventana, personaje)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK1 = Button(image=None, pos=(1040, 600),
                            text_input="Volver", font=get_font(55), base_color=(61, 3, 39),
                            hovering_color="Purple")
        PLAY_BACK1.changeColor(PLAY_MOUSE_POS)  # Cambia el color al colocar el puntero sobre el botón
        PLAY_BACK1.update(SCREEN)  # Actualiza la pantalla

        if Fin:
            finText = get_font(45).render("Felicitaciones", True, "White")
            finTextRect = finText.get_rect(center=(640, 180))
            SCREEN.blit(finText, finTextRect)


        # Actualizar
        pygame.display.update()
def LabTwo():
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

    # Fondo
    bg_game = pygame.image.load('bg_1.jpg').convert()
    bg = pygame.image.load('bg_main.jpg').convert()

    # Consiguiendo el laberinto
    laberinto = genera_Lab()

    # Personaje

    player_speed = 5
    player_img = pygame.image.load('gato.jpg').convert_alpha()
    player_img = pygame.transform.scale(player_img,
                                        (TILE - 2 * laberinto[0].thickness, TILE - 2 * laberinto[0].thickness))
    player_rect = player_img.get_rect()
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_a, 'd': pygame.K_d, 'w': pygame.K_w, 's': pygame.K_s}
    direction = (0, 0)

    # Lista de la colisión
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

        # Dibujando el laberinto
        [cell.draw(game_surface) for cell in laberinto]
        # Dibujando al personaje
        game_surface.blit(player_img, player_rect)

        # Actualizar
        pygame.display.flip()
        reloj.tick(FPS)



def options(): #Pantalla de opciones
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu(): #Pantalla del Menú
    while True:
        SCREEN.blit(BG, (0, 0))  #Poner el fondo

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    lvlSelection()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()