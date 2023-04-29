# https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = nums[0]
        max_p = nums[0]
        min_p = nums[0]

        for num in nums[1:]:
            tmp = max_p
            max_p = max(max_p * num, num * min_p, num)
            min_p = min(tmp * num, num * min_p, num)
            max_product = max(max_p, max_product)

        return max_product


# Tests
solver = Solution()
assert solver.maxProduct([2, 3, -2, 4]) == 6
assert solver.maxProduct([-2, 0, -1]) == 0
assert solver.maxProduct([0, 2]) == 2
assert solver.maxProduct([-2, 3, -4]) == 24
assert solver.maxProduct([2, -5, -2, -4, 3]) == 24
