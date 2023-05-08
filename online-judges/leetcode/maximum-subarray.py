# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sub = nums[0]

        cur_sum = 0
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sub = max(max_sub, cur_sum)

        return max_sub


# Tests
solver = Solution()
assert solver.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert solver.maxSubArray([1]) == 1
assert solver.maxSubArray([5, 4, -1, 7, 8]) == 23
