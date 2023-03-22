# https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


# Tests
solver = Solution()
assert solver.isSubsequence("abc", "ahbgdc") == True
assert solver.isSubsequence("axc", "ahbgdc") == False
