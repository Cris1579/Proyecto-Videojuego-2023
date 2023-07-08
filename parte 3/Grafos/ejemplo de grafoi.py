import networkx as nx

# Crear un grafo
grafo = nx.DiGraph()

# Agregar nodos
grafo.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Agregar aristas
grafo.add_edge('A', 'B')
grafo.add_edge('B', 'C')
grafo.add_edge('C', 'D')
grafo.add_edge('D', 'E')
grafo.add_edge('E', 'A')

# Obtener información del grafo
print("Número de nodos:", grafo.number_of_nodes())
print("Número de aristas:", grafo.number_of_edges())
print("Nodos del grafo:", grafo.nodes())
print("Aristas del grafo:", grafo.edges())