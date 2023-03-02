def floyd_warshall(graph):
    n_vertices = len(graph)
    dists = [[graph[i][j] for i in range(n_vertices)] for j in range(n_vertices)]

    for intermediate in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                alt = dists[i][intermediate] + dists[intermediate][j]
                if alt < dists[i][j]:
                    dists[i][j] = alt

    return dists


# Tests
# https://www.freecodecamp.org/news/content/images/2020/06/image-76.png

INF = float("INF")
graph = [
    [0, 2, 6, INF, INF, INF, INF],
    [2, 0, INF, 5, INF, INF, INF],
    [6, INF, 0, 8, INF, INF, INF],
    [INF, 5, 8, 0, 10, 15, INF],
    [INF, INF, INF, 10, 0, 6, 2],
    [INF, INF, INF, 15, 6, 0, 6],
    [INF, INF, INF, INF, 2, 6, 0],
]

assert floyd_warshall(graph) == [
    [0, 2, 6, 7, 17, 22, 19],
    [2, 0, 8, 5, 15, 20, 17],
    [6, 8, 0, 8, 18, 23, 20],
    [7, 5, 8, 0, 10, 15, 12],
    [17, 15, 18, 10, 0, 6, 2],
    [22, 20, 23, 15, 6, 0, 6],
    [19, 17, 20, 12, 2, 6, 0],
]
