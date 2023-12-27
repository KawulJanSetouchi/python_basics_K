import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(["A", "B", "C", "D"])

# Add edges with weights
G.add_edge("A", "B", weight=5)  # Edge from A to B with weight 5
G.add_edge("B", "C", weight=7)  # Edge from B to C with weight 7
G.add_edge("C", "D", weight=3)  # Edge from C to D with weight 3
G.add_edge("A", "D", weight=10) # Edge from A to D with weight 10

# Find the shortest path using Dijkstra's algorithm
shortest_path = nx.shortest_path(G, "A", "D", weight="weight")
shortest_path_length = nx.shortest_path_length(G, "A", "D", weight="weight")

print("Shortest path:", shortest_path)
print("Shortest path length:", shortest_path_length)

# Visualize the graph and shortest path
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue')
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
plt.show()