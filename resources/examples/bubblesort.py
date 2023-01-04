def bubblesort(collection):
    for n in range(len(collection)):
        for i in range(len(collection) - n - 1):
            if collection[i] > collection[i + 1]:
                tmp = collection[i]
                collection[i] = collection[i + 1]
                collection[i + 1] = tmp
    return collection


assert bubblesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert bubblesort([1, 5, 3, 2, 4]) == [1, 2, 3, 4, 5]
assert bubblesort([-1, -5, -3, -2, -4]) == [-5, -4, -3, -2, -1]
assert bubblesort(
    [
        1,
        0,
        -2,
        23,
    ]
) == [-2, 0, 1, 23]
