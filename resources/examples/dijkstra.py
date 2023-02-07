from heapq import heappush, heappop


def dijkstra(graph, src, dst):
    dists = [float("inf")] * len(graph)
    dists[src] = 0

    visited = set()
    pq = [(0, src)]
    while len(pq) > 0:
        (_, cur) = heappop(pq)

        if cur == dst:
            return dists[dst]

        if cur in visited:
            continue
        visited.add(cur)

        for (neighbor, cost) in enumerate(graph[cur]):
            alt = dists[cur] + cost
            if alt < dists[neighbor]:
                dists[neighbor] = alt
            heappush(pq, (dists[neighbor], neighbor))

    return -1


# Tests
# https://www.freecodecamp.org/news/content/images/2020/06/image-76.png

INF = float("inf")
graph = [
    [0, 2, 6, INF, INF, INF, INF],
    [2, 0, INF, 5, INF, INF, INF],
    [6, INF, 0, 8, INF, INF, INF],
    [INF, 5, 8, 0, 10, 15, INF],
    [INF, INF, INF, 10, 0, 6, 2],
    [INF, INF, INF, 15, 6, 0, 6],
    [INF, INF, INF, INF, 2, 6, 0],
]

assert dijkstra(graph, 2, 2) == 0
assert dijkstra(graph, 0, 6) == 19
assert dijkstra(graph, 2, 6) == 20
