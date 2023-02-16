# https://leetcode.com/problems/max-area-of-island/

from typing import List, Set, Tuple


class Solution:
    def area(
        self, grid: List[List[int]], i: int, j: int, points: Set[Tuple[int, int]]
    ) -> Set[Tuple[int, int]]:
        if (i, j) in points:
            return points

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return points

        if grid[i][j] == 0:
            return points

        points.add((i, j))

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbors = [(i + di, j + dj) for (di, dj) in deltas]
        for ni, nj in neighbors:
            neighbor_area = self.area(grid, ni, nj, points)
            points = points.union(neighbor_area)

        return points

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max, explored = 0, set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue

                if (i, j) in explored:
                    continue

                points = self.area(grid, i, j, set())
                explored = explored.union(points)
                max = len(points) if len(points) > max else max

        return max


# Tests
solver = Solution()
assert (
    solver.maxAreaOfIsland(
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
    == 6
)
assert solver.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
assert (
    solver.maxAreaOfIsland(
        [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    )
    == 4
)
