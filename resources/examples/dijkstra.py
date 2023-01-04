from heapq import heappush, heappop


def dijkstra(graph, src, dst):
    prev = [None] * len(graph)
    dists = [float("inf")] * len(graph)

    visited = set()
    pq = [(0, src)]
    dists[src] = 0
    while len(pq) > 0:
        (_, cur) = heappop(pq)

        if cur in visited:
            continue
        visited.add(cur)

        if cur == dst:
            return dists[dst], prev

        for (neighbor, cost) in enumerate(graph[cur]):
            alt = dists[cur] + cost
            if alt < dists[neighbor]:
                prev[neighbor] = cur
                dists[neighbor] = alt
            heappush(pq, (dists[neighbor], neighbor))

    return -1, []


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

dist, prev = dijkstra(graph, 2, 6)
print(dist, prev)
