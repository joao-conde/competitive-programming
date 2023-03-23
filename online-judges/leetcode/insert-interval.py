# https://leetcode.com/problems/insert-interval/

from typing import List


class Solution:
    def overlaps(self, i1, i2):
        s1, e1 = i1
        s2, e2 = i2
        return (s1 <= s2 and e1 >= s2) or (s2 <= s1 and e2 >= s1)

    def merge(self, i1, i2):
        s1, e1 = i1
        s2, e2 = i2
        return [min(s1, s2), max(e1, e2)]

    def smaller(self, i1, i2):
        s1, _ = i1
        s2, _ = i2
        return s1 < s2

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        i = 0
        new = []
        merged = newInterval

        while (
            i < len(intervals)
            and self.smaller(intervals[i], newInterval)
            and not self.overlaps(intervals[i], newInterval)
        ):
            new.append(intervals[i])
            i += 1

        while i < len(intervals) and self.overlaps(intervals[i], merged):
            merged = self.merge(intervals[i], merged)
            i += 1
        new.append(merged)

        while i < len(intervals):
            new.append(intervals[i])
            i += 1

        return new


# Tests
solver = Solution()
assert solver.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
assert solver.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
    [1, 2],
    [3, 10],
    [12, 16],
]
assert solver.insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]
