class DisjointSet:
    def __init__(self):
        self.groups = dict()

    def find(self, x):
        if x not in self.groups:
            self.groups[x] = x

        while x != self.groups[x]:
            x = self.groups[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.groups[root_x] = root_y


def has_cycle(edges):
    disjoint_set = DisjointSet()

    for src, dst in edges:
        if disjoint_set.find(src) == disjoint_set.find(dst):
            return True
        disjoint_set.union(src, dst)

    return False
