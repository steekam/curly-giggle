import networkx as nx
import matplotlib.pyplot as plt

from classes.BFS import BfsTraverser
from classes.UCS import UcsTraverser
from classes.Astar import Astar
from classes.GreedyBFS import GreedyBFS


# Init graph with data
def init_graph():
    # Create graph
    G = nx.Graph()

    # Add nodes
    nodes = [
        "Karen", "J6", "Gitaru", "J7", "J8", "Loresho", "J9", "Lavington", "J10", "Parklands", "J11", "Kilimani", "J12", "CBD", "J13", "ImaraDaima", "Donholm", "HillView", "Kasarani", "Kahawa", "J1", "J4", "J5", "J2", "J3", "Langata"
    ]
    G.add_nodes_from(nodes)

    # Add edges
    edges = [
        ("Karen", "J1", 2.8), ("J1", "J2", 6), ("J2", "Langata", 2.6),
        ("J2", "J3", 5.4), ("J1", "J4", 2.6), ("J4", "J5", 9.7),
        ("J5", "Kilimani", 0.5), ("J3", "J12", 6.7), ("J3", "J13", 6.2),
        ("Kilimani", "J12", 2.3), ("J12", "CBD", 1.5), ("CBD", "J13", 5.5),
        ("J13", "ImaraDaima", 3.9), ("Donholm", "HillView", 20),
        ("ImaraDaima", "Donholm", 10.4), ("HillView", "Kasarani", 1.7),
        ("Kasarani", "Kahawa", 11.5), ("Karen", "J6", 4),
        ("J6", "J4", 6), ("J6", "Gitaru", 10), ("J6", "J7", 6), ("Gitaru", "J7", 6),
        ("J7", "J8", 7), ("J8", "Loresho", 2), ("J8", "J9", 3), ("J9", "J10", 4),
        ("J9", "Lavington", 7), ("Lavington", "J11", 0.5), ("J10", "J11", 7),
        ("J10", "Parklands", 3), ("J11", "Kilimani", 0.5), ("J4", "J3", 9)
    ]
    G.add_weighted_edges_from(edges)

    # Set positions
    node_positions = {
        "Karen": (0, 0), "J6": (0, 8), "J1": (4, -4), "J4": (6, -4), "J7": (0, 14), "Gitaru": (-3, 5), "J5": (8, -4),
        "J2": (5, -10), "Langata": (5, -18), "J3": (8, -10), "J8": (4, 14), "Loresho": (4, 22), "J9": (6, 14), "J10": (8, 14),
        "Parklands": (10, 22), "Lavington": (6, 6), "J11": (12, 6), "Kilimani": (10, 2), "J12": (12, 0), "CBD": (14, 0), "J13": (14, -8),
        "ImaraDaima": (16, -10), "Donholm": (16, 4), "HillView": (16, 12), "Kasarani": (16, 20), "Kahawa": (18, 28)
    }

    for node_key in node_positions:
        G.node[node_key]['pos'] = node_positions[node_key]

    # Set heuristics
    heuristics = {
        "Karen": 21.22, "Gitaru": 25, "Loresho": 16, "Lavington": 12, "Parklands": 10,
        "Kilimani": 11, "Langata": 15, "CBD": 8, "Donholm": 4, "HillView": 12, "Kasarani": 11,
        "Kahawa": 16, "ImaraDaima": 0, "J1": 19, "J2": 14.5, "J3": 10, "J4": 17, "J5": 12,
        "J6": 22, "J7": 24, "J8": 17, "J9": 14, "J10": 9, "J11": 11.7, "J12": 9, "J13": 4
    }

    for node_key in heuristics:
        G.node[node_key]['heuristics'] = heuristics[node_key]

    return G


# utility function to draw and color graph figure
def draw_colored_graph(graph, visited_nodes, figure_title):
    node_positions = nx.get_node_attributes(graph, 'pos')
    arc_weights = nx.get_edge_attributes(graph, 'weight')

    plt.figure(figure_title)
    plt.axis('off')
    # color the nodes in the route_bfs
    node_colors = [
        'darkturquoise' if node not in visited_nodes else 'peru' for node in graph.nodes()
    ]

    # Generating edges in visited nodes
    all_combinations = [(i, j)
                        for i in visited_nodes for j in visited_nodes[1:]]
    peru_colored_edges = list(
        inter for inter in all_combinations if inter in graph.edges())

    # color the edges as well
    edge_colors = [
        'darkturquoise' if edge not in peru_colored_edges else 'peru' for edge in graph.edges()
    ]
    nx.draw_networkx(graph, node_positions,
                     node_color=node_colors, node_size=400)
    nx.draw_networkx_edges(graph, node_positions,
                           width=2, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(
        graph, node_positions, edge_color=edge_colors, edge_labels=arc_weights)


if __name__ == '__main__':
    graph = init_graph()

    # Breadth First Search
    # bfsTraverser = BfsTraverser()
    # bfsTraverser.BFS(graph, "Karen", "ImaraDaima")
    # draw_colored_graph(graph, bfsTraverser.visited, "BFS Visited Nodes")

    # # Uniform Cost Search
    # ucsTraverser = UcsTraverser()
    # ucsTraverser.UCS(graph, "Karen", "ImaraDaima")
    # draw_colored_graph(graph, ucsTraverser.visited, "UCS Visited Nodes")
    # draw_colored_graph(graph, ucsTraverser.least_cost_path, "UCS Optimal Path")

    # # A* search
    # astar = Astar()
    # astar.traverser(graph, "Karen", "ImaraDaima")
    # visited_nodes = list(astar.explored.keys())
    # draw_colored_graph(graph, visited_nodes, "Astar Visited Nodes")
    # draw_colored_graph(graph, astar.path, "Astar Optimal Path")

    # GreedyBFS
    greedybfs = GreedyBFS()
    greedybfs.traverser(graph, "Karen", "ImaraDaima")
    visited_nodes = list(greedybfs.visited.keys())
    # draw_colored_graph(graph, visited_nodes, "GreedyBFS Visited Nodes")
    # draw_colored_graph(graph, greedybfs.path, "GreedyBFS Optimal Path")

    # plt.show()
