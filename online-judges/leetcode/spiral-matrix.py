# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        if len(matrix) == 0:
            return spiral

        mini, maxi = 0, len(matrix) - 1
        minj, maxj = 0, len(matrix[0]) - 1
        while mini <= maxi and minj <= maxj:
            for i in range(minj, maxj + 1):
                spiral.append(matrix[mini][i])
            mini += 1

            for i in range(mini, maxi + 1):
                spiral.append(matrix[i][maxj])
            maxj -= 1

            if mini <= maxi:
                for i in range(maxj, minj - 1, -1):
                    spiral.append(matrix[maxi][i])
                maxi -= 1

            if minj <= maxj:
                for i in range(maxi, mini - 1, -1):
                    spiral.append(matrix[i][minj])
                minj += 1

        return spiral


# Tests
solver = Solution()
assert solver.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
    1,
    2,
    3,
    6,
    9,
    8,
    7,
    4,
    5,
]
assert solver.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
    1,
    2,
    3,
    4,
    8,
    12,
    11,
    10,
    9,
    5,
    6,
    7,
]
assert solver.spiralOrder([[3], [2]]) == [3, 2]
assert solver.spiralOrder(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
assert solver.spiralOrder(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
) == [
    1,
    2,
    3,
    4,
    5,
    10,
    15,
    20,
    25,
    24,
    23,
    22,
    21,
    16,
    11,
    6,
    7,
    8,
    9,
    14,
    19,
    18,
    17,
    12,
    13,
]
assert solver.spiralOrder([[6, 9, 7]]) == [6, 9, 7]
assert solver.spiralOrder([[7], [9], [6]]) == [7, 9, 6]
assert solver.spiralOrder(
    [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]
) == [2, 3, 4, 7, 10, 13, 16, 15, 14, 11, 8, 5, 6, 9, 12]
assert solver.spiralOrder(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
) == [1, 2, 3, 4, 5, 10, 15, 14, 13, 12, 11, 6, 7, 8, 9]
