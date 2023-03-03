# https://leetcode.com/problems/divisor-game/


class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0


# Tests
solver = Solution()
assert solver.divisorGame(2) == True
assert solver.divisorGame(3) == False
