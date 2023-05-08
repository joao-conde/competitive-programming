# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        closest = float("-inf")
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return total

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total > target:
                    k -= 1
                else:
                    j += 1

        return closest


# Tests
solver = Solution()
assert solver.threeSumClosest([-1, 2, 1, -4], 1) == 2
assert solver.threeSumClosest([0, 0, 0], 1) == 0
