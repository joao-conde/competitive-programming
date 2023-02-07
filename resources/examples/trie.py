class Trie:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.terminal = True

    def remove(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                break
            cur = cur.children[c]
        cur.terminal = False

    def search(self, word) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.terminal


# Tests
trie = Trie()
assert trie.search("hell") == False
assert trie.search("hello") == False

trie.insert("hell")
assert trie.search("hell") == True
assert trie.search("hello") == False

trie.insert("hello")
assert trie.search("hell") == True
assert trie.search("hello") == True

assert trie.search("linkedlist") == False
assert trie.search("tree") == False
assert trie.search("trie") == False

trie.insert("linkedlist")
trie.insert("tree")
trie.insert("trie")
assert trie.search("hell") == True
assert trie.search("hello") == True
assert trie.search("linkedlist") == True
assert trie.search("tree") == True
assert trie.search("trie") == True

trie.remove("hell")
assert trie.search("hell") == False
assert trie.search("hello") == True
assert trie.search("linkedlist") == True
assert trie.search("tree") == True
assert trie.search("trie") == True

trie.remove("hello")
assert trie.search("hell") == False
assert trie.search("hello") == False
assert trie.search("linkedlist") == True
assert trie.search("tree") == True
assert trie.search("trie") == True

trie.remove("hello")
trie.remove("linkedlist")
trie.remove("tree")
trie.remove("trie")
assert trie.search("hell") == False
assert trie.search("hello") == False
assert trie.search("linkedlist") == False
assert trie.search("tree") == False
assert trie.search("trie") == False
