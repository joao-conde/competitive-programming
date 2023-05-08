# https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Tests
solver = Solution()
assert solver.containsDuplicate([1, 2, 3, 1]) == True
assert solver.containsDuplicate([1, 2, 3, 4]) == False
assert solver.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
