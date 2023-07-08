import networkx as nx
import matplotlib.pyplot as plt
import random


def create_maze(n):
    # Crea un grafo de tamaño n x n
    G = nx.grid_2d_graph(n, n)

    # Conecta nodos aleatoriamente para crear el laberinto
    for (u, v) in G.edges():
        if random.random() < 0.4:  # Probabilidad de conexión
            G.remove_edge(u, v)

    return G


def draw_maze(G):
    # Dibuja el laberinto
    pos = dict((n, n) for n in G.nodes())
    nx.draw_networkx(G, pos=pos, with_labels=False, node_size=0)  #with_labels muestra la posición ej: (0,0)
    plt.axis('equal')                                               #node_size es el tamaño del nodo, es decir, del punto
    plt.xticks([])
    plt.yticks([])
    plt.show()

"""""
def solve_maze(G, start, end):
    # Resuelve el laberinto utilizando la búsqueda de caminos más cortos
    path = nx.shortest_path(G, start, end)
    return path
"""""

# Crear el laberinto
maze_size = 6
maze = create_maze(maze_size)

# Dibujar el laberinto
draw_maze(maze)
"""""
# Resolver el laberinto
start_node = (0, 0)
end_node = (maze_size - 1, maze_size - 1)
path = solve_maze(maze, start_node, end_node)

print(f"Camino desde {start_node} hasta {end_node}: {path}")
"""""