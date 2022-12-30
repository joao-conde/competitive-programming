# https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        x = 0
        for _ in range(32):
            x = (x << 1) | (n & 1)
            n = n >> 1
        return x


# Tests
solver = Solution()
assert solver.reverseBits(0b00000010100101000001111010011100) == 964176192
assert solver.reverseBits(0b11111111111111111111111111111101) == 3221225471
