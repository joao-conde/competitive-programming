# https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


# Tests
solver = Solution()
assert solver.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert solver.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
assert solver.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
assert solver.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
