# https://leetcode.com/problems/making-a-large-island/

from collections import defaultdict


class Solution:
    def find_island(self, grid, si, sj, seen):
        points = set()

        if (si, sj) in seen:
            return points

        if si < 0 or sj < 0:
            return points

        if si >= len(grid) or sj >= len(grid):
            return points

        if grid[si][sj] == 0:
            return points

        seen.add((si, sj))
        points.add((si, sj))
        points.update(self.find_island(grid, si + 1, sj, seen))
        points.update(self.find_island(grid, si - 1, sj, seen))
        points.update(self.find_island(grid, si, sj + 1, seen))
        points.update(self.find_island(grid, si, sj - 1, seen))
        return points

    def largestIsland(self, grid: list[list[int]]) -> int:
        largest = 0

        seen = set()
        islands = defaultdict(lambda: set())
        for i in range(len(grid)):
            for j in range(len(grid)):
                island = self.find_island(grid, i, j, seen)
                largest = max(largest, len(island))
                for (si, sj) in island:
                    islands[(si, sj)] = island

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    continue

                flipped = set().union(
                    islands[(i + 1, j)],
                    islands[(i - 1, j)],
                    islands[(i, j + 1)],
                    islands[(i, j - 1)],
                )
                largest = max(largest, len(flipped) + 1)

        return largest


# Tests
solver = Solution()
assert solver.largestIsland([[1, 0], [0, 1]]) == 3
assert solver.largestIsland([[1, 1], [1, 0]]) == 4
assert solver.largestIsland([[1, 1], [1, 1]]) == 4
