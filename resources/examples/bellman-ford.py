def bellman_ford(graph, src, dst):
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

    return dists[dst]


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

assert bellman_ford(graph, 0, 0) == 0
assert bellman_ford(graph, 0, 1) == -1
assert bellman_ford(graph, 0, 2) == 2
assert bellman_ford(graph, 0, 3) == -2
assert bellman_ford(graph, 0, 4) == 1

assert bellman_ford(graph, 1, 0) == INF
assert bellman_ford(graph, 1, 1) == 0
assert bellman_ford(graph, 1, 2) == 3
assert bellman_ford(graph, 1, 3) == -1
assert bellman_ford(graph, 1, 4) == 2

assert bellman_ford(graph, 2, 0) == INF
assert bellman_ford(graph, 2, 1) == INF
assert bellman_ford(graph, 2, 2) == 0
assert bellman_ford(graph, 2, 3) == INF
assert bellman_ford(graph, 2, 4) == INF
