# https://leetcode.com/problems/first-bad-version/


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lb, ub = 1, n

        while lb < ub:
            mid = lb + (ub - lb) // 2
            if isBadVersion(mid):
                ub = mid
            else:
                lb = mid + 1
        return ub


# Tests
def isBadVersion(version: int) -> bool:
    if version <= 3:
        return False
    return True


solver = Solution()
assert solver.firstBadVersion(5) == 4
