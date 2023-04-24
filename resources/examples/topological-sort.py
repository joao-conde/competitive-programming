from collections import deque


def topological(graph):
    # build the dependency graph
    indegrees = {i: 0 for i in range(len(graph))}
    for _, neighbors in enumerate(graph):
        for neighbor in neighbors:
            indegrees[neighbor] += 1

    # find the initial sources
    sources = deque([k for k, v in indegrees.items() if v == 0])

    # topological order found by popping as dependencies are met
    visited = set()
    topological = []
    while len(sources) > 0:
        source = sources.popleft()
        if source in visited:
            continue

        visited.add(source)
        topological.append(source)

        for neighbor in graph[source]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                sources.append(neighbor)

    return topological


# Tests
# https://www.geeksforgeeks.org/topological-sorting/

graph = [
    [],
    [],
    [3],
    [1],
    [0, 1],
    [0, 2],
]

assert topological(graph) == [4, 5, 0, 2, 3, 1]
