# https://leetcode.com/problems/jump-game/


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        cache = dict()

        def dfs(pos):
            if pos in cache:
                return cache[pos]

            if pos >= len(nums) - 1:
                cache[pos] = True
                return True

            for jump in reversed(range(pos + 1, pos + nums[pos] + 1)):
                if dfs(jump):
                    cache[pos] = True
                    return True

            cache[pos] = False
            return False

        return dfs(0)


# Tests
solver = Solution()
assert solver.canJump([2, 3, 1, 1, 4]) == True
assert solver.canJump([3, 2, 1, 0, 4]) == False
assert (
    solver.canJump(
        [
            8,
            2,
            4,
            4,
            4,
            9,
            5,
            2,
            5,
            8,
            8,
            0,
            8,
            6,
            9,
            1,
            1,
            6,
            3,
            5,
            1,
            2,
            6,
            6,
            0,
            4,
            8,
            6,
            0,
            3,
            2,
            8,
            7,
            6,
            5,
            1,
            7,
            0,
            3,
            4,
            8,
            3,
            5,
            9,
            0,
            4,
            0,
            1,
            0,
            5,
            9,
            2,
            0,
            7,
            0,
            2,
            1,
            0,
            8,
            2,
            5,
            1,
            2,
            3,
            9,
            7,
            4,
            7,
            0,
            0,
            1,
            8,
            5,
            6,
            7,
            5,
            1,
            9,
            9,
            3,
            5,
            0,
            7,
            5,
        ]
    )
    == True
)
