from classes.PriorityQueue import PriorityQueue


class UcsTraverser:
    # Constructor
    def __init__(self):
        self.visited = []
        self.paths = {}
        self.least_cost_path = []
        self.least_cost = 0

    def UCS(self, graph, start_node, goal_node):
        queue = PriorityQueue()
        # Init with start node and cost of zero
        queue.push((0, start_node))
        # ?Init path root
        self.paths.update({(0, start_node): [start_node]})

        iteration = 1
        while queue.queue:
            # print("Priority queue Iteration ",
            #       iteration, [{tuple[1]: tuple[0]} for tuple in queue.queue], end="\n")
            # iteration += 1

            cost, current_node = queue.pop()
            if current_node == goal_node:
                self.visited.append(current_node)
                self.least_cost = cost
                self.least_cost_path = self.paths.get((cost, current_node))
                break

            if current_node not in self.visited:
                self.visited.append(current_node)

            # print("Current node => ", current_node, end="\n")
            for child in list(graph[current_node]):
                # print("Child => ", child, " Visited list: ",
                #       self.visited, end="\n")
                # ?Calculate total cost up to current child
                total_cost = round(
                    cost + graph[current_node][child]['weight'], 1)

                if child not in self.visited and child not in [tuple[1] for tuple in queue.queue]:
                    queue.push((total_cost, child))
                elif child in [tuple[1] for tuple in queue.queue]:
                    queue.replace_if_higher_exists((total_cost, child))

                # ?Add value to paths
                parentPath = self.paths.get((cost, current_node))
                self.paths.update(
                    {(total_cost, child): parentPath + [child]})

        print("==== UCS Visited Nodes: ====")
        print(self.visited, end="\n")
        print("==== UCS Least Cost Path: (", self.least_cost, ") ====")
        print(self.least_cost_path, end="\n")
