# https://leetcode.com/problems/reverse-string/


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1


# Tests
solver = Solution()

s = ["h", "e", "l", "l", "o"]
solver.reverseString(s)
assert s == ["o", "l", "l", "e", "h"]

s = ["H", "a", "n", "n", "a", "h"]
solver.reverseString(s)
assert s == ["h", "a", "n", "n", "a", "H"]
