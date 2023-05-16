# https://leetcode.com/problems/pacific-atlantic-water-flow/


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])

        def dfs(ocean, i, j):
            if (i, j) in ocean:
                return
            ocean.add((i, j))

            if i + 1 < m and heights[i + 1][j] >= heights[i][j]:
                dfs(ocean, i + 1, j)

            if i > 0 and heights[i - 1][j] >= heights[i][j]:
                dfs(ocean, i - 1, j)

            if j + 1 < n and heights[i][j + 1] >= heights[i][j]:
                dfs(ocean, i, j + 1)

            if j > 0 and heights[i][j - 1] >= heights[i][j]:
                dfs(ocean, i, j - 1)

        pacific = set()
        atlantic = set()

        for i in range(m):
            dfs(pacific, i, 0)
            dfs(atlantic, i, n - 1)

        for j in range(n):
            dfs(pacific, 0, j)
            dfs(atlantic, m - 1, j)

        common = sorted([i, j] for (i, j) in pacific.intersection(atlantic))
        return common


# Tests
solver = Solution()
assert solver.pacificAtlantic(
    [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
assert solver.pacificAtlantic([[1]]) == [[0, 0]]
