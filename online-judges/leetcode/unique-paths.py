# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            grid[i][-1] = 1

        for i in range(n):
            grid[-1][i] = 1

        for mi in range(m - 2, -1, -1):
            for ni in range(n - 2, -1, -1):
                grid[mi][ni] = grid[mi + 1][ni] + grid[mi][ni + 1]

        return grid[0][0]


# Tests
solver = Solution()
assert solver.uniquePaths(3, 7) == 28
assert solver.uniquePaths(3, 2) == 3
