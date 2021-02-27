# https://leetcode.com/problems/count-sorted-vowel-strings/
class Solution:
    VOWELS = ["a", "e", "i", "o", "u"]

    CACHE = dict()

    def countVowelStrings(self, n):
        return sum([self.count(n, vowel) for vowel in self.VOWELS])

    def count(self, n, char):
        if (n, char) in self.CACHE: return self.CACHE[(n, char)]

        if n == 1: return 1
        valid = [vowel for vowel in self.VOWELS if vowel >= char]
        result = sum([self.count(n - 1, char) for char in valid])

        self.CACHE[(n, char)] = result
        return result

# Tests
solver = Solution()
assert(solver.countVowelStrings(1) == 5)
assert(solver.countVowelStrings(2) == 15)
assert(solver.countVowelStrings(33) == 66045)
assert(solver.countVowelStrings(50) == 316251)
