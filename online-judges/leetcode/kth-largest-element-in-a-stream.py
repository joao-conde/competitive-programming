# https://leetcode.com/problems/kth-largest-element-in-a-stream/


from heapq import heapify, heappush, heappop


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


# Tests
largest = KthLargest(3, [4, 5, 8, 2])
assert largest.add(3) == 4
assert largest.add(5) == 5
assert largest.add(10) == 5
assert largest.add(9) == 8
assert largest.add(4) == 8

largest = KthLargest(1, [])
assert largest.add(-3) == -3
assert largest.add(-2) == -2
assert largest.add(-4) == -2
assert largest.add(0) == 0
assert largest.add(4) == 4
