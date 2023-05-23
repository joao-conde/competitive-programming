class QueueManager:

    def __init__(self):
        self.id = 0
        self.queue = BST()
        self.groups = dict()

    def arrive(self, n):
        node = self.queue.append((n, self.id))
        self.groups[self.id] = node
        self.id += 1

    def leave(self, id):
        group = self.groups.get(id, None)
        if not group:
            return
        
        self.groups.pop(id)
        self.queue.remove(group)

    def find(self, n):
        group = self.queue.find_value(n, self._bst_comparator)
        self.queue.remove(group)
        return group
    
    def _bst_comparator(self, n1, n2):
        (size1, id1) = n1
        (size2, id2) = n2

        if size1 == size2:
            return id1 < id2
        
        return size1 > size2