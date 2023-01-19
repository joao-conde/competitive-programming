# https://leetcode.com/problems/plus-one/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        carry = 0
        for i in reversed(range(len(digits))):
            total = carry + digits[i]
            carry = total // 10
            remainder = total % 10
            digits[i] = remainder

        return digits if carry == 0 else [carry] + digits


# Tests
solver = Solution()
assert solver.plusOne([1, 2, 3]) == [1, 2, 4]
assert solver.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
assert solver.plusOne([9]) == [1, 0]
