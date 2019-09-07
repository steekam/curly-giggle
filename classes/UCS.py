from queue import PriorityQueue


class UcsTraverser:
    # Constructor
    def __init__(self):
        self.visited = []
        self.paths = {}
        self.least_cost_path = []

    def UCS(self, graph, start_node, goal_node):
        queue = PriorityQueue()
        # Init with start node and cost of zero
        queue.put((0, start_node))
        # ?Init path root
        self.paths.update({(0, start_node): [start_node]})

        while queue:
            cost, current_node = queue.get()
            if current_node == goal_node:
                self.visited.append(current_node)
                self.least_cost_path = self.paths.get((cost, current_node))
                break

            if current_node not in self.visited:
                self.visited.append(current_node)

            for child in list(graph[current_node]):
                if child not in self.visited:
                    total_cost = round(
                        cost + graph[current_node][child]['weight'], 1)
                    queue.put((total_cost, child))
                    # ?Add value to paths
                    parentPath = self.paths.get((cost, current_node))
                    self.paths.update(
                        {(total_cost, child): parentPath + [child]})

        print("==== UCS Visited Nodes: ====")
        print(self.visited, end="\n")
        print("==== UCS Least Cost Path: ====")
        print(self.least_cost_path, end="\n")
