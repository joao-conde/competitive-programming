# https://leetcode.com/problems/design-add-and-search-words-data-structure/


class Trie:
    def __init__(self) -> None:
        self.terminal = False
        self.children = dict()


class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.terminal = True

    def search(self, word: str) -> bool:
        return self.search_dfs(self.root, word)

    def search_dfs(self, cur: Trie, word: str) -> bool:
        if len(word) == 0:
            return cur.terminal

        c = word[0]
        if c == ".":
            terminal = False
            for child in cur.children.values():
                terminal = terminal or self.search_dfs(child, word[1:])
            return terminal

        if c not in cur.children:
            return False

        return self.search_dfs(cur.children[c], word[1:])


# Tests
word_dict = WordDictionary()
word_dict.addWord("bad")
word_dict.addWord("dad")
word_dict.addWord("mad")
assert word_dict.search("pad") == False
assert word_dict.search("bad") == True
assert word_dict.search(".ad") == True
assert word_dict.search("b..") == True
