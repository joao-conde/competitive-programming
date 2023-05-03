# https://leetcode.com/problems/binary-tree-maximum-path-sum/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal maximum
            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            maximum = max(maximum, left_max + node.val + right_max)

            best_path = node.val + max(left_max, right_max)
            return best_path

        maximum = root.val
        dfs(root)
        return maximum
