# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        ways, n1, n2 = 0, 0, 1
        for _ in range(n):
            ways = n1 + n2
            n1 = n2
            n2 = ways
        return ways


# Tests
solver = Solution()
assert solver.climbStairs(1) == 1
assert solver.climbStairs(2) == 2
assert solver.climbStairs(3) == 3
assert solver.climbStairs(38) == 63245986
