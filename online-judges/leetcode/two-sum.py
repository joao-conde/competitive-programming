# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complements = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            complements[num] = i
        return None


# Tests
solver = Solution()
assert solver.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert solver.twoSum([3, 2, 4], 6) == [1, 2]
assert solver.twoSum([3, 3], 6) == [0, 1]
