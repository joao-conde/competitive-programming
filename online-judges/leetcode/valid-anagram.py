# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = dict()
        for c in s:
            s_counts[c] = s_counts.get(c, 0) + 1

        t_counts = dict()
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1

        return s_counts == t_counts


# Tests
solver = Solution()
assert solver.isAnagram("anagram", "nagaram") == True
assert solver.isAnagram("rat", "car") == False
