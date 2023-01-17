# https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = dict()

        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2

            if n in cache:
                return cache[n]

            ways = climb(n - 1) + climb(n - 2)
            cache[n] = ways
            return ways

        return climb(n)


# Tests
solver = Solution()
assert solver.climbStairs(1) == 1
assert solver.climbStairs(2) == 2
assert solver.climbStairs(3) == 3
assert solver.climbStairs(38) == 63245986
