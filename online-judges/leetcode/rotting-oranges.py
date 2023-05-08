# https://leetcode.com/problems/rotting-oranges/

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        fresh, rotten = 0, deque()
        for i in range(m):
            for j in range(n):
                orange = grid[i][j]
                if orange == 1:
                    fresh += 1
                elif orange == 2:
                    rotten.append((i, j))

        minutes = 0
        while len(rotten) > 0 and fresh > 0:
            minutes += 1

            cur_rotten = [(i, j) for (i, j) in rotten]
            rotten.clear()
            for i, j in cur_rotten:
                deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                neighbors = [(i + di, j + dj) for (di, dj) in deltas]
                neighbors = [
                    (i, j)
                    for (i, j) in neighbors
                    if i >= 0 and i < m and j >= 0 and j < n
                ]

                for ni, nj in neighbors:
                    if grid[ni][nj] == 0 or grid[ni][nj] == 2:
                        continue

                    if grid[ni][nj] == 1:
                        fresh -= 1

                    grid[ni][nj] = 2
                    rotten.append((ni, nj))

        return minutes if fresh == 0 else -1


# Tests
solver = Solution()
assert solver.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
assert solver.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
assert solver.orangesRotting([[0, 2]]) == 0
assert solver.orangesRotting([[1], [1], [1], [1]]) == -1
assert solver.orangesRotting([[0]]) == 0
assert solver.orangesRotting([[2, 1, 0, 2]]) == 1
