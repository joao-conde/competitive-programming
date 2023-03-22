# https://leetcode.com/problems/design-hashmap/


class MyHashMap:
    def __init__(self):
        self.map = dict()

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map.get(key, -1)

    def remove(self, key: int) -> None:
        self.map.pop(key, None)


# Tests
map = MyHashMap()
map.put(1, 1)
map.put(2, 2)
assert map.get(1) == 1
assert map.get(3) == -1
map.put(2, 1)
assert map.get(2) == 1
map.remove(2)
assert map.get(2) == -1
