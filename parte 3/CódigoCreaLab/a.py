
import sys
from b import *


# =====================================================================================
# ---                Codigo Principal ( M A I N ) | clase Game                      ---
# -------------------------------------------------------------------------------------
class Game:
    def __init__(self):
        pygame.init()
        self.fondoCOLOR = (90, 90, 90)
        self.paredCOLOR = (45, 45, 45)
        self.verdeCURSOR = (20, 80, 220)
        self.verdeVISITADA = (64, 170, 16)
        self.azulClaroCamino = (16, 170, 252)
        self.amarillo = (204, 238, 0)
        self.rojoSprite = (238, 48, 16)

        self.TX = 35  # Tamaño de los TILES (por defecto)
        self.TY = 35

        self.RESOLUCION = (500, 500)
        self.FPS = 60

        self.stack = []
        self.casillas = []

        self.programaEjecutandose = True
        self.comenzar = False
        self.terminado = False

        self.pantalla = pygame.display.set_mode(self.RESOLUCION)
        self.reloj = pygame.time.Clock()

    def crearArrayObjetosCasilla(self):
        for i in range(self.FILAS):
            for ii in range(self.COLUMNAS):
                casilla = Casilla(self, ii, i, self.TX, self.TY)
                self.casillas.append(casilla)

    def inicializaParaArrancar(self):
        self.actual = self.casillas[0]  # actual = la 1ra casilla (para arrancar)
        self.actual.visitada = True  # La metemos como 'visitada'
        self.stack.append(self.actual)  # Importante, para que el array Stack NO este vacio

    def comenzarAlgoritmo(self, tiles):
        print('tecla Pulsada')
        if not self.comenzar:
            self.comenzar = True
            self.TX = tiles
            self.TY = tiles
            self.FILAS = int(self.RESOLUCION[1] / self.TY)
            self.COLUMNAS = int(self.RESOLUCION[0] / self.TX)
            self.crearArrayObjetosCasilla()
            self.inicializaParaArrancar()

    def abrirCamino(self, actual, elegida):
        lr = actual.x - elegida.x

        if lr == -1:
            actual.walls[1] = False
            elegida.walls[3] = False

        elif lr == 1:
            actual.walls[3] = False
            elegida.walls[1] = False

        tb = actual.y - elegida.y

        if tb == -1:
            actual.walls[2] = False
            elegida.walls[0] = False

        elif tb == 1:
            actual.walls[0] = False
            elegida.walls[2] = False

    def reiniciarPrograma(self):
        self.stack.clear()
        self.casillas.clear()
        self.terminado = False

        self.crearArrayObjetosCasilla()
        self.inicializaParaArrancar()

    def dibuja_texto(self, surface, texto, size, x, y, qcolor):
        font = pygame.font.SysFont('serif', size)
        text_surface = font.render(texto, True, qcolor)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def mostrar_textos(self):

        centroX = int(self.RESOLUCION[0] / 2)
        centroY = int(self.RESOLUCION[1] / 2)

        if self.terminado:
            self.dibuja_texto(self.pantalla, ' Laberinto Creado! Pulse espacio para generar otro... ',
                              int(self.RESOLUCION[0] / 25), centroX, centroY, self.amarillo)

        if not self.comenzar:
            self.dibuja_texto(self.pantalla, ' 1. Pequeño    ',
                              int(self.RESOLUCION[0] / 20), centroX, centroY - 200, self.amarillo)

            self.dibuja_texto(self.pantalla, ' 2. Mediano    ',
                              int(self.RESOLUCION[0] / 20), centroX, centroY - 100, self.amarillo)

            self.dibuja_texto(self.pantalla, ' 3. Grande     ',
                              int(self.RESOLUCION[0] / 20), centroX, centroY, self.amarillo)

            self.dibuja_texto(self.pantalla, ' 4. Enorme     ',
                              int(self.RESOLUCION[0] / 20), centroX, centroY + 100, self.amarillo)

            self.dibuja_texto(self.pantalla, ' Seleccione tamaño Laberinto... ',
                              int(self.RESOLUCION[0] / 20), centroX, centroY + 250, self.amarillo)

    def dibujaLaberinto(self):
        for i in range(len(self.casillas)):
            self.casillas[i].render()

    def LaberintoGenerandose(self):
        if len(self.stack) > 0:

            self.dibujaLaberinto()

            self.actual = self.stack.pop()
            elegida = self.actual.check_vecinos()

            if elegida:
                elegida.cursor()
                self.stack.append(self.actual)
                self.abrirCamino(self.actual, elegida)
                elegida.visitada = True
                self.stack.append(elegida)
                print(self.stack[0].x, self.stack[1].x)

            else:
                self.actual.cursor()

        else:
            self.dibujaLaberinto()
            self.terminado = True

    def update(self):
        pygame.display.set_caption(str(int(self.reloj.get_fps())))
        self.pantalla.fill(self.fondoCOLOR)

        if self.comenzar:
            self.LaberintoGenerandose()

        self.mostrar_textos()

        pygame.display.flip()
        self.reloj.tick(self.FPS)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_1]:
            tiles = 140
            self.comenzarAlgoritmo(tiles)
        elif tecla[pygame.K_2]:
            tiles = 70
            self.comenzarAlgoritmo(tiles)
        elif tecla[pygame.K_3]:
            tiles = 35
            self.comenzarAlgoritmo(tiles)
        elif tecla[pygame.K_4]:
            tiles = 14
            self.comenzarAlgoritmo(tiles)

        if tecla[pygame.K_SPACE]:
            if self.comenzar:
                self.reiniciarPrograma()

        if tecla[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def run(self):
        while self.programaEjecutandose:
            self.check_event()
            self.update()


if __name__ == '__main__':
    game = Game()
    game.run()