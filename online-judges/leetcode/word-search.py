# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def matches(board, i, j, word, used):
            if len(word) == 0:
                return True

            if (i, j) in used:
                return False

            if i < 0 or i >= len(board):
                return False

            if j < 0 or j >= len(board[i]):
                return False

            if board[i][j] != word[0]:
                return False

            used.add((i, j))
            neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            return any(
                [
                    matches(board, ni, nj, word[1:], used.copy())
                    for (ni, nj) in neighbors
                ]
            )

        # reverse string if the last character is less frequent to reduce branching
        freqs = dict()
        for i in range(len(board)):
            for j in range(len(board[i])):
                freqs[board[i][j]] = freqs.get(board[i][j], 0) + 1
        if freqs.get(word[0], 0) < freqs.get(word[-1], 0):
            word = word[::-1]

        # ensure there is enough of each character
        word_freqs = dict()
        for c in word:
            word_freqs[c] = word_freqs.get(c, 0) + 1
        for k, v in word_freqs.items():
            if freqs.get(k, 0) < v:
                return False

        # test all starting points
        for i in range(len(board)):
            for j in range(len(board[i])):
                used = set()
                if matches(board, i, j, word, used):
                    return True
        return False


# Tests
solver = Solution()
assert (
    solver.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
    == True
)
assert (
    solver.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
    )
    == True
)
assert (
    solver.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    )
    == False
)
assert solver.exist([["a"]], "a") == True
assert solver.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB") == True
assert (
    solver.exist(
        [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"
    )
    == True
)
assert (
    solver.exist(
        [
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "B"],
            ["A", "A", "A", "A", "B", "A"],
        ],
        "AAAAAAAAAAAAABB",
    )
    == False
)
assert (
    solver.exist(
        [["a"]],
        "ab",
    )
    == False
)
assert (
    solver.exist(
        [
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
        ],
        "BAAAAAAAAAAAAAA",
    )
    == False
)
