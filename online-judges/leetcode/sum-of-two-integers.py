# https://leetcode.com/problems/sum-of-two-integers/


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask

        if a > mask // 2:
            return ~(a ^ mask)
        else:
            return a


# Tests
solver = Solution()
assert solver.getSum(1, 2) == 3
assert solver.getSum(2, 3) == 5
assert solver.getSum(1, 15) == 16
assert solver.getSum(10, 11) == 21
assert solver.getSum(-1, 1) == 0
