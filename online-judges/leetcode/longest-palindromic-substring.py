# https://leetcode.com/problems/longest-palindromic-substring/

from typing import Tuple


class Solution:
    def expand(self, s: str, l: int, r: int) -> Tuple[int, int]:
        x, y = l, r
        while x >= 0 and y < len(s) and s[x] == s[y]:
            x -= 1
            y += 1
        return (x, y)

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            (x1, y1) = self.expand(s, i, i)
            (x2, y2) = self.expand(s, i, i + 1)

            if y1 - x1 > end - start:
                start = x1
                end = y1

            if y2 - x2 > end - start:
                start = x2
                end = y2

        return s[start + 1 : end]


# Tests
solver = Solution()
assert solver.longestPalindrome("babad") == "bab"
assert solver.longestPalindrome("cbbd") == "bb"
assert (
    solver.longestPalindrome(
        "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
    )
    == "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
)
