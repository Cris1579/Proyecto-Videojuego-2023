import pygame,sys
from random import choice, randrange

size = ANCHO, ALTO = 800, 762
TILE = 100
cols, rows = ANCHO // TILE, ALTO // TILE

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class Cell: #Creamos una clase casilla
    def __init__(self,x,y):
        self.x, self.y = x, y
        self.walls = {'top': True,'right': True,'bottom': True,'left': True}
        self.visited = False

    def draw_current_cell(self): #Cuadrado que recorre el mapa
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(screen,pygame.Color('saddlebrown'),(x+2,y+2,TILE - 2, TILE - 2))

    def draw(self): #Con esto pinta el recorrido que hace
        x,y = self.x * TILE, self.y * TILE

        if self.visited:
            pygame.draw.rect(screen,pygame.Color('black'),(x,y,TILE,TILE)) #Dejando en negro cuando pase
        #Las paredes se hacen verde
        if self.walls['top']:
            pygame.draw.line(screen,pygame.Color('green'),(x,y),(x + TILE,y), 2)
        if self.walls['right']:
            pygame.draw.line(screen,pygame.Color('green'),(x + TILE,y),(x + TILE,y + TILE),2)
        if self.walls['bottom']:
            pygame.draw.line(screen,pygame.Color('green'),(x + TILE, y + TILE), (x , y + TILE), 2)
        if self.walls['left']:
            pygame.draw.line(screen,pygame.Color('green'),(x, y + TILE),(x, y),2)

    def check_cell(self,x,y):   #Con esto, le decimos al programa que no se salga de los limites
        find_index = lambda x ,y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x,y)]
    def check_neighbors(self,): #Revisa los 'vecinos' de la casilla en que esté
        neighbors = []
        top = self.check_cell(self.x,self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False

def remove_walls(current, next): # 'Rompe' las paredes
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False


grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)] #Aqui ponemos cada cosa en una lista
current_cell = grid_cells[0] #Celda o casilla inicial
array = []

while True:
    screen.fill(pygame.Color('darkslategray'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    [cell.draw() for cell in grid_cells] #Con esto, se dibuja el mapa
    current_cell.visited = True
    current_cell.draw_current_cell()
    #Ciclo que permite al algoritmo recorrer todo el mapa
    next_cell = current_cell.check_neighbors()
    if next_cell:
        next_cell.visited = True
        remove_walls(current_cell,next_cell)

        array.append(current_cell)
        current_cell = next_cell
    elif array:
        current_cell = array.pop()


    pygame.display.flip()
    clock.tick(30)