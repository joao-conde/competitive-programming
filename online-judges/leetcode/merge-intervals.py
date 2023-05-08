# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals)

        merged = []
        start, end = intervals[0][0], intervals[0][1]
        for interval in intervals[1:]:
            s, e = interval[0], interval[1]
            if s > end:
                merged.append([start, end])
                start = s
                end = e
            else:
                end = max(end, e)

        merged.append([start, end])
        return merged


# Tests
solver = Solution()
assert solver.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert solver.merge([[1, 4], [4, 5]]) == [[1, 5]]
assert solver.merge([[1, 4], [2, 3]]) == [[1, 4]]
assert solver.merge([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]) == [
    [1, 3],
    [4, 7],
]
