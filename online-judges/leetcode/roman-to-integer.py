# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        values = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

        i, number = 0, 0
        while i < len(s):
            cur = values[s[i]]
            next = values[s[i + 1]] if i + 1 < len(s) else cur
            if cur < next:
                number += next - cur
                i += 1
            else:
                number += cur
            i += 1

        return number


# Tests
solver = Solution()
assert solver.romanToInt("III") == 3
assert solver.romanToInt("LVIII") == 58
assert solver.romanToInt("MCMXCIV") == 1994
