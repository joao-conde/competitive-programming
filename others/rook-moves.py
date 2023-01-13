def longest_rook_path(matrix):
    n, m = len(matrix), len(matrix[0])
    longest = []

    cache = dict()
    for i in range(n):
        for j in range(m):
            path = longest_path(matrix, i, j, [], cache)
            if len(path) > len(longest):
                longest = path
    return longest


def longest_path(matrix, si, sj, path, cache):
    n, m = len(matrix), len(matrix[0])

    if (si, sj) in cache:
        return cache[(si, sj)]

    path.append((si, sj))

    max_row = []
    for j in range(m):
        if matrix[si][j] > matrix[si][sj]:
            max_row.append((si, j))

    max_col = []
    for i in range(n):
        if matrix[i][sj] > matrix[si][sj]:
            max_col.append((i, sj))

    positions = max_row + max_col
    if len(positions) == 0:
        return path

    answer = []
    subpaths = [longest_path(matrix, i, j, path[:], cache) for (i, j) in positions]
    for subpath in subpaths:
        if len(subpath) > len(answer):
            answer = subpath

    cache[(si, sj)] = answer
    return cache[(si, sj)]


assert longest_rook_path(
    [
        [7, -3, 11, 13],
        [-7, 39, 2, 30],
        [36, -2, -9, 8],
        [24, -12, -10, -5],
    ]
) == [(0, 0), (0, 2), (0, 3), (1, 3), (1, 1)]
