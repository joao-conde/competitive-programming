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


disjoint_set = DisjointSet()
assert disjoint_set.find(0) == 0
assert disjoint_set.find(1) == 1
assert disjoint_set.find(2) == 2
assert disjoint_set.find(3) == 3
assert disjoint_set.find(4) == 4

disjoint_set.union(0, 1)
disjoint_set.union(1, 4)
assert disjoint_set.find(0) == 4
assert disjoint_set.find(1) == 4
assert disjoint_set.find(2) == 2
assert disjoint_set.find(3) == 3
assert disjoint_set.find(4) == 4

disjoint_set.union(4, 3)
assert disjoint_set.find(0) == 3
assert disjoint_set.find(1) == 3
assert disjoint_set.find(2) == 2
assert disjoint_set.find(3) == 3
assert disjoint_set.find(4) == 3

disjoint_set.union(3, 2)
assert disjoint_set.find(0) == 2
assert disjoint_set.find(1) == 2
assert disjoint_set.find(2) == 2
assert disjoint_set.find(3) == 2
assert disjoint_set.find(4) == 2
