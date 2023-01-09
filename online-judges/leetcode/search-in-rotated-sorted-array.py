# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def find_pivot(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                return left
            left = left + 1
        return -1

    def bin_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot_i = self.find_pivot(nums)
        res = self.bin_search(nums, 0, pivot_i, target)
        res = res if res != -1 else self.bin_search(nums, pivot_i, len(nums), target)
        return res


# Tests
solver = Solution()
assert solver.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert solver.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert solver.search([1], 0) == -1
assert solver.search([3, 1], 0) == -1
assert solver.search([3, 1], 1) == 1
assert solver.search([9, 1, 2, 3, 4, 5, 6, 7, 8], 9) == 0
