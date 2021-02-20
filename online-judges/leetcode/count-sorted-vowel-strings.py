# https://leetcode.com/problems/count-sorted-vowel-strings/
class Solution:
    VOWELS = ["a", "e", "i", "o", "u"]
    
    cache = dict()

    def countVowelStrings(self, n):
        return self.count(n, 'a') + self.count(n, 'e') + self.count(n, 'i') + self.count(n, 'o') + self.count(n, 'u')

    def count(self, n, char):
        if (n, char) in self.cache: return self.cache[(n, char)]

        if n == 1: return 1
        valid = [vowel for vowel in self.VOWELS if vowel >= char]
        result = sum([self.count(n - 1, char) for char in valid])

        self.cache[(n, char)] = result
        return result

# Tests
solver = Solution()
assert(solver.countVowelStrings(1) == 5)
assert(solver.countVowelStrings(2) == 15)
assert(solver.countVowelStrings(33) == 66045)
assert(solver.countVowelStrings(50) == 316251)
