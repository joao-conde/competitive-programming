# https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow_b = 0
        while True:
            slow = nums[slow]
            slow_b = nums[slow_b]
            if slow_b == slow:
                break

        return slow


# Tests
solver = Solution()
assert solver.findDuplicate([1, 3, 4, 2, 2]) == 2
assert solver.findDuplicate([3, 1, 3, 4, 2]) == 3
assert solver.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]) == 9
