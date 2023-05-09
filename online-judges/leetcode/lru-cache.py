# https://leetcode.com/problems/find-median-from-data-stream/


class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = dict()

        self.head = LRUCache.Node("head", "head")
        self.tail = LRUCache.Node("tail", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.nodes.get(key, None)
        if node:
            self._refresh(node)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.nodes.get(key, None)
        node = node or LRUCache.Node(key, value)
        node.val = value
        self.nodes[key] = node
        self._refresh(node)
        self._resize()

    def _refresh(self, node):
        first = self.head.next
        if node == first:
            return

        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if first:
            first.prev = node

        self.head.next = node

        node.prev = self.head
        node.next = first

    def _resize(self):
        size = len(self.nodes)
        if size <= self.capacity:
            return

        last = self.tail.prev
        if last == self.head:
            return

        self.tail.prev = last.prev
        last.prev.next = self.tail
        self.nodes.pop(last.key)


# Tests
lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
assert lru_cache.get(1) == 1
lru_cache.put(3, 3)
assert lru_cache.get(2) == -1
lru_cache.put(4, 4)
assert lru_cache.get(1) == -1
assert lru_cache.get(3) == 3
assert lru_cache.get(4) == 4

lru_cache = LRUCache(1)
lru_cache.put(2, 1)
assert lru_cache.get(2) == 1
lru_cache.put(3, 2)
assert lru_cache.get(2) == -1
assert lru_cache.get(3) == 2

lru_cache = LRUCache(3)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
lru_cache.put(3, 3)
lru_cache.put(4, 4)
assert lru_cache.get(4) == 4
assert lru_cache.get(3) == 3
assert lru_cache.get(2) == 2
assert lru_cache.get(1) == -1
lru_cache.put(5, 5)
assert lru_cache.get(1) == -1
assert lru_cache.get(2) == 2
assert lru_cache.get(3) == 3
assert lru_cache.get(4) == -1
assert lru_cache.get(5) == 5
