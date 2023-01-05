# https://leetcode.com/problems/removing-stars-from-a-string/


class Solution:
    def removeStars(self, s: str) -> str:
        res, skip = "", 0
        for i in reversed(range(len(s))):
            if s[i] == "*":
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                res = s[i] + res
        return res


# Tests
solver = Solution()
assert solver.removeStars("leet**cod*e") == "lecoe"
assert solver.removeStars("erase*****") == ""
