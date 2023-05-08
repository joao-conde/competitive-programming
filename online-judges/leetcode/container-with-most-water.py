# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        def getArea(i, j) -> int:
            return min(heights[i], heights[j]) * (j - i)

        i, j = 0, len(heights) - 1

        maxArea = -1
        while i < j:
            area = getArea(i, j)
            maxArea = max(maxArea, area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxArea


# Tests
solver = Solution()
assert solver.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert solver.maxArea([1, 1]) == 1
assert solver.maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
assert solver.maxArea([1, 3, 2, 5, 25, 24, 5]) == 24
