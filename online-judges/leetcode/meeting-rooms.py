# https://www.lintcode.com/problem/920/


class Solution:
    def can_attend_meetings(self, intervals: list[tuple[int, int]]) -> bool:
        intervals.sort()

        last = intervals[0][1]
        for s, e in intervals[1:]:
            if s < last:
                return False
            last = e

        return True


# Tests
solver = Solution()
assert solver.can_attend_meetings([(0, 30), (5, 10), (15, 20)]) == False
assert solver.can_attend_meetings([(5, 8), (9, 15)]) == True
