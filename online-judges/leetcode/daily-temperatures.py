# https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            if i == 0:
                stack.append((0, temperature))
                continue

            while True and len(stack) > 0:
                top_i, top_t = stack[-1]
                if temperature <= top_t:
                    break

                answer[top_i] = i - top_i
                stack.pop()

            stack.append((i, temperature))

        return answer


# Tests
solver = Solution()
assert solver.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
    1,
    1,
    4,
    2,
    1,
    1,
    0,
    0,
]
assert solver.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert solver.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
