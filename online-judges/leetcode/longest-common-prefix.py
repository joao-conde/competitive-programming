# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = min([len(s) for s in strs])
        common = ""

        i = 0
        while i < length:
            chars = set([s[i] for s in strs])
            if len(chars) != 1:
                break

            common += strs[0][i]
            i += 1

        return common


# Tests
solver = Solution()
assert solver.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert solver.longestCommonPrefix(["dog", "racecar", "car"]) == ""
