# https://leetcode.com/problems/find-median-from-data-stream/

from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2


# Tests
median_finder = MedianFinder()
median_finder.addNum(1)
median_finder.addNum(2)
assert median_finder.findMedian() == 1.5
median_finder.addNum(3)
assert median_finder.findMedian() == 2.0

median_finder = MedianFinder()
median_finder.addNum(6)
assert median_finder.findMedian() == 6.00000
median_finder.addNum(10)
assert median_finder.findMedian() == 8.00000
median_finder.addNum(2)
assert median_finder.findMedian() == 6.00000
median_finder.addNum(6)
assert median_finder.findMedian() == 6.00000
median_finder.addNum(5)
assert median_finder.findMedian() == 6.00000
median_finder.addNum(0)
assert median_finder.findMedian() == 5.50000
median_finder.addNum(6)
assert median_finder.findMedian() == 6.00000
median_finder.addNum(3)
assert median_finder.findMedian() == 5.50000
median_finder.addNum(1)
assert median_finder.findMedian() == 5.00000
median_finder.addNum(0)
assert median_finder.findMedian() == 4.00000
median_finder.addNum(0)
assert median_finder.findMedian() == 3.00000
