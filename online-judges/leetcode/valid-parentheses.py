# https://leetcode.com/problems/valid-parentheses/


class Solution:
    MATCH = {"(": ")", "{": "}", "[": "]"}

    def isValid(self, s: str) -> bool:
        open = self.MATCH.keys()
        stack = list()
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if self.MATCH[p] != c:
                    return False
        return len(stack) == 0


# Tests
solver = Solution()
assert solver.isValid("") == True
assert solver.isValid("()") == True
assert solver.isValid("()[]{}") == True
assert solver.isValid("([{}])") == True
assert solver.isValid("(]") == False
