# https://leetcode.com/problems/counting-bits/

from typing import List


class Solution:
    def countOnes(self, x: int) -> int:
        ones = 0
        while x != 0:
            ones += x & 1
            x >>= 1
        return ones

    def countBits(self, n: int) -> List[int]:
        return [self.countOnes(x) for x in range(n + 1)]


# Tests
solver = Solution()
assert solver.countBits(2) == [0, 1, 1]
assert solver.countBits(5) == [0, 1, 1, 2, 1, 2]
