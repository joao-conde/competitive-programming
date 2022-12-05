# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums)
        mid = lb + (ub - lb) // 2
        while lb < ub:
            if nums[mid] < target:
                lb = mid + 1
            elif nums[mid] > target:
                ub = mid
            else:
                return mid
            mid = lb + (ub - lb) // 2
        return mid


# Tests
solver = Solution()
assert solver.searchInsert([1, 3, 5, 6], 5) == 2
assert solver.searchInsert([1, 3, 5, 6], 2) == 1
assert solver.searchInsert([1, 3, 5, 6], 7) == 4
assert solver.searchInsert([1, 3, 5, 6], 0) == 0
assert solver.searchInsert([1, 3], 2) == 1
