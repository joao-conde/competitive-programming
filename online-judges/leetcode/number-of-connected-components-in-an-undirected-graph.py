# https://www.lintcode.com/problem/591/


class Connections:
    def __init__(self, n):
        self.groups = dict()
        self.sizes = dict()

    def connect(self, a, b):
        if a not in self.groups:
            self.groups[a] = a
            self.sizes[a] = 1

        if b not in self.groups:
            self.groups[b] = b
            self.sizes[b] = 1

        while a != self.groups[a]:
            a = self.groups[a]

        while b != self.groups[b]:
            b = self.groups[b]

        if a == b:
            return

        small = a if self.sizes[a] < self.size[b] else b
        large = b if self.sizes[a] < self.size[b] else a
        self.groups[small] = large
        self.sizes[large] += self.sizes[small]

    def query(self):
        return len(set(self.groups.values()))


# Tests
connections = Connections(5)
assert connections.query() == 5
connections.connect(1, 2)
assert connections.query() == 4
connections.connect(2, 4)
assert connections.query() == 3
connections.connect(1, 4)
assert connections.query() == 3
