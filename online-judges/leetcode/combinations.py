# https://leetcode.com/problems/combinations/


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        if k == 0:
            return [[]]

        combinations = []
        for i in range(k, n + 1):
            for comb in self.combine(i - 1, k - 1):
                combinations.append(comb + [i])

        return combinations


# Tests
solver = Solution()
print(solver.combine(4, 2))
print(solver.combine(1, 1))
