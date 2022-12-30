# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n:
            weight += 1
            n = n & (n - 1)
        return weight

    # def hammingWeight(self, n: int) -> int:
    #     bits = bin(n)
    #     return len([x for x in bits if x == "1"])


# Tests
solver = Solution()
assert solver.hammingWeight(0b00000000000000000000000000001011) == 3
assert solver.hammingWeight(0b00000000000000000000000010000000) == 1
assert solver.hammingWeight(0b11111111111111111111111111111101) == 31
