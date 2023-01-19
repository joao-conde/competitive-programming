# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0

        def dfs_max_diam(node):
            if node == None:
                return 0

            left_h = dfs_max_diam(node.left)
            right_h = dfs_max_diam(node.right)

            nonlocal diam
            diam = max(diam, left_h + right_h)

            return 1 + max(left_h, right_h)

        dfs_max_diam(root)
        return diam
