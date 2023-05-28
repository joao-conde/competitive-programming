# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top, bot = left, right

                top_left = matrix[top][left + i]
                matrix[top][left + i] = matrix[bot - i][left]
                matrix[bot - i][left] = matrix[bot][right - i]
                matrix[bot][right - i] = matrix[top + i][right]
                matrix[top + i][right] = top_left

            left += 1
            right -= 1


# Tests
solver = Solution()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solver.rotate(matrix)
assert matrix == [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
solver.rotate(matrix)
assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
