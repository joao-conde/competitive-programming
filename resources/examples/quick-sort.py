def quicksort(collection):
    return _quicksort(collection, 0, len(collection) - 1)


def _quicksort(collection, left, right):
    if left >= right:
        return

    pivot = collection[(left + right) // 2]
    split = partition(collection, left, right, pivot)
    _quicksort(collection, left, split - 1)
    _quicksort(collection, split, right)
    return collection


def partition(collection, left, right, pivot):
    while left <= right:
        while collection[left] < pivot:
            left += 1

        while collection[right] > pivot:
            right -= 1

        if left <= right:
            tmp = collection[left]
            collection[left] = collection[right]
            collection[right] = tmp
            left += 1
            right -= 1

    return left


assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert quicksort([1, 5, 3, 2, 4]) == [1, 2, 3, 4, 5]
assert quicksort([-1, -5, -3, -2, -4]) == [-5, -4, -3, -2, -1]
assert quicksort(
    [
        1,
        0,
        -2,
        23,
    ]
) == [-2, 0, 1, 23]
