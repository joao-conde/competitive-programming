# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional["Node"]) -> Optional["Node"]:
        if root == None:
            return None

        levels = dict()
        dq = deque([(root, 0)])
        while len(dq) > 0:
            (cur, level) = dq.popleft()
            if cur == None:
                continue

            levels[level] = levels.get(level, []) + [cur]
            dq.append((cur.left, level + 1))
            dq.append((cur.right, level + 1))

        for level, nodes in levels.items():
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]

        return root
