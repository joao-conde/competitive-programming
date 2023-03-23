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


def kruskal(edges):
    edges.sort()

    mst = []
    disjoint_set = DisjointSet()

    for cost, src, dst in edges:
        root_src = disjoint_set.find(src)
        root_dst = disjoint_set.find(dst)

        if root_src != root_dst:
            disjoint_set.union(root_src, root_dst)
            mst.append((cost, src, dst))

    return mst


# Tests
# https://www.freecodecamp.org/news/content/images/2020/06/image-76.png

# tuples (cost, src, dst)
graph = [
    (2, 0, 1),
    (6, 0, 2),
    (5, 1, 3),
    (8, 2, 3),
    (10, 3, 4),
    (15, 3, 5),
    (6, 4, 5),
    (2, 4, 6),
    (6, 5, 6),
]
assert kruskal(graph) == [
    (2, 0, 1),
    (2, 4, 6),
    (5, 1, 3),
    (6, 0, 2),
    (6, 4, 5),
    (10, 3, 4),
]
