# https://leetcode.com/problems/same-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            return p == q

        left_equal = self.isSameTree(p.left, q.left)
        right_equal = self.isSameTree(p.right, q.right)
        return p.val == q.val and left_equal and right_equal
