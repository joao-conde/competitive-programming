# https://leetcode.com/problems/reorder-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return

        nodes = [head]
        while nodes[-1].next != None:
            nodes.append(nodes[-1].next)

        nodes_len = len(nodes)
        for i in range(nodes_len // 2):
            tmp = nodes[i].next
            nodes[i].next = nodes[nodes_len - i - 1]
            nodes[nodes_len - i - 1].next = tmp

        nodes[nodes_len // 2].next = None
