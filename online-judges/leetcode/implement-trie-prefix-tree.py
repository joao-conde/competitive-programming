# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieNode:
    def __init__(self, val, terminal=False):
        self.val = val
        self.terminal = terminal
        self.children = []


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        i, last = self._find(word)
        for c in word[i:]:
            child = TrieNode(c)
            last.children.append(child)
            last = child
        last.terminal = True

    def search(self, word: str) -> bool:
        i, last = self._find(word)
        return i == len(word) and last.terminal

    def startsWith(self, prefix: str) -> bool:
        i, last = self._find(prefix)
        return i == len(prefix)

    def _find(self, word: str) -> tuple[int, TrieNode]:
        i, cur = 0, self.root
        while i < len(word) and cur:
            possible = [c for c in cur.children if c.val == word[i]]

            if len(possible) == 0:
                break

            i += 1
            cur = possible[0]

        return i, cur


# Tests
trie = Trie()
trie.insert("apple")
assert trie.search("apple") == True
assert trie.search("app") == False
assert trie.startsWith("app") == True
trie.insert("app")
assert trie.search("app") == True
