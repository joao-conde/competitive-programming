def minimalHeaviestSetA(arr):
    if len(arr) == 0:
        return []

    sumA, sumB = 0, 0
    i, j = 0, len(arr) - 1

    arr.sort()
    while i <= j:
        if sumA <= sumB:
            sumA += arr[j]
            j -= 1
        else:
            sumB += arr[i]
            i += 1

    sol = arr[j + 1 :]
    return set(sol)


assert minimalHeaviestSetA([3, 7, 5, 6, 2]) == set([6, 7])
assert minimalHeaviestSetA([5, 3, 2, 4, 1, 2]) == set([4, 5])
assert minimalHeaviestSetA([4, 2, 5, 1, 6]) == set([5, 6])
