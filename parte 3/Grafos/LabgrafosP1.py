import networkx as nx
import matplotlib.pyplot as plt
import random

# Crear el laberinto
laberinto = nx.Graph()
laberinto.add_nodes_from([(i, j) for i in range(5) for j in range(5)])
for i in range(5):
    for j in range(5):
        if i < 4:
            laberinto.add_edge((i, j), (i + 1, j))
        if j < 4:
            laberinto.add_edge((i, j), (i, j + 1))

# Eliminar aristas aleatoriamente para crear un laberinto
num_aristas_eliminar = random.randint(10, 20)
for _ in range(num_aristas_eliminar):
    arista = random.choice(list(laberinto.edges()))
    laberinto.remove_edge(*arista)

# Función para mostrar el laberinto
def mostrar_laberinto(pos_jugador=None):
    plt.clf()
    pos = nx.spring_layout(laberinto, seed=42)
    nx.draw(laberinto, pos, with_labels=False, node_size=200, node_color="lightblue", font_size=8)

    if pos_jugador:
        nx.draw_networkx_nodes(laberinto, pos, nodelist=[pos_jugador], node_color="red", node_size=200)

    plt.title("Laberinto")
    plt.axis("off")
    plt.show()

# Inicializar posición del jugador
posicion_player = (0, 0)
mostrar_laberinto(posicion_player)

# Función para mover al jugador
def mover_jugador(direccion,posicion_player):
    x, y = posicion_player
    if direccion == "arriba" and (x, y) in laberinto.neighbors((x - 1, y)):
        posicion_player = (x - 1, y)
    elif direccion == "abajo" and (x, y) in laberinto.neighbors((x + 1, y)):
        posicion_player = (x + 1, y)
    elif direccion == "izquierda" and (x, y) in laberinto.neighbors((x, y - 1)):
        posicion_player = (x, y - 1)
    elif direccion == "derecha" and (x, y) in laberinto.neighbors((x, y + 1)):
        posicion_player = (x, y + 1)
    else:
        print("Movimiento inválido. Inténtalo nuevamente.")
        return

    mostrar_laberinto(posicion_player)

# Juego principal
while True:
    direccion = input("Ingresa la dirección de movimiento (arriba/abajo/izquierda/derecha): ")
    mover_jugador(direccion)

    if posicion_player == (4, 4):
        print("¡Has encontrado la salida! ¡Ganaste!")
        break