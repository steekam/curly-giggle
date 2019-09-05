from queue import PriorityQueue


class UcsTraverser:
    # Constructor
    def __init__(self):
        self.visited = []

    def ucs(self, graph, start_node, goal_node):
        queue = PriorityQueue()
        # Init with start node and cost of zero
        queue.put((0, start_node))

        while queue:
            cost, current_node = queue.get()
            print("Drive to ", current_node,
                  "with cumulative cost => ", cost, end="\n")
            if current_node not in self.visited:
                self.visited.append(current_node)

            if current_node == goal_node:
                return

            for child in list(graph[current_node]):
                if child not in self.visited:
                    total_cost = cost + graph[current_node][child]['weight']
                    queue.put((total_cost, child))
