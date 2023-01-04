class DisjointSet:
    def __init__(self, length):
        self.groups = list(range(length))

    def find(self, x):
        while x != self.groups[x]:
            x = self.groups[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.groups[root_x] = root_y
