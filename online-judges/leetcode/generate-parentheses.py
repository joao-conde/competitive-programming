# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def helper(n: int, open: int, closed: int, state: str) -> list[str]:
            if open + closed == 2 * n:
                return [state]

            combinations = []
            if open < n:
                combinations.extend(helper(n, open + 1, closed, state + "("))

            if closed < n and closed < open:
                combinations.extend(helper(n, open, closed + 1, state + ")"))

            return combinations

        return helper(n, 1, 0, "(")


# Tests
solver = Solution()
assert solver.generateParenthesis(3) == [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()",
]
assert solver.generateParenthesis(2) == ["(())", "()()"]
assert solver.generateParenthesis(1) == ["()"]
