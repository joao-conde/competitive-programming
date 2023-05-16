class DisjointSet:
    def __init__(self):
        self.groups = dict()
        self.sizes = dict()

    def find(self, x):
        if x not in self.groups:
            self.groups[x] = x
            self.sizes[x] = 1

        while x != self.groups[x]:
            x = self.groups[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        small = x if self.sizes[x] < self.sizes[y] else y
        large = y if self.sizes[x] < self.sizes[y] else x
        self.groups[small] = large
        self.sizes[large] += self.sizes[small]


def has_cycle(edges):
    disjoint_set = DisjointSet()

    for src, dst in edges:
        root_src = disjoint_set.find(src)
        root_dst = disjoint_set.find(dst)

        if root_src == root_dst:
            return True

        disjoint_set.union(root_src, root_dst)

    return False


disjoint_set = DisjointSet()
assert disjoint_set.find(0) == 0
assert disjoint_set.find(1) == 1
assert disjoint_set.find(2) == 2
assert disjoint_set.find(3) == 3
assert disjoint_set.find(4) == 4

disjoint_set.union(0, 1)
disjoint_set.union(1, 4)
assert disjoint_set.find(0) == disjoint_set.find(1) == disjoint_set.find(4)
assert disjoint_set.find(0) != disjoint_set.find(2)
assert disjoint_set.find(0) != disjoint_set.find(3)

disjoint_set.union(4, 3)
assert (
    disjoint_set.find(0)
    == disjoint_set.find(1)
    == disjoint_set.find(3)
    == disjoint_set.find(4)
)
assert disjoint_set.find(0) != disjoint_set.find(2)

disjoint_set.union(3, 2)
assert (
    disjoint_set.find(0)
    == disjoint_set.find(1)
    == disjoint_set.find(2)
    == disjoint_set.find(3)
    == disjoint_set.find(4)
)
