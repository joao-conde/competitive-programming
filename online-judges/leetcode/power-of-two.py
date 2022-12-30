# https://leetcode.com/problems/power-of-two/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bits = bin(n)[2:]
        return bits[0] == "1" and all(b == "0" for b in bits[1:])

    # def isPowerOfTwo(self, n: int) -> bool:
    #     return n != 0 and not n & (n - 1)


# Tests
solver = Solution()
assert solver.isPowerOfTwo(1) == True
assert solver.isPowerOfTwo(16) == True
assert solver.isPowerOfTwo(3) == False
