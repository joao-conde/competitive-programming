class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

    @property
    def children(self):
        return [self.left, self.right]


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


# def dfs(root):
#     if root == None: return
#     print(root)
#     for child in root.children:
#         dfs(child)


def dfs(root):
    stack = [root]
    while len(stack) > 0:
        top = stack.pop()
        print(top)
        for child in reversed(top.children):
            if child == None:
                continue
            stack.append(child)


from collections import deque
def bfs(root):
    queue = deque([root])
    while len(queue) > 0:
        front = queue.popleft()
        print(front)
        for child in front.children:
            if child == None: continue
            queue.append(child)


bfs(A)
