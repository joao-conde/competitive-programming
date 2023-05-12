# https://www.lintcode.com/problem/920/


class Solution:
    def can_attend_meetings(self, intervals: list[tuple[int, int]]) -> bool:
        intervals.sort()

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] >= i2[0]:
                return False

        return True


# Tests
solver = Solution()
assert solver.can_attend_meetings([(0, 30), (5, 10), (15, 20)]) == False
assert solver.can_attend_meetings([(5, 8), (9, 15)]) == True
