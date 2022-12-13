def countGroups(related):
    union_find = list(range(len(related)))

    def find(x):
        while x != union_find[x]:
            x = union_find[x]
        return x

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        union_find[root_i] = root_j

    for i in range(len(related)):
        for j in range(len(related[i])):
            if related[i][j] == "1":
                union(i, j)

    groups = [find(x) for x in union_find]
    return len(set(groups))


assert countGroups(["1100", "1110", "0110", "0001"]) == 2
assert countGroups(["10000", "01000", "00100", "00010", "00001"]) == 5
