# https://leetcode.com/problems/number-of-islands/

from collections import deque
from typing import List, Set, Tuple


class Solution:
    def get_island(self, grid: List[List[str]], i: int, j: int) -> Set[Tuple[int, int]]:
        points, dq = set(), deque([(i, j)])
        while len(dq) > 0:
            (pi, pj) = dq.popleft()

            deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            neighbors = [(pi + di, pj + dj) for (di, dj) in deltas]
            neighbors = [
                (ni, nj)
                for (ni, nj) in neighbors
                if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[ni])
            ]
            neighbors = [(ni, nj) for (ni, nj) in neighbors if grid[ni][nj] == "1"]
            neighbors = [neighbor for neighbor in neighbors if neighbor not in points]

            dq.extend(neighbors)
            points.update(neighbors)

        return points

    def numIslands(self, grid: List[List[str]]) -> int:
        skip, islands = set(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue

                if (i, j) in skip:
                    continue

                island = self.get_island(grid, i, j)
                skip.update(island)
                islands += 1

        return islands


# Tests
solver = Solution()
assert (
    solver.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
    == 1
)
assert (
    solver.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
    == 3
)
