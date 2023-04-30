# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from collections import heappush, nsmallest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []

        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node == None:
                continue

            heappush(nodes, (node.val, node))
            stack.append(node.left)
            stack.append(node.right)

        val, _ = nsmallest(k, nodes)[-1]
        return val
