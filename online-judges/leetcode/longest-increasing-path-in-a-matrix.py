# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


class Solution:
    def longest_from(self, matrix, i, j, cache):
        if (i, j) in cache:
            return cache[(i, j)]

        m = len(matrix)
        n = len(matrix[i])
        at = matrix[i][j]

        longest = 1

        if i > 0 and at < matrix[i - 1][j]:
            longest = max(longest, 1 + self.longest_from(matrix, i - 1, j, cache))

        if i < m - 1 and at < matrix[i + 1][j]:
            longest = max(longest, 1 + self.longest_from(matrix, i + 1, j, cache))

        if j > 0 and at < matrix[i][j - 1]:
            longest = max(longest, 1 + self.longest_from(matrix, i, j - 1, cache))

        if j < n - 1 and at < matrix[i][j + 1]:
            longest = max(longest, 1 + self.longest_from(matrix, i, j + 1, cache))

        cache[(i, j)] = longest
        return cache[(i, j)]

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        longest = 1
        cache = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                longest = max(longest, self.longest_from(matrix, i, j, cache))
        return longest


# Tests
solver = Solution()
assert solver.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
assert solver.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
assert solver.longestIncreasingPath([[1]]) == 1
