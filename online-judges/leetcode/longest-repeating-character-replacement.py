# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counts = defaultdict(lambda: 0)

        i, j, maxf = 0, 0, 0
        while j < len(s):
            counts[s[j]] += 1
            maxf = max(maxf, counts[s[j]])

            if (j - i + 1) - maxf > k:
                counts[s[i]] -= 1
                i += 1

            longest = max(longest, j - i + 1)
            j += 1

        longest = max(longest, j - i)
        return longest


# Tests
solver = Solution()
assert solver.characterReplacement("ABAB", 2) == 4
assert solver.characterReplacement("AABABBA", 1) == 4
assert solver.characterReplacement("ABCDE", 1) == 2
