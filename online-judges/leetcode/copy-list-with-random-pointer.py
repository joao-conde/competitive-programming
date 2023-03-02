# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        root = None

        new, nodes = None, dict()
        while head != None:
            if head not in nodes:
                nodes[head] = Node(head.val)

            if head.next and head.next not in nodes:
                nodes[head.next] = Node(head.next.val)

            if head.random and head.random not in nodes:
                nodes[head.random] = Node(head.random.val)

            new = nodes[head]
            new.next = nodes[head.next] if head.next else None
            new.random = nodes[head.random] if head.random else None

            if not root:
                root = new

            head = head.next

        return root
