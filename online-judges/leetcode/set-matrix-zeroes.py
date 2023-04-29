# https://leetcode.com/problems/set-matrix-zeroes/


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0


# Tests
solver = Solution()

m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solver.setZeroes(m)
assert m == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solver.setZeroes(m)
assert m == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
