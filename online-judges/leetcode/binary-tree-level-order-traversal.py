# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        order = []

        dq = deque([[root]])
        while len(dq) > 0:
            level = dq.popleft()

            order.append([n.val for n in level])

            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            if len(next_level) > 0:
                dq.append(next_level)

        return order
