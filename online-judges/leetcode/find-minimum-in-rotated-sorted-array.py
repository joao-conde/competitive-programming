# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        answer = float("inf")
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            answer = min(answer, nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return answer


# Tests
solver = Solution()
assert solver.findMin([3, 4, 5, 1, 2]) == 1
assert solver.findMin([5, 1, 2, 3, 4]) == 1
assert solver.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert solver.findMin([11, 13, 15, 17]) == 11
