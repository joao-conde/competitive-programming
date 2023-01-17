# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = float("inf")
        for price in prices:
            if price < lowest:
                lowest = price
            profit = max(profit, price - lowest)
        return profit


# Tests
solver = Solution()
assert solver.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert solver.maxProfit([7, 6, 4, 3, 1]) == 0
