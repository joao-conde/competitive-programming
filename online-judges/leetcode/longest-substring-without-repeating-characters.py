# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        longest, i, j = 0, 0, 0
        seen = set()
        while i < len(s):
            if j >= len(s) or s[j] in seen:
                seen.clear()
                length = j - i
                longest = longest if longest > length else length
                i += 1
                j = i
            else:
                seen.add(s[j])
                j += 1

        return longest


# Tests
solver = Solution()
assert solver.lengthOfLongestSubstring("abcabcbb") == 3
assert solver.lengthOfLongestSubstring("bbbbb") == 1
assert solver.lengthOfLongestSubstring("pwwkew") == 3
assert solver.lengthOfLongestSubstring(" ") == 1
assert solver.lengthOfLongestSubstring("au") == 2
