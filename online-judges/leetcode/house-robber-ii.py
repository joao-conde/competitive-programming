# https://leetcode.com/problems/house-robber-ii/


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def _rob(ns, cache):
            if len(ns) == 0:
                return 0

            key = len(ns)
            if key in cache:
                return cache[key]

            cache[key] = max(ns[0] + _rob(ns[2:], cache), _rob(ns[1:], cache))
            return cache[key]

        return max(_rob(nums[:-1], dict()), _rob(nums[1:], dict()))


# Tests
solver = Solution()
assert solver.rob([2, 3, 2]) == 3
assert solver.rob([1, 2, 3, 1]) == 4
assert solver.rob([1, 2, 3]) == 3
