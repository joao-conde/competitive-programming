# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.map = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.map[key]

        res = ""
        left, right = 0, len(timestamps) - 1
        while left <= right:
            mid = left + (right - left) // 2
            (value, ts) = timestamps[mid]

            if ts <= timestamp:
                res = value
                left = mid + 1
            else:
                right = mid - 1

        return res


# Tests
time_map = TimeMap()
time_map.set("foo", "bar", 1)
assert time_map.get("foo", 1) == "bar"
assert time_map.get("foo", 3) == "bar"
time_map.set("foo", "bar2", 4)
assert time_map.get("foo", 4) == "bar2"
assert time_map.get("foo", 5) == "bar2"

time_map = TimeMap()
time_map.set("love", "high", 10)
time_map.set("love", "low", 20)
assert time_map.get("love", 5) == ""
assert time_map.get("love", 10) == "high"
assert time_map.get("love", 15) == "high"
assert time_map.get("love", 20) == "low"
assert time_map.get("love", 25) == "low"
