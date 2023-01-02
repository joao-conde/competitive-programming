# https://leetcode.com/problems/number-of-closed-islands/

from typing import List, Set, Tuple


class Solution:
    def get_island(
        self, grid: List[List[int]], si: int, sj: int
    ) -> Set[Tuple[int, int]]:
        stack, points = [(si, sj)], set([(si, sj)])
        while len(stack) > 0:
            (i, j) = stack.pop()

            deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            neighbors = [(i + di, j + dj) for (di, dj) in deltas]
            neighbors = [
                (ni, nj)
                for (ni, nj) in neighbors
                if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[ni])
            ]
            neighbors = [(ni, nj) for (ni, nj) in neighbors if grid[ni][nj] == 0]
            neighbors = [neighbor for neighbor in neighbors if neighbor not in points]

            points.update(neighbors)
            stack.extend(neighbors)

        return points

    def is_closed(self, grid: List[List[int]], island: Set[Tuple[int, int]]) -> bool:
        for (i, j) in island:
            if i <= 0 or j <= 0:
                return False

            if i >= len(grid) - 1 or j >= len(grid[i]) - 1:
                return False

        return True

    def closedIsland(self, grid: List[List[int]]) -> int:
        closed, visited = 0, set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in visited:
                    continue

                if grid[i][j] == 1:
                    continue

                island = self.get_island(grid, i, j)
                visited.update(island)

                if self.is_closed(grid, island):
                    closed += 1

        return closed


# Tests
solver = Solution()
assert (
    solver.closedIsland(
        [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ]
    )
    == 2
)
assert solver.closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]) == 1
assert (
    solver.closedIsland(
        [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]
    )
    == 2
)
assert (
    solver.closedIsland(
        [
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        ]
    )
    == 5
)
