# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        tortoise, hare = head, head.next
        while hare:
            tortoise = tortoise.next
            hare = hare.next.next if hare.next != None else None

        return tortoise


# Tests
solver = Solution()

nums = [1, 2, 3, 4, 5]
nodes = [ListNode(val=n) for n in nums]
for i, node in enumerate(nodes[:-1]):
    node.next = nodes[i + 1]
assert solver.middleNode(nodes[0]) == nodes[2]

nums = [1, 2, 3, 4, 5, 6]
nodes = [ListNode(val=n) for n in nums]
for i, node in enumerate(nodes[:-1]):
    node.next = nodes[i + 1]
assert solver.middleNode(nodes[0]) == nodes[3]

node = ListNode(val=1)
assert solver.middleNode(node) == node
