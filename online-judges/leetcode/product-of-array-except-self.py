# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(res)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


# Tests
solver = Solution()
assert solver.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert solver.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
