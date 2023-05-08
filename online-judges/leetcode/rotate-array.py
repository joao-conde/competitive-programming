# https://leetcode.com/problems/rotate-array/


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tmp = nums[-k:] + nums[:-k]
        for i in range(len(tmp)):
            nums[i] = tmp[i]


# Tests
solver = Solution()

nums = [1, 2, 3, 4, 5, 6, 7]
solver.rotate(nums, 3)
assert nums == [5, 6, 7, 1, 2, 3, 4]

nums = [-1, -100, 3, 99]
solver.rotate(nums, 2)
assert nums == [3, 99, -1, -100]

nums = [1, 2]
solver.rotate(nums, 3)
assert nums == [2, 1]
