def bellman_ford(graph, src):
    n_vertices = len(graph)

    dists = [float("inf")] * n_vertices
    dists[src] = 0

    for _ in range(n_vertices - 1):
        # for each neighbor check if the cost of going
        # from current to neighbor is lower than neighbor distance
        for i in range(n_vertices):
            for j in range(n_vertices):
                alt = dists[i] + graph[i][j]
                if alt < dists[j]:
                    dists[j] = alt

    return dists


def has_cycle(graph, src):
    n_vertices = len(graph)
    dists = bellman_ford(graph, src)

    # run an extra cycle to see if anything improves
    for i in range(n_vertices):
        for j in range(n_vertices):
            alt = dists[i] + graph[i][j]
            if alt < dists[j]:
                return True

    return False


# Tests
# https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

INF = float("inf")
graph = [
    [0, -1, 4, INF, INF],
    [INF, 0, 3, 2, 2],
    [INF, INF, 0, INF, INF],
    [INF, 1, 5, 0, INF],
    [INF, INF, INF, -3, 0],
]

assert bellman_ford(graph, 0) == [0, -1, 2, -2, 1]
assert bellman_ford(graph, 1) == [INF, 0, 3, -1, 2]
assert bellman_ford(graph, 2) == [INF, INF, 0, INF, INF]
assert bellman_ford(graph, 3) == [INF, 1, 4, 0, 3]
assert bellman_ford(graph, 4) == [INF, -2, 1, -3, 0]

assert has_cycle(graph, 0) == False
