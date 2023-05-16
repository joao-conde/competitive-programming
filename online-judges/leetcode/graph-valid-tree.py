# https://leetcode.com/problems/graph-valid-tree/


class Solution:
    def valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        node_edges = dict()
        for i in range(n):
            node_edges[i] = []

        for src, dst in edges:
            node_edges[src].append(dst)
            node_edges[dst].append(src)

        visited = set()

        def has_cycle(node, prev):
            if node in visited:
                return True
            visited.add(node)

            for n in node_edges[node]:
                if n == prev:
                    continue

                if has_cycle(n, node):
                    return True

            return False

        cycles = has_cycle(0, -1)
        return not cycles and len(visited) == n


# Tests
solver = Solution()
assert solver.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
assert solver.valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
