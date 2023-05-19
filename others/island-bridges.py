from collections import deque


def min_bridge(map):
    rows, cols = len(map), len(map[0])

    dq = deque()
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == "R":
                dq.append((i, j, 0))

    visited = set()
    while len(dq) > 0:
        cur_i, cur_j, length = dq.popleft()

        if map[cur_i][cur_j] == "B":
            return length - 1

        if (cur_i, cur_j) in visited:
            continue
        visited.add((cur_i, cur_j))

        if cur_i + 1 < rows:
            dq.append((cur_i + 1, cur_j, length + 1))

        if cur_i > 0:
            dq.append((cur_i - 1, cur_j, length + 1))

        if cur_j + 1 < cols:
            dq.append((cur_i, cur_j + 1, length + 1))

        if cur_j > 0:
            dq.append((cur_i, cur_j - 1, length + 1))

    return -1


assert min_bridge([".RB...", "R....B", "R.....", ".....R"]) == 0
assert min_bridge([".R....", "R....B", "R.....", "......"]) == 4
assert min_bridge([".BB...", ".....B", "......", ".....R"]) == 1
assert min_bridge([".RR...", "R....R", "R.....", ".....R"]) == -1
assert min_bridge([".BB...", ".....B", "......", ".....B"]) == -1
assert min_bridge(["......", "......", "......", "......"]) == -1
