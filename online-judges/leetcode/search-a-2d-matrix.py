# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_i, row_left, row_right = 0, 0, len(matrix) - 1
        while row_left <= row_right:
            row_i = row_left + (row_right - row_left) // 2
            row = matrix[row_i]
            if target >= row[0] and target <= row[-1]:
                break
            elif row[-1] < target:
                row_left = row_i + 1
            elif row[0] > target:
                row_right = row_i - 1

        col_i, col_left, col_right = 0, 0, len(matrix[row_i]) - 1
        while col_left <= col_right:
            col_i = col_left + (col_right - col_left) // 2
            if target == matrix[row_i][col_i]:
                return True
            elif matrix[row_i][col_i] < target:
                col_left = col_i + 1
            elif matrix[row_i][col_i] > target:
                col_right = col_i - 1

        return target == matrix[row_i][col_i]


# Tests
solver = Solution()
assert (
    solver.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True
)
assert (
    solver.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False
)
assert solver.searchMatrix([[1]], 1) == True
assert solver.searchMatrix([[1]], 3) == False
assert solver.searchMatrix([[1, 3]], 3) == True
