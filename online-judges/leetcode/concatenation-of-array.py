# https://leetcode.com/problems/concatenation-of-array/

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


# Tests
solver = Solution()
assert solver.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
assert solver.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
