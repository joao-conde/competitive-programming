# https://leetcode.com/problems/pascals-triangle/


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        rows = []
        for r in range(numRows):
            row = [1] * (r + 1)
            for i in range(1, r):
                row[i] = rows[-1][i - 1] + rows[-1][i]
            rows.append(row)
        return rows


# Tests
solver = Solution()
assert solver.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert solver.generate(1) == [[1]]
