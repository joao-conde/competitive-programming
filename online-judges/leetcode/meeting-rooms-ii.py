# https://www.lintcode.com/problem/919/


class Solution:
    def min_meeting_rooms(self, intervals: list[tuple[int, int]]) -> int:
        if len(intervals) == 0:
            return 0

        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        events.sort()

        max_busy, busy = 1, 0
        for event in events:
            busy += event[1]
            max_busy = max(max_busy, busy)

        return max_busy


# Tests
solver = Solution()
assert solver.min_meeting_rooms([(0, 30), (5, 10), (15, 20)]) == 2
assert solver.min_meeting_rooms([(2, 7)]) == 1
