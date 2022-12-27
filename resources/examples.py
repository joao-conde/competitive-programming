class Node:
    def __init__(self, val, left=None, right=None):
        if left:
            assert left <= val
        if right:
            assert val <= right

        self.val = val
        self.left = left
        self.right = right

    def height(self):
        left_h = self.left.height() if self.left else 0
        right_h = self.right.height() if self.right else 0
        return max(left_h, right_h) + 1


def height(root):
    if root == None:
        return 0
    return max(height(root.left), height(root.right)) + 1
