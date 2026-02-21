import networkx as nx
import matplotlib.pyplot as plt

# --------------------------
# Nodes
# --------------------------

factories = ["F1", "F2"]
customers = ["C1", "C2", "C3"]

# --------------------------
# Shipment Results (from optimization output)
# --------------------------

shipments = {
    ("F1", "C1"): 50,
    ("F1", "C2"): 19,
    ("F1", "C3"): 11,
    ("F2", "C1"): 0,
    ("F2", "C2"): 51,
    ("F2", "C3"): 29,
}

# --------------------------
# Create Graph
# --------------------------

G = nx.DiGraph()

# Add nodes with positions
pos = {
    "F1": (-1, 1),
    "F2": (-1, -1),
    "C1": (1, 1),
    "C2": (1, 0),
    "C3": (1, -1),
}

G.add_nodes_from(factories)
G.add_nodes_from(customers)

# Add edges (only if shipment > 0)
for (f, c), value in shipments.items():
    if value > 0:
        G.add_edge(f, c, weight=value)

# --------------------------
# Draw Graph
# --------------------------

plt.figure()

edges = G.edges()
weights = [G[u][v]['weight'] for u, v in edges]

nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edges(G, pos, width=[w/10 for w in weights])
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={(u, v): f"{G[u][v]['weight']}" for u, v in edges}
)

plt.title("Optimized Transportation Network")
plt.show()
