# https://leetcode.com/problems/01-matrix/


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    continue
                top = mat[i - 1][j] if i > 0 else float("inf")
                left = mat[i][j - 1] if j > 0 else float("inf")
                mat[i][j] = min(top, left) + 1

        for i in reversed(range(len(mat))):
            for j in reversed(range(len(mat[0]))):
                if mat[i][j] == 0:
                    continue
                bot = mat[i + 1][j] if i < len(mat) - 1 else float("inf")
                right = mat[i][j + 1] if j < len(mat[0]) - 1 else float("inf")
                mat[i][j] = min(mat[i][j], bot + 1, right + 1)
        return mat


# Tests
solver = Solution()
assert solver.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]
assert solver.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [
    [0, 0, 0],
    [0, 1, 0],
    [1, 2, 1],
]
assert solver.updateMatrix(
    [
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
    ]
) == [
    [0, 1, 0, 1, 2],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
]
