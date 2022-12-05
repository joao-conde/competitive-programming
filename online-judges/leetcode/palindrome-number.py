# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        y = 0
        while n > 0:
            y *= 10
            y += n % 10
            n //= 10
        return x == y


# Tests
solver = Solution()
assert solver.isPalindrome(121) == True
assert solver.isPalindrome(-121) == False
assert solver.isPalindrome(10) == False
