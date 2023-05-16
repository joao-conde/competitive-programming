# https://leetcode.com/problems/minimum-window-substring/


class Solution:
    def fulfilled(self, counts, window):
        for c in counts:
            if window.get(c, 0) < counts[c]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_counts = dict()
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1

        si, sj, found = 0, len(s), False
        i, j = 0, 0
        window = dict()
        while j < len(s):
            window[s[j]] = window.get(s[j], 0) + 1

            while self.fulfilled(t_counts, window):
                if (j - i + 1) < (sj - si + 1):
                    found = True
                    si = i
                    sj = j

                window[s[i]] -= 1
                i += 1

            j += 1

        return s[si : sj + 1] if found else ""


# Tests
solver = Solution()
assert solver.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert solver.minWindow("a", "a") == "a"
assert solver.minWindow("a", "aa") == ""
