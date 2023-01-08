# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        jump = 2 * (numRows - 1)
        for r in range(numRows):
            for i in range(r, len(s), jump):
                res += s[i]

                diag_i = i + jump - 2 * r
                if r > 0 and r < numRows - 1 and diag_i < len(s):
                    res += s[diag_i]

        return res


# Tests
solver = Solution()
assert solver.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert solver.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert solver.convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
assert solver.convert("A", 1) == "A"
