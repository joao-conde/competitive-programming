# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted = [None] * len(nums)

        i, j, e = 0, len(nums) - 1, len(nums) - 1
        while e >= 0:
            squarei = nums[i] ** 2
            squarej = nums[j] ** 2
            if squarei >= squarej:
                sorted[e] = squarei
                i += 1
            else:
                sorted[e] = squarej
                j -= 1
            e -= 1

        return sorted


# Tests
solver = Solution()
assert solver.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert solver.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
assert solver.sortedSquares([-1, 0, 3, 10]) == [0, 1, 9, 100]
