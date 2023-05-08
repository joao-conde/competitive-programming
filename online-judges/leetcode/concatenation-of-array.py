# https://leetcode.com/problems/concatenation-of-array/


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums


# Tests
solver = Solution()
assert solver.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
assert solver.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
