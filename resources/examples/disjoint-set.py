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


def has_cycle(graph):
    n_vertices = len(graph)
    disjoint_set = DisjointSet()

    for i in range(n_vertices):
        for j in range(n_vertices):
            if i == j or graph[i][j] == float("inf"):
                continue

            if disjoint_set.find(i) == disjoint_set.find(j):
                return True

            disjoint_set.union(i, j)

    return False
