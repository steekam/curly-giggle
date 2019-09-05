import networkx as nx
import matplotlib.pyplot as plt

from classes.BFS import BfsTraverser
from classes.UCS import UcsTraverser

# Create graph
G = nx.Graph()

# Add nodes
nodes = [
    "Karen", "J6", "Gitaru", "J7", "J8", "Loresho", "J9", "Lavington", "J10", "Parklands", "J11", "Kilimani", "J12", "CBD", "J13", "ImaraDaima", "Donholm", "HillView", "Kasarani", "Kahawa", "J1", "J4", "J5", "J2", "J3", "Langata"
]
G.add_nodes_from(nodes)

# Add edges
edges = [
    ("Karen", "J1", 2.8), ("J1", "J2", 6.7), ("J2", "Langata", 2.8),
    ("J2", "J3", 6.5), ("J1", "J4", 2.8), ("J4", "J5", 9.2),
    ("J5", "Kilimani", 2.5), ("J3", "J12", 6), ("J3", "J13", 7.6),
    ("Kilimani", "J12", 2.3), ("J12", "CBD", 2.5), ("CBD", "J13", 6),
    ("J13", "ImaraDaima", 8.6), ("Donholm", "HillView", 20),
    ("ImaraDaima", "Donholm", 6), ("HillView", "Kasarani", 1.7),
    ("Kasarani", "Kahawa", 11.5), ("Karen", "J6", 4),
    ("J6", "J4", 6), ("J6", "Gitaru", 10), ("J6", "J7", 6), ("Gitaru", "J7", 6),
    ("J7", "J8", 7), ("J8", "Loresho", 2), ("J8", "J9", 3), ("J9", "J10", 4),
    ("J9", "Lavington", 7), ("Lavington", "J11", 0.5), ("J10", "J11", 7),
    ("J10", "Parklands", 3), ("J11", "Kilimani", 0.5), ("J4", "J3", 10.8)
]
G.add_weighted_edges_from(edges)

# Set positions
node_positions = {
    "Karen": (0, 0), "J6": (0, 8), "J1": (4, -4), "J4": (6, -4), "J7": (0, 14), "Gitaru": (-3, 5), "J5": (8, -4),
    "J2": (5, -10), "Langata": (5, -16), "J3": (8, -10), "J8": (4, 14), "Loresho": (4, 22), "J9": (6, 14), "J10": (8, 14),
    "Parklands": (10, 22), "Lavington": (6, 6), "J11": (12, 6), "Kilimani": (10, 2), "J12": (12, 0), "CBD": (14, 0), "J13": (14, -5),
    "ImaraDaima": (16, -7), "Donholm": (16, 4), "HillView": (16, 12), "Kasarani": (16, 20), "Kahawa": (18, 28)
}


for node_key in node_positions:
    G.node[node_key]['pos'] = node_positions[node_key]

# store all positions in a variable
node_pos = nx.get_node_attributes(G, 'pos')
arc_weight = nx.get_edge_attributes(G, 'weight')

# call BFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
print("===================================", end="\n")
print("====== BFS Traversal ========", end="\n")
print("===================================", end="\n")
route_bfs.BFS(G, "Karen", "ImaraDaima")
route_list_bfs = route_bfs.visited
print("====== BFS Traversal Route list ========", end="\n")
print(route_list_bfs, end="\n")

plt.figure("BFS Traversal")
plt.axis('off')
# color the nodes in the route_bfs
node_col_bfs = [
    'darkturquoise' if node not in route_list_bfs else 'peru' for node in G.nodes()
]

# Generating edges in visited nodes
all_combi = [(i, j) for i in route_list_bfs for j in route_list_bfs[1:]]
peru_colored_edges_bfs = list(inter for inter in all_combi if inter in G.edges())


# color the edges as well
edge_col_bfs = [
    'darkturquoise' if edge not in peru_colored_edges_bfs else 'peru' for edge in G.edges()
]
nx.draw_networkx(G, node_pos, node_color=node_col_bfs, node_size=400)
nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col_bfs)
nx.draw_networkx_edge_labels(
    G, node_pos, edge_color=edge_col_bfs, edge_labels=arc_weight)


route_ucs = UcsTraverser()
print("===================================", end="\n")
print("====== UCS Traversal ========", end="\n")
print("===================================", end="\n")
route_ucs.ucs(G, "Karen", "ImaraDaima")
route_list_ucs = route_ucs.visited
print("====== UCS Traversal Route list ========", end="\n")
print(route_list_ucs, end="\n")

plt.figure("UCS Traversal")
plt.axis('off')
# color the nodes in the route_bfs
node_col_ucs = [
    'darkturquoise' if node not in route_list_ucs else 'peru' for node in G.nodes()
]

# Generating edges in visited nodes
all_combi_ucs = [(i, j) for i in route_list_ucs for j in route_list_ucs[1:]]
peru_colored_edges_ucs = list(inter for inter in all_combi_ucs if inter in G.edges())

# color the edges as well
edge_col_ucs = [
    'darkturquoise' if edge not in peru_colored_edges_ucs else 'peru' for edge in G.edges()
]
nx.draw_networkx(G, node_pos, node_color=node_col_ucs, node_size=400)
nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col_ucs)
nx.draw_networkx_edge_labels(
    G, node_pos, edge_color=edge_col_ucs, edge_labels=arc_weight)
plt.show()
