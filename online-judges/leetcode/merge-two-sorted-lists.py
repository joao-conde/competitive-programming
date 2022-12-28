# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 == None:
            return list2

        if list2 == None:
            return list1

        root = ListNode()
        cur, cur1, cur2 = root, list1, list2
        while cur1 or cur2:
            if cur1 == None:
                cur.next = cur2
                cur2 = cur2.next

            elif cur2 == None:
                cur.next = cur1
                cur1 = cur1.next

            elif cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next

            elif cur2.val < cur1.val:
                cur.next = cur2
                cur2 = cur2.next

            cur = cur.next

        return root.next
