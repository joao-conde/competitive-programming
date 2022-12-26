# https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # if current pixel is correctly colored just return
        if image[sr][sc] == color:
            return image

        # store previous color and paint current pixel
        prev = image[sr][sc]
        image[sr][sc] = color

        # check 4-directions and if within bounds and same color
        # has the pixel it started from, color it correctly
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for (dr, dc) in deltas:
            r = sr + dr
            c = sc + dc
            if r >= 0 and r < len(image) and c >= 0 and c < len(image[0]):
                if image[r][c] == prev:
                    self.floodFill(image, r, c, color)

        return image


# Tests
solver = Solution()
assert solver.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
    [2, 2, 2],
    [2, 2, 0],
    [2, 0, 1],
]
assert solver.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]]
