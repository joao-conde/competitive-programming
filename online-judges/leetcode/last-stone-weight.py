# https://leetcode.com/problems/last-stone-weight/

from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            if y > x:
                heappush(stones, -(y - x))

        return -stones[0] if len(stones) > 0 else 0


# Tests
solver = Solution()
assert solver.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
assert solver.lastStoneWeight([1]) == 1
