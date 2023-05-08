# https://leetcode.com/problems/koko-eating-bananas/

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lb, ub = 1, max(piles)
        while lb < ub:
            k = lb + (ub - lb) // 2
            time = self.eating_time(piles, k)

            if time <= h:
                ub = k
            else:
                lb = k + 1

        return ub

    def eating_time(self, piles, k):
        time = 0
        for pile in piles:
            time += math.ceil(pile / k)
        return time


# Tests
solver = Solution()
assert solver.minEatingSpeed([3, 6, 7, 11], 8) == 4
assert solver.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
assert solver.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
assert solver.minEatingSpeed([312884470], 312884469) == 2
