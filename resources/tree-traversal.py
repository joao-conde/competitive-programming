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
