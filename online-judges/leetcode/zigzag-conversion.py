# https://leetcode.com/problems/zigzag-conversion/

# TODO: https://leetcode.com/problems/spiral-matrix/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        jump = 2 * (numRows - 1)

        i = 0
        while i < len(s):
            res += s[i]
            i += jump

        for r in range(1, numRows - 1):
            i = r
            while i < len(s):
                res += s[i]

                diag_i = (i + jump) - 2 * r
                if diag_i < len(s):
                    res += s[diag_i]

                i += jump

        i = numRows - 1
        while i < len(s):
            res += s[i]
            i += jump

        return res


# Tests
solver = Solution()
assert solver.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert solver.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert solver.convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
assert solver.convert("A", 1) == "A"
