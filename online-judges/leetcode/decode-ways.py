# https://leetcode.com/problems/decode-ways/


class Solution:
    def decodings(self, s, i, cache):
        if i in cache:
            return cache[i]

        if i == len(s):
            return 1

        if s[i] == "0":
            return 0

        result = self.decodings(s, i + 1, cache)

        val = int(s[i] + s[i + 1]) if i + 1 < len(s) else -1
        if val >= 1 and val <= 26:
            result += self.decodings(s, i + 2, cache)

        cache[i] = result
        return result

    def numDecodings(self, s: str) -> int:
        result = self.decodings(s, 0, dict())
        return result


# Tests
solver = Solution()
assert solver.numDecodings("12") == 2
assert solver.numDecodings("226") == 3
assert solver.numDecodings("06") == 0
assert solver.numDecodings("27") == 1
assert (
    solver.numDecodings("111111111111111111111111111111111111111111111") == 1836311903
)
