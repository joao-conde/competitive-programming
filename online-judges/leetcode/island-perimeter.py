# https://leetcode.com/problems/island-perimeter/

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])

        perimeter = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 0:
                    continue

                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                if i == nrows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                if j == ncols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

        return perimeter


# Tests
solver = Solution()
assert (
    solver.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
    == 16
)
assert solver.islandPerimeter([[1]]) == 4
