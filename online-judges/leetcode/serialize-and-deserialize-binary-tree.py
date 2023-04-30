# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        nodes = dict()

        stack = [(nodes, root, "root")]
        while len(stack) > 0:
            (parent, node, key) = stack.pop()

            val = node.val if node != None else "None"
            dict_key = f"{key};{val}"
            parent[dict_key] = dict()

            if node == None:
                continue

            stack.append((parent[dict_key], node.left, "left"))
            stack.append((parent[dict_key], node.right, "right"))

        return str(nodes)

    def deserialize(self, data: str) -> TreeNode:
        data = data.replace(",", "").replace(":", "").replace("'", "")
        data = data.replace("{", "{ ").replace("}", "} ")
        tokens = data.strip().split(" ")

        dummy = TreeNode(0)
        nodes = [("root", dummy)]
        for token in tokens:
            if token == "":
                continue
            elif token == "{":
                pass
            elif token == "}":
                side, node = nodes.pop()

                if node.val == "None":
                    continue

                if len(nodes) == 0:
                    continue

                _, root = nodes[-1]
                if side == "left":
                    root.left = node
                else:
                    root.right = node
            else:
                side, val = token.split(";")
                node = TreeNode(val)
                nodes.append((side, node))

        return dummy.left if dummy.left != None else dummy.right
