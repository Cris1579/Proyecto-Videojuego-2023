import networkx as nx
import matplotlib.pyplot as plt
import random

# Crear un grafo vacío
laberinto = nx.Graph()

# Agregar nodos al grafo
laberinto.add_nodes_from([(i, j) for i in range(5) for j in range(5)])

# Agregar aristas al grafo
for i in range(5):
    for j in range(5):
        if i < 4:
            laberinto.add_edge((i, j), (i + 1, j))  # Conexión vertical
        if j < 4:
            laberinto.add_edge((i, j), (i, j + 1))  # Conexión horizontal

# Eliminar aristas aleatoriamente para crear un laberinto
num_aristas_eliminar = random.randint(10, 20)
for _ in range(num_aristas_eliminar):
    arista = random.choice(list(laberinto.edges()))
    laberinto.remove_edge(*arista)

# Mostrar el laberinto
pos = nx.spring_layout(laberinto, seed=42)
nx.draw(laberinto, pos, with_labels=False, node_size=200, node_color="lightblue", font_size=8)
plt.title("Laberinto")
plt.axis("off")
plt.show()