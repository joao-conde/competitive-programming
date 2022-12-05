# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        first, last = None, None
        current1, current2 = l1, l2
        while current1 or current2:
            sum = (
                (current1.val if current1 else 0)
                + (current2.val if current2 else 0)
                + carry
            )
            carry = sum // 10
            remainder = sum % 10

            new = ListNode(val=remainder)
            if not first:
                first = new
            if last:
                last.next = new
            last = new

            current1 = current1.next if current1 else None
            current2 = current2.next if current2 else None

        if carry:
            new = ListNode(val=carry)
            last.next = new
            last = new

        return first
