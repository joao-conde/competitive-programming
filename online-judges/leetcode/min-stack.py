# https://leetcode.com/problems/min-stack/


class MinStack:
    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        topmin = self.getMin()
        topmin = min(topmin, val) if topmin != None else val
        self.values.append(val)
        self.values.append(topmin)

    def pop(self) -> None:
        self.values.pop()
        self.values.pop()

    def top(self) -> int:
        return self.values[-2] if len(self.values) > 0 else None

    def getMin(self) -> int:
        return self.values[-1] if len(self.values) > 0 else None


# Tests
minstack = MinStack()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)
assert minstack.getMin() == -3
minstack.pop()
assert minstack.top() == 0
assert minstack.getMin() == -2
