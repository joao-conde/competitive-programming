from heapq import heapify, heappush, heappop


def heapsort(collection):
    heapify(collection)
    return [heappop(collection) for _ in range(len(collection))]


assert heapsort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert heapsort([1, 5, 3, 2, 4]) == [1, 2, 3, 4, 5]
assert heapsort([-1, -5, -3, -2, -4]) == [-5, -4, -3, -2, -1]
