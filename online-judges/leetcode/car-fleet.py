# https://leetcode.com/problems/car-fleet/


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed))
        arrivals = [(target - p) / s for p, s in cars]

        mono_stack = []
        for t in reversed(arrivals):
            mono_stack.append(t)
            if len(mono_stack) == 1:
                continue

            if mono_stack[-1] <= mono_stack[-2]:
                mono_stack.pop()

        return len(mono_stack)


# Tests
solver = Solution()
assert solver.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
assert solver.carFleet(10, [3], [3]) == 1
assert solver.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
assert solver.carFleet(10, [0, 4, 2], [2, 1, 3]) == 1
