# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    def is_type(self, val, type):
        try:
            type(val)
            return True
        except:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if self.is_type(token, int):
                stack.append(int(token))
                continue

            op2, op1 = stack.pop(), stack.pop()
            if token == "+":
                stack.append(op1 + op2)
            elif token == "-":
                stack.append(op1 - op2)
            elif token == "*":
                stack.append(op1 * op2)
            elif token == "/":
                stack.append(int(op1 / op2))

        return stack[0]


# Tests
solver = Solution()
# assert solver.evalRPN(["2", "1", "+", "3", "*"]) == 9
# assert solver.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert (
    solver.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
    == 22
)
