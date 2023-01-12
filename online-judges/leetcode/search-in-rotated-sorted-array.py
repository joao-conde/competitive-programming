# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


# Tests
solver = Solution()
assert solver.search([0, 1, 2, 3, 4, 5, 6], 5) == 5
assert solver.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert solver.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert solver.search([1], 0) == -1
assert solver.search([3, 1], 0) == -1
assert solver.search([3, 1], 1) == 1
assert solver.search([9, 1, 2, 3, 4, 5, 6, 7, 8], 9) == 0
