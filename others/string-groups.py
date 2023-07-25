from collections import defaultdict


def string_groups_1(strings):
    groups = defaultdict(lambda: set())

    for s in strings:
        sorted_s = str(sorted(s))
        groups[sorted_s].add(s)

    return [list(g) for g in groups.values()]


def string_groups_2(strings):
    groups = defaultdict(lambda: set())

    for s in strings:
        counts = defaultdict(lambda: 0)
        for c in s:
            counts[c] += 1
        groups[tuple(counts)].add(s)

    return [list(g) for g in groups.values()]


# [["241", "124", "412"], ["524", "425"], ["324"], ["2141"]]
string_groups_1(
    [
        "124",
        "412",
        "425",
        "241",
        "524",
        "324",
        "2141",
    ]
)
string_groups_2(
    [
        "124",
        "412",
        "425",
        "241",
        "524",
        "324",
        "2141",
    ]
)

# [["cba", "bca", "abc"], ["c"], ["cc"], ["dc"], ["cdd"]]
string_groups_1(
    [
        "abc",
        "bca",
        "cba",
        "c",
        "cc",
        "dc",
        "cdd",
    ]
)
string_groups_2(
    [
        "abc",
        "bca",
        "cba",
        "c",
        "cc",
        "dc",
        "cdd",
    ]
)
