# https://leetcode.com/problems/course-schedule/


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # build the dependency graph
        graph = [[] for i in range(numCourses)]
        indegrees = {i: 0 for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
            indegrees[b] += 1

        # find the initial sources
        sources = [k for k, v in indegrees.items() if v == 0]

        # topological order found by popping as dependencies are met
        visited = set()
        topological = []
        while len(sources) > 0:
            source = sources.pop()
            if source in visited:
                continue

            visited.add(source)
            topological.append(source)

            for neighbor in graph[source]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    sources.append(neighbor)

        return len(topological) == numCourses


# Tests
solver = Solution()
assert solver.canFinish(2, [[1, 0]]) == True
assert solver.canFinish(2, [[1, 0], [0, 1]]) == False
assert solver.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]) == True
