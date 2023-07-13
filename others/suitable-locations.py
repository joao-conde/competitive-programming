def suitableLocations(center, d):
    center.sort()

    # left and right bounds given by our centers expanded
    # by distance / 2 since we have to pick up and come back
    min_x = center[0] - d // 2
    max_x = center[-1] + d // 2
    nxs = len(center)

    locations = 0

    for x in range(center[nxs // 2] + 1, max_x + 1):
        total = 0
        for c in center:
            total += abs(x - c) * 2
            if total > d:
                break
        if total > d:
            break
        locations += 1

    for x in range(center[nxs // 2], min_x - 1, -1):
        total = 0
        for c in center:
            total += abs(x - c) * 2
            if total > d:
                break
        if total > d:
            break
        locations += 1

    return locations


assert suitableLocations([2, 0, 3, -4], 22) == 5
assert suitableLocations([-3, 2, 2], 8) == 0
