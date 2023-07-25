from collections import defaultdict


def string_groups(strings):
    groups = defaultdict(lambda: set())

    for s in strings:
        sorted_s = str(sorted(s))
        groups[sorted_s].add(s)

    return [list(g) for g in groups.values()]


# [["241", "124", "412"], ["524", "425"], ["324"], ["2141"]]
string_groups(
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
string_groups(
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
