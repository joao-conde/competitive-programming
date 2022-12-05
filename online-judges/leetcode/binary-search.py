# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums) - 1

        mid = lb + (ub - lb) // 2
        while lb <= ub:
            if nums[mid] < target:
                lb = mid + 1
            elif nums[mid] > target:
                ub = mid - 1
            else:
                return mid

            mid = lb + (ub - lb) // 2
        return -1


# Tests
solver = Solution()
assert solver.search([-1, 0, 3, 5, 9, 12], 9) == 4
assert solver.search([-1, 0, 3, 5, 9, 12], 2) == -1
assert solver.search([5], 5) == 0
