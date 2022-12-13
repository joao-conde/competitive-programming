import math

sqrts = dict()


def computeSqrts(x):
    if x in sqrts:
        return sqrts[x]
    if not float(x).is_integer():
        return []
    sqrts[x] = [x] + computeSqrts(math.sqrt(x))
    return sqrts[x]


def maxSetSize(riceBags):
    sets = []

    options = set(riceBags)
    for bag in riceBags:
        sqrts = computeSqrts(bag)
        sqrts = [s for s in computeSqrts(bag) if s in options]
        sets.append(sqrts)

    perfect_len = max([len(s) for s in sets])
    return perfect_len if perfect_len >= 2 else -1


assert maxSetSize([3, 9, 4, 2, 16]) == 3
assert maxSetSize([625, 4, 2, 5, 25]) == 3
assert maxSetSize([7, 4, 8, 9]) == -1
