# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


# Tests
solver = Solution()
assert solver.minPartitions("32") == 3
assert solver.minPartitions("82734") == 8
assert solver.minPartitions("27346209830709182346") == 9
