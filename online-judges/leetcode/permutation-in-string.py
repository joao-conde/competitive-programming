# https://leetcode.com/problems/permutation-in-string/


class Solution:
    def counts(self, s):
        map = dict()
        for c in s:
            map[c] = map.get(c, 0) + 1
        return map

    def contains(self, map1, map2):
        return all([map2.get(k, 0) == v for k, v in map1.items()])

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        s1map = self.counts(s1)
        slidingmap = self.counts(s2[:s1len])

        if self.contains(s1map, slidingmap):
            return True

        for i in range(0, len(s2) - s1len):
            added = s2[i + s1len]
            evicted = s2[i]
            slidingmap[added] = slidingmap.get(added, 0) + 1
            slidingmap[evicted] -= 1

            if self.contains(s1map, slidingmap):
                return True

        return False


# Tests
solver = Solution()
assert solver.checkInclusion("ab", "eidbaooo") == True
assert solver.checkInclusion("ab", "eidboaoo") == False
assert solver.checkInclusion("adc", "dcda") == True
