# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combinations = []
        for i, candidate in enumerate(candidates):
            if candidate > target:
                continue

            if candidate == target:
                combinations.append([candidate])

            for comb in self.combinationSum(candidates[i:], target - candidate):
                combinations.append([candidate] + comb)

        return combinations


# Tests
solver = Solution()
assert solver.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
assert solver.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
assert solver.combinationSum([2], 1) == []
