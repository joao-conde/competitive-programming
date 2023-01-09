# https://leetcode.com/problems/combination-sum/

from typing import Dict, List


class Solution:
    def helper(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        for candidate in candidates:
            if candidate > target:
                continue

            if candidate == target:
                combinations.append([candidate])

            for comb in self.helper(candidates, target - candidate):
                combinations.append([candidate] + comb)

        return combinations

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = self.helper(candidates, target)
        unique = set()
        for comb in combinations:
            comb_t = tuple(sorted(comb))
            if comb_t not in unique:
                unique.add(comb_t)

        return list([list(s) for s in unique])


# Tests
solver = Solution()
assert solver.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
assert solver.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
assert solver.combinationSum([2], 1) == []
