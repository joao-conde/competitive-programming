groups = dict()


def find(x):
    if x not in groups:
        groups[x] = x

    while x != groups[x]:
        x = groups[x]
    return x


def union(x, y):
    group_x = find(x)
    group_y = find(y)
    groups[group_x] = group_y


def kruskal(edges):
    edges.sort()

    mst = []
    while len(edges) > 0:
        cost, src, dst = edges.pop(0)

        if find(src) != find(dst):
            union(src, dst)
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
