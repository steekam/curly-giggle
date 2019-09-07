from collections import defaultdict


class BfsTraverser:

    # Constructor
    def __init__(self):
        self.visited = []
        self.end_search = False
        self.paths = {}
        self.optimal_path = []

    def BFS(self, graph, start_node, goal_node):
        queue = []
        queue.append(start_node)
        self.visited.append(start_node)
        # ?Init root with start node
        self.paths.update({start_node: [start_node]})

        while queue and not self.end_search:
            # Dequeue a vertex from
            current_node = queue.pop(0)

            for child in list(graph[current_node]):
                if child not in self.visited:
                    if child is goal_node:
                        self.visited.append(child)
                        self.optimal_path = self.paths.get(current_node) + [child]
                        self.end_search = True
                        break
                    else:
                        queue.append(child)
                        # Add node to visited
                        self.visited.append(child)
                        # Add entry in paths
                        parentPath = self.paths.get(current_node)
                        self.paths.update({child: parentPath + [child]})

        print("==== BFS Visited Nodes: ====")
        print(self.visited, end="\n")
        print("==== BFS Optimal Path: ====")
        print(self.optimal_path, end="\n")
