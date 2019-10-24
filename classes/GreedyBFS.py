from heapq import heappop as pop, heappush as push


class GreedyBFS:

    def __init__(self):
        self.visited = {}
        self.path = []

    def traverser(self, graph, source, dest):
        queue = []
        start_heuristic = graph.node[source]['heuristics']
        push(queue, (start_heuristic, {
             'node': source, 'cost': 0, 'parent': None}))

        while queue:
            current_node, cost, parent = list(pop(queue)[1].values())

            # goal check
            if (current_node == dest):
                self.visited[current_node] = parent
                self.path = [current_node]
                node = parent
                while node is not None:
                    self.path.append(node)
                    node = self.visited[node]
                self.path.reverse()
                break

            if (current_node not in list(self.visited.keys())):
                self.visited[current_node] = parent

            # Check neighbors
            for neighbor, data in graph[current_node].items():
                nheuristic = graph.node[neighbor]['heuristics']
                ncost = cost + data['weight']

                # Create list of nodes in queue
                queuenodes = [tuple[1]['node'] for tuple in queue]
                if (neighbor not in list(self.visited.keys()) and neighbor not in queuenodes):
                    push(queue, (nheuristic, {
                        'node': neighbor, 'cost': ncost, 'parent': current_node}))
