# https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single = 0
        for num in nums:
            single = single ^ num
        return single


# Tests
solver = Solution()
assert solver.singleNumber([2, 2, 1]) == 1
assert solver.singleNumber([4, 1, 2, 1, 2]) == 4
assert solver.singleNumber([1]) == 1
