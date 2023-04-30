# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        tokens = []

        def preorder(node):
            nonlocal tokens

            if node == None:
                tokens.append("N")
                return
            tokens.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        print(",".join(tokens))
        return ",".join(tokens)

    def deserialize(self, data: str) -> TreeNode:
        tokens = data.split(",")
        i = 0

        def preorder():
            nonlocal i, tokens

            i += 1
            if tokens[i - 1] == "N":
                return None
            node = TreeNode(int(tokens[i - 1]))
            node.left = preorder()
            node.right = preorder()
            return node

        root = preorder()
        return root
