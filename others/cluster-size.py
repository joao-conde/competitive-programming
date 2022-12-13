def findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax):
    n = len(processingPower)
    i, j, maxK = 0, 0, 0
    pp = processingPower[0]

    while i < n and j < n:

        # TODO: ran out of time but one has to keep the bootingPowers
        # as a sliding window aggregation computed on element
        # addition and eviction instead of recomputing in each cycle
        # otherwise this won't be fast enough for large inputs
        bootingPowers = [b for (i, b) in enumerate(bootingPower) if i >= i and i <= j]

        k = j - i + 1
        windowPower = max(bootingPowers) + pp * k

        if windowPower > powerMax:
            pp -= processingPower[i]
            i += 1
        else:
            if maxK < k:
                maxK = k
            j += 1
            if j < n:
                pp += processingPower[j]

    return maxK


assert findMaximumSustainableClusterSize([2, 1, 3, 4, 5], [3, 6, 1, 3, 4], 25) == 3
assert findMaximumSustainableClusterSize([4, 1, 4, 5, 3], [8, 8, 10, 9, 12], 33) == 2
assert findMaximumSustainableClusterSize([10, 8, 7], [11, 12, 19], 6) == 0
