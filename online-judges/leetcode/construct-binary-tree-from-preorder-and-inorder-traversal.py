# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode(val=preorder[0])

        root_i = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : root_i + 1], inorder[:root_i])
        root.right = self.buildTree(preorder[root_i + 1 :], inorder[root_i + 1 :])

        return root
