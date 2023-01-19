# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = dict()

        def min_cost(cur):
            if cur in cache:
                return cache[cur]

            if cur >= len(cost):
                return 0

            cache[cur] = cost[cur] + min(min_cost(cur + 1), min_cost(cur + 2))
            return cache[cur]

        return min(min_cost(0), min_cost(1))


# Tests
solver = Solution()
assert solver.minCostClimbingStairs([10, 15, 20]) == 15
assert solver.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
