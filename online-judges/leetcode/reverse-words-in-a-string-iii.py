# https://leetcode.com/problems/reverse-words-in-a-string-iii/

from typing import List


class Solution:
    def reverseWord(self, s: str) -> str:
        s_list = list(s)
        i, j = 0, len(s_list) - 1
        while i < j:
            tmp = s_list[i]
            s_list[i] = s_list[j]
            s_list[j] = tmp
            i += 1
            j -= 1
        return "".join(s_list)

    def reverseWords(self, s: str) -> str:
        reverse = [self.reverseWord(word) for word in s.split(" ")]
        return " ".join(reverse)


# Tests
solver = Solution()
assert (
    solver.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
)
assert solver.reverseWords("God Ding") == "doG gniD"
