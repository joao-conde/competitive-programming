# https://leetcode.com/problems/maximum-width-of-binary-tree/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        width = 0
        queue = deque([(0, root)])
        while len(queue) > 0:
            level = []

            width = max(width, queue[-1][0] - queue[0][0] + 1)

            while len(queue) > 0:
                (i, node) = queue.popleft()
                if node == None:
                    continue

                if node.left != None:
                    level.append((2 * i, node.left))

                if node.right != None:
                    level.append((2 * i + 1, node.right))

            queue.extend(level)

        return width
