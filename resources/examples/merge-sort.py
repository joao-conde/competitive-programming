def mergesort(collection):
    if len(collection) <= 1:
        return collection

    middle = len(collection) // 2
    left = mergesort(collection[:middle])
    right = mergesort(collection[middle:])
    merged = merge(left, right)
    return merged


def merge(left, right):
    merged = []

    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    while l < len(left):
        merged.append(left[l])
        l += 1

    while r < len(right):
        merged.append(right[r])
        r += 1

    return merged


assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert mergesort([1, 5, 3, 2, 4]) == [1, 2, 3, 4, 5]
assert mergesort([-1, -5, -3, -2, -4]) == [-5, -4, -3, -2, -1]
assert mergesort(
    [
        1,
        0,
        -2,
        23,
    ]
) == [-2, 0, 1, 23]
