from collections import deque


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


def preorder(root):
    if root == None:
        return
    print(root, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root, end=" ")
    inorder(root.right)


def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root, end=" ")


def dfs_rec(root):
    if root == None:
        return
    print(root)
    for child in root.children:
        dfs_rec(child)


def dfs(root):
    stack = [root]
    while len(stack) > 0:
        top = stack.pop()
        print(top)
        for child in reversed(top.children):
            if child == None:
                continue
            stack.append(child)


def bfs(root):
    queue = deque([root])
    while len(queue) > 0:
        front = queue.popleft()
        print(front)
        for child in front.children:
            if child == None:
                continue
            queue.append(child)


def height(root):
    if root == None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def main():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    F.left = G


main()
