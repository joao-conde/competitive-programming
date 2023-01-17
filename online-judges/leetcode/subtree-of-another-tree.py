# https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left == None or right == None:
            return left == right

        left_equals = self.isSameTree(left.left, right.left)
        right_equals = self.isSameTree(left.right, right.right)
        return left.val == right.val and left_equals and right_equals

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes = [root]
        while len(nodes) > 0:
            node = nodes.pop()

            if self.isSameTree(node, subRoot):
                return True

            if node.left:
                nodes.append(node.left)

            if node.right:
                nodes.append(node.right)

        return False
