# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        max_bf = 0

        def dfs_max_bf(node):
            if node == None:
                return 0

            left_h = dfs_max_bf(node.left)
            right_h = dfs_max_bf(node.right)

            nonlocal max_bf
            max_bf = max(max_bf, abs(left_h - right_h))

            return 1 + max(left_h, right_h)

        dfs_max_bf(root)
        return max_bf <= 1
