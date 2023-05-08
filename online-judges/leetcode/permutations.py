# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]

        permutations = []
        for i in range(len(nums)):
            for p in self.permute(nums[:i] + nums[i + 1 :]):
                permutations.append([nums[i]] + p)

        return permutations


# Tests
solver = Solution()
print(solver.permute([1, 2, 3]))
print(solver.permute([0, 1]))
print(solver.permute([1]))
