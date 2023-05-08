# https://leetcode.com/problems/4sum/


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()

        quadruplets = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 2):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    quadruplet = (nums[i], nums[j], nums[k], nums[l])
                    total = sum(quadruplet)
                    if total == target:
                        quadruplets.add(quadruplet)
                        k += 1
                        l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1

        return [list(quadruplet) for quadruplet in quadruplets]


# Tests
solver = Solution()
assert [-2, -1, 1, 2] in solver.fourSum([1, 0, -1, 0, -2, 2], 0)
assert [-2, 0, 0, 2] in solver.fourSum([1, 0, -1, 0, -2, 2], 0)
assert [-1, 0, 0, 1] in solver.fourSum([1, 0, -1, 0, -2, 2], 0)
assert solver.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
assert solver.fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
assert solver.fourSum([0], 0) == []
