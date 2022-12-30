# https://leetcode.com/problems/happy-number/


class Solution:
    # def isHappy(self, n: int, seen=None) -> bool:
    #     if n == 1:
    #         return True

    #     seen = seen or set()
    #     if n in seen:
    #         return False
    #     seen.add(n)

    #     next = sum([int(c) ** 2 for c in str(n)])
    #     return self.isHappy(next, seen=seen)

    def isHappy(self, n: int) -> bool:
        def next_n(n):
            return sum([int(c) ** 2 for c in str(n)])

        slow, fast = next_n(n), next_n(next_n(n))
        while slow != fast:
            slow = next_n(slow)
            fast = next_n(next_n(fast))

        return slow == fast == 1


# Tests
solver = Solution()
assert solver.isHappy(19) == True
assert solver.isHappy(2) == False
