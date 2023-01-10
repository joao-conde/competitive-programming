# https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = [defaultdict(lambda: 0) for s in strs]
        for i in range(len(strs)):
            for c in strs[i]:
                counts[i][c] += 1

        groups = []
        for i in range(len(counts)):
            count = counts[i]

            new = True
            for group in groups:
                (group_cnt, _) = group[-1]
                if group_cnt == count:
                    group.append((count, i))
                    new = False
                    break

            if new:
                groups.append([(count, i)])

        return [[strs[i] for (_, i) in g] for g in groups]


# Tests
solver = Solution()
assert solver.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"],
]
assert solver.groupAnagrams([""]) == [[""]]
assert solver.groupAnagrams(["a"]) == [["a"]]
