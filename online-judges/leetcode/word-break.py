# https://leetcode.com/problems/word-break/


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


# Tests
solver = Solution()
assert solver.wordBreak("leetcode", ["leet", "code"]) == True
assert solver.wordBreak("applepenapple", ["apple", "pen"]) == True
assert solver.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
assert solver.wordBreak("aaaaaaa", ["aaaa", "aa"]) == False
assert solver.wordBreak("bb", ["a", "b", "bbb", "bbbb"]) == True
