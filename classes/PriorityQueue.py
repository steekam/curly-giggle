
class PriorityQueue:
    def __init__(self):
        self.queue = []

    # ?Item structure (cost, data)
    def push(self, item):
        self.queue.append(item)
        self.queue.sort(key=self.get_key)

    # ?When queue is sorted, item with highest priority (least cost) is returned
    def pop(self):
        # ?check if empty
        if not self.queue:
            return False
        # self.queue.sort(key=self.get_key)

        # ?Pop first element
        return self.queue.pop(0)

    # ?Pop specific item from queue
    def remove_item(self, item):
        # ?check if empty
        if not self.queue:
            return False

        self.queue.remove(item)
        self.queue.sort(key=self.get_key)

    # ?Push item, but if item with higher cost exists, replace
    def replace_if_higher_exists(self, item):
        cost, node = item
        existing_item = [_node for _node in self.queue if _node[1] == node][0]

        if existing_item[0] > cost:
            self.remove_item(existing_item[0])
            self.push(item)

    # ?Specifies the key to be used to sort tuple
    def get_key(self, item):
        return item[0]
