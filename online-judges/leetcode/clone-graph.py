# https://leetcode.com/problems/clone-graph/


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node == None:
            return None

        clones = dict()

        to_clone = [node]
        while len(to_clone) > 0:
            top = to_clone.pop()
            if top.val in clones:
                continue

            clones[top.val] = Node(val=top.val)

            to_clone.extend(top.neighbors)

        connected = set()
        to_connect = [node]
        while len(to_connect) > 0:
            top = to_connect.pop()
            cloned = clones[top.val]
            if cloned.val in connected:
                continue

            for neighbor in top.neighbors:
                cloned.neighbors.append(clones[neighbor.val])
            connected.add(cloned.val)
            to_connect.extend(top.neighbors)

        return clones[node.val]
