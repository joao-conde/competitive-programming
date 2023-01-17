# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = nums[0]
        for num in nums[1:]:
            missing ^= num

        for i in range(len(nums) + 1):
            missing ^= i

        return missing


# Tests
solver = Solution()
assert solver.missingNumber([3, 0, 1]) == 2
assert solver.missingNumber([0, 1]) == 2
assert solver.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
