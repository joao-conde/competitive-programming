# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]


# Tests
solver = Solution()
assert solver.twoSum([2, 7, 11, 15], 9) == [1, 2]
assert solver.twoSum([2, 3, 4], 6) == [1, 3]
assert solver.twoSum([-1, 0], -1) == [1, 2]
assert solver.twoSum([5, 25, 75], 100) == [2, 3]
