# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()

        tail = dummy
        while len(lists) > 0:
            cur = 0
            for i in range(len(lists)):
                if lists[i] == None or lists[cur] == None:
                    continue
                if lists[i].val < lists[cur].val:
                    cur = i

            if lists[cur] == None:
                lists.pop(cur)
                continue

            tail.next = lists[cur]
            tail = tail.next

            lists[cur] = lists[cur].next
            if lists[cur] == None:
                lists.pop(cur)

        return dummy.next
