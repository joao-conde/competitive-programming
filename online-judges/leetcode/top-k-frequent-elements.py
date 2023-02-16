# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        top = []
        for num, count in counts.items():
            heappush(top, (count, num))
            if len(top) > k:
                heappop(top)

        top = [num for (_, num) in top]
        return top


# Tests
solver = Solution()
assert 1 in solver.topKFrequent([1, 1, 1, 2, 2, 3], 2)
assert 2 in solver.topKFrequent([1, 1, 1, 2, 2, 3], 2)
assert 1 in solver.topKFrequent([1], 1)
