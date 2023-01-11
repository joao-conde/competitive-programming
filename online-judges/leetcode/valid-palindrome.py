# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        left, right = 0, length - 1

        while left < right:
            while left < length and not s[left].isalnum():
                left += 1

            while right >= 0 and not s[right].isalnum():
                right -= 1

            if left < length and right >= 0 and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# Tests
solver = Solution()
assert solver.isPalindrome("A man, a plan, a canal: Panama") == True
assert solver.isPalindrome("race a car") == False
assert solver.isPalindrome(" ") == True
assert solver.isPalindrome(".,") == True
assert solver.isPalindrome("0P") == False
