# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        window = []
        while cur:
            window.append(cur)
            if len(window) > n + 1:
                window.pop(0)
            cur = cur.next

        # we want to pop the first element
        before = window[0]
        if len(window) == n:
            return head.next

        if before.next:
            before.next = before.next.next
        return head


# Tests


def buildListNums(head: ListNode) -> list[int]:
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums


def buildList(nums: list[int]) -> ListNode:
    nodes = [ListNode(val=n) for n in nums]
    for i, node in enumerate(nodes[:-1]):
        node.next = nodes[i + 1]
    return nodes[0]


solver = Solution()

solution = solver.removeNthFromEnd(buildList([1, 2, 3, 4, 5]), 2)
assert buildListNums(solution) == [1, 2, 3, 5]

solution = solver.removeNthFromEnd(buildList([1, 2]), 1)
assert buildListNums(solution) == [1]

solution = solver.removeNthFromEnd(buildList([1, 2]), 2)
assert buildListNums(solution) == [2]

solution = solver.removeNthFromEnd(buildList([1]), 1)
assert solution == None
