# https://leetcode.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = 0

        for i in range(len(s)):
            substrings += self.count(s, i, i)
            substrings += self.count(s, i, i + 1)

        return substrings

    def count(self, s, left, right):
        palis = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            palis += 1
            left -= 1
            right += 1

        return palis


# Tests
solver = Solution()
assert solver.countSubstrings("abc") == 3
assert solver.countSubstrings("aaa") == 6
