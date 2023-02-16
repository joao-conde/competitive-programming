# https://leetcode.com/problems/count-sub-islands/

from typing import List


class Solution:
    def get_island(self, grid, si, sj):
        m, n = len(grid), len(grid[0])
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        stack, points = [(si, sj)], set()
        while len(stack) > 0:
            (i, j) = stack.pop()

            if (i, j) in points:
                continue
            points.add((i, j))

            neighbors = []
            for di, dj in deltas:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= m:
                    continue

                if nj < 0 or nj >= n:
                    continue

                if grid[ni][nj] == 0:
                    continue

                neighbors.append((ni, nj))

            stack.extend(neighbors)
        return points

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        cnt, seen = 0, set()
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i, j) in seen:
                    continue

                if grid2[i][j] == 0:
                    continue

                island = self.get_island(grid2, i, j)
                seen.update(island)

                if all(grid1[ii][ij] == 1 for (ii, ij) in island):
                    cnt += 1
        return cnt


# Tests
solver = Solution()
assert (
    solver.countSubIslands(
        [
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1],
        ],
        [
            [1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 1, 0, 0, 0],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0],
        ],
    )
    == 3
)
assert (
    solver.countSubIslands(
        [
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
        ],
        [
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1],
        ],
    )
    == 2
)
