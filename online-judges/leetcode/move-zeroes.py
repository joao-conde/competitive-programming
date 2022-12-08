# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def swap(self, nums: List[int], i: int, j: int) -> None:
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums

        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1

            j = i + 1
            while j < len(nums) and nums[j] == 0:
                j += 1

            if i < len(nums) and j < len(nums):
                self.swap(nums, i, j)

            i += 1


# Tests
solver = Solution()

nums = [0, 1, 0, 3, 12]
solver.moveZeroes(nums)
assert nums == [1, 3, 12, 0, 0]

nums = [0]
solver.moveZeroes(nums)
assert nums == [0]

nums = [0, 0, 1]
solver.moveZeroes(nums)
assert nums == [1, 0, 0]

nums = [1, 0]
solver.moveZeroes(nums)
assert nums == [1, 0]

nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
solver.moveZeroes(nums)
assert nums == [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
