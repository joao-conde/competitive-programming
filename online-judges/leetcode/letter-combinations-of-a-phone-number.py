# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    KEYS = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(Solution.KEYS[digits[0]])

        combinations = []
        for c in Solution.KEYS[digits[0]]:
            for combination in self.letterCombinations(digits[1:]):
                combinations.append(c + combination)
        return combinations


# Tests
solver = Solution()
assert solver.letterCombinations("23") == [
    "ad",
    "ae",
    "af",
    "bd",
    "be",
    "bf",
    "cd",
    "ce",
    "cf",
]
assert solver.letterCombinations("") == []
assert solver.letterCombinations("2") == ["a", "b", "c"]
