# https://leetcode.com/problems/letter-case-permutation/


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        if len(s) == 1:
            return [s.upper(), s.lower()] if s.isalpha() else [s]

        permutations = set()
        for i in range(len(s)):
            for perm in self.letterCasePermutation(s[i + 1 :]):
                if s[i].isalpha():
                    permutations.add(s[:i] + s[i].swapcase() + perm)
                permutations.add(s[: i + 1] + perm)

        return list(permutations)


# Tests
solver = Solution()
print(solver.letterCasePermutation("a1b2"))
print(solver.letterCasePermutation("3z4"))
print(solver.letterCasePermutation("C"))
print(solver.letterCasePermutation("0"))
print(solver.letterCasePermutation("12345"))
