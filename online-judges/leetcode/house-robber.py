# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0
        for num in nums:
            tmp = sum1
            sum1 = max(sum2 + num, sum1)
            sum2 = tmp
        return sum1


# Tests
solver = Solution()
assert solver.rob([1, 2, 3, 1]) == 4
assert solver.rob([2, 7, 9, 3, 1]) == 12
assert solver.rob([1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]) == 42
