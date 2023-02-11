from heapq import heappush, heappop


def dijkstra(graph, src):
    dists = [float("inf")] * len(graph)
    dists[src] = 0

    visited = set()
    pq = [(0, src)]
    while len(pq) > 0:
        (_, cur) = heappop(pq)

        if cur in visited:
            continue
        visited.add(cur)

        # for each neighbor check if the cost of going
        # from current to neighbor is lower than neighbor distance
        for (neighbor, cost) in enumerate(graph[cur]):
            alt = dists[cur] + cost
            if alt < dists[neighbor]:
                dists[neighbor] = alt
            heappush(pq, (dists[neighbor], neighbor))

    return dists


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

assert dijkstra(graph, 0) == [0, 2, 6, 7, 17, 22, 19]
assert dijkstra(graph, 1) == [2, 0, 8, 5, 15, 20, 17]
assert dijkstra(graph, 2) == [6, 8, 0, 8, 18, 23, 20]
assert dijkstra(graph, 3) == [7, 5, 8, 0, 10, 15, 12]
assert dijkstra(graph, 4) == [17, 15, 18, 10, 0, 6, 2]
assert dijkstra(graph, 5) == [22, 20, 23, 15, 6, 0, 6]
assert dijkstra(graph, 6) == [19, 17, 20, 12, 2, 6, 0]
