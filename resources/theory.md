# Data Structures

*Disclaimer: example source code might not compile/execute properly*

Built-in python data structures and relevant notes:

| Structure      | Python                                     | Relevant Notes                                                                             |
| -------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Vector         | list()                                     | `append`, `pop`, `insert`, `remove`, `extend`, `index`, `clear`                            |
| HashMap        | dict(), collections.defaultdict(lambda: 0) | `d[k]=v`, `d.pop(k)`. CPython uses open addressing and random probing to solve collisions. |
| HashSet        | set()                                      | `add`, `update`, `remove`, `clear`, `union`, `intersection`                                |
| Stack          | list()                                     |                                                                                            |
| Dequeue        | collections.deque                          | `rotate`, `append`, `appendleft`, `pop`, `popleft`, `extend`, `extendleft`                 |
| Priority Queue | heapq                                      | `heapify`, `heappush`, `heappop`, `nlargest`, `nsmallest`                                  |

| Function (Python)                          | Relevant Notes                                    |
| ------------------------------------------ | ------------------------------------------------- |
| sorted(iterable, key=key, reverse=reverse) | Ascending sort of an iterable collection          |
| reversed(sequence)                         | Reverses a sequence (lists, strings, tuples, ...) |
| bin(number)                                | Binary string representation of a number          |

## Tree

- acyclic graph (root + children)
- given the height of tree as H:
  - O(H) lookup
  - O(H) insert
  - O(H) delete

```python
class Node:
    def __init__(self, val, children = []):
        self.val = val
        self.children = children
```

## Binary Tree

- a tree with at most 2 children
- no certainty regarding tree height, hence:
  - O(H) lookup
  - O(H) insert
  - O(H) delete

```python
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
```

## Binary Search Tree

- a binary tree where left < root < right
- no certainty regarding tree height, hence:
  - O(H) lookup
  - O(H) insert
  - O(H) delete

```python
class Node:
    def __init__(self, val, left = None, right = None):
        if left: assert(left.val < val)
        if right: assert(val <= right.val)

        self.val = val
        self.left = left
        self.right = right
```

## Balanced Binary Search Tree

- a binary search tree where the height difference between subtrees is at most 1
- the height H is balanced, hence with N nodes height is log N, thus:
  - O(log N) lookup
  - O(log N) insert
  - O(log N) delete

- insertions and deletions possibly make the tree unbalanced, self-balancing trees correct this through rotations (e.g. AVL)

```python
class Node:
    def __init__(self, val, left = None, right = None):
        if left: assert(left.val <= val)
        if right: assert(val <= right.val)
        if left and right: assert(abs(left.height() - right.height()) <= 1)

        self.val = val
        self.left = left
        self.right = right

    def height(self):
        left_h = self.left.height() if self.left else 0
        right_h = self.right.height() if self.right else 0
        return max(left_h, right_h) + 1
```

## Trie

- trees of characters
- terminal nodes (leaves) represent words
- allows caching of current prefix and current node for efficient search
- given the prefix length of K:
    - O(K) lookup

```python
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
```

## Heap (Max)

- balanced binary tree
- root is bigger than children (recursive definition meaning maximum is at the top)
- insertion is done by inserting new element in the last spot and bubbling it up, swapping with parent if needed
- deletion is done by removing element and replacing by the last element added, swapping it down with the max child
- great for sorting or priority queues
- balanced binary tree:
  - O(log N) insertions/deletions
  - O(1) query max

## Disjoint Set

- keeps track of multiple sets of elements, disjoint at first
- allows fast check of disjoint sets of elements
- implemented as a simple array that keeps track of set parents
- `union(x, y)` should set `x` and `y` to the same set (O(1))
- `find(x)` should return the set `x` belongs to (O(N))
  - can be made O(log N) if we track the size and chain to the smallest, guaranteeing at max log N length of each chain

```python
groups = list(range(length))

def find(x):
    while x != groups[x]:
        x = groups[x]
    return x

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    groups[root_x] = root_y
```

## Graph

- collection of vertices (V) and edges (E)
- adjacency matrix representation (good for dense graphs): V * V matrix with distances (0, inf, x)
- adjacency list representation (good for sparse graphs): list of lists of neighbors

# Algorithms

Example tree:

```
        A
      /   \         
    B      C
   / \     /
  D  E   F
        /
       G 
```

## Tree Traversal

| Method    | Order               | Example       |
| --------- | ------------------- | ------------- |
| Pre (dfs) | **root** left right | A B D E C F G |
| In        | left **root** right | D B E A G F C |
| Post      | left right **root** | D E B G F C A |

```python
def preorder(root):
    if root == None: return
    print(root)
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root == None: return
    inorder(root.left)
    print(root)
    inorder(root.right)


def postorder(root):
    if root == None: return
    postorder(root.left)
    postorder(root.right)
    print(root)
```

## Minimum Spanning Tree (MST)

- a tree that contains all nodes of the original one with a minimal sum of edge weights

### Kruskal's Algorithm

- select minimum cost edges that do not form a cycle
- pop them one by one, using those that do not connect two already used vertices (disjoint set)
- stop when all vertices are connected

```python
def kruskal(edges):
    edges.sort()

    mst = []
    while len(edges) > 0:
        cost, src, dst = edges.pop(0)

        # disjoint set keeps track of connectivity
        if find(src) != find(dst):
            union(src, dst)
            mst.append((cost, src, dst))

    return mst
```

## Binary Search

- cut the search space in half each iteration (logarithmic complexity)
- requires a sorted collection and monotonicity
- O(log N)

```python
lb, ub = 0, len(nums) - 1
while lb <= ub:
    mid = lb + (ub - lb) // 2
    if nums[mid] < target:
        lb = mid + 1
    elif nums[mid] > target:
        ub = mid - 1
    else:
        return mid
```

## Depth-First Search (DFS)

- LIFO approach
- search leftmost first, backtracking when needed
- useful to detect graph cycles too
- O(V)
- example: A B D E C F G (tree pre-order)

```python
# recursive
def dfs(root):
    if root == None: return
    print(root)
    for child in root.children:
        dfs(child)


# stack based
def dfs(root):
    stack = [root]
    while len(stack) > 0:
        top = stack.pop()
        print(top)
        for child in reversed(top.children):
            if child == None: continue
            stack.append(child)
```

## Breadth-First Search (BFS)

- FIFO approach
- explore all nodes in a "level" before going deeper
- O(V)
- example: A B C D E F G

```python
from collections import deque

def bfs(root):
    queue = deque([root])
    while len(queue) > 0:
        front = queue.popleft()
        print(front)
        for child in front.children:
            if child == None: continue
            queue.append(child)
```

## Dijkstra

- greedy algorithm to find the shortest path from one node to all others
- no negative weight edges allowed
- O((V + E) log V) with min-heap:
  - heappush once per edge -> E log V
  - heappop once per node -> V log V

```python
from heapq import heappush, heappop

def dijkstra(graph, src, dst):
    dists = [float("inf")] * len(graph)
    dists[src] = 0

    visited = set()
    pq = [(0, src)]
    while len(pq) > 0:
        (_, cur) = heappop(pq)

        if cur in visited:
            continue
        visited.add(cur)

        # for each neighbor check if the cost of going
        # from current to neighbor is lower than neighbor distance
        for (neighbor, cost) in enumerate(graph[cur]):
            alt = dists[cur] + cost
            if alt < dists[neighbor]:
                dists[neighbor] = alt
            heappush(pq, (dists[neighbor], neighbor))

    return dists[dst]
```

## Bellman-Ford

- finds the shortest path between two nodes
- relaxes edges V-1 times, quitting early if no distance improves
- works for negative edges
- does not work with negative cycles but detects them

```python
def bellman_ford(graph, src, dst):
    n_vertices = len(graph)

    dists = [float("inf")] * n_vertices
    dists[src] = 0

    for _ in range(n_vertices - 1):
        # for each neighbor check if the cost of going
        # from current to neighbor is lower than neighbor distance
        for i in range(n_vertices):
            for j in range(n_vertices):
                alt = dists[i] + graph[i][j]
                if alt < dists[j]:
                    dists[j] = alt

    return dists[dst]
```

## Floyd-Warshall

- shortest path between all nodes
- O(V³)

## Cycle Detection

Detecting cycles in a graph can be done in several ways:

- DFS: check if a node has been visited twice
- Disjoint Set: union nodes for each edge and quit if same set is found
- Bellman-Ford: run an extra cycle and if it improves there is a cycle
- Tortoise & Hare: if both pointers meet, there is a cycle

## Dynamic Programming

- appliable when optimal solution depends on the optimal solution for subproblems
- bottom-up: solve base cases and compound results
- top-down: memoization, cache results and avoid recomputation, easily applied to recursive solutions

## Quick Sort

- recursively sort halves, partitioned by a pivot
- swap left and right elements of the pivot and call quick sort on both halves
- O(N * log N)

## Merge Sort

- recursively sort halves, call merge sort on each
- copy elements in order to a new array
- O(N * log N)

## Heap Sort

- build an heap (heapify O(N))
- keep popping the min element into a new array
- O(N * log N):
  - the popped top element will be replaced by a leaf and bubbled down

```python
from heapq import heapify, heappush, heappop

def heapsort(collection):
    heapify(collection)
    return [heappop(collection) for _ in range(len(collection))]
```

# Object Oriented Programming (OOP)

**Abstraction** - black-box abstractions that hide implementation details

**Encapsulation** - hide private implementation details, expose a public interface

**Inheritance** - parent/child relationship, inherit data and behavior

**Polymorphism** - uniform usage of objects that share a same interface

## SOLID

**Single Responsibility** - classes should do one thing and do it well, having one reason to change

**Open-Closed** - classes should be open for extension and closed for modifications

**Liskov Substition** - classes should be substituted for parent classes or interfaces they implement

**Interface Segregation** - keep interfaces thin, split big ones into smaller contracts, each client implements what is needed

**Dependency Inversion** - entities depend on abstractions and not on concretions

## Design Patterns

https://www.youtube.com/watch?v=tAuRQs_d9F8

Typical solutions for common software OOP design problems.

**Creational** - objects' creation

  - **Factory** - interface for creating objects, simplifying and centralizing logic

```python
class Honda:
    def __init__(self, model): pass
    def drive(self): pass

class BMW:
    def __init__(self, model, premium): pass
    def drive(self): pass

class Ferrari:
    def __init__(self, model, super): pass
    def drive(self): pass

class CarFactory:
    @classmethod
    def build(cls, brand, model, **kwargs):
        if brand == "honda": return Honda(model)
        if brand == "bmw": return BMW(model, kwargs.get("premium", True))
        if brand == "ferrari": return Ferrari(model, kwargs.get("super", True))
```

  - **Builder** - construct complex objects step by step

```python
class House:
    def __init__(self): pass

    def with_walls(self, nwalls):
        self.nwalls = nwalls
        return self

    def with_roof(self):
        self.roof = True
        return self

house = House()
house = house.with_walls(3).with_roof()
```

  - **Singleton** - ensure a single instance of a class

```python
class Singleton:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
```

**Structural** - objects' assembly

  - **Adapter** - allow objects with incompatible interfaces to communicate

  - **Decorator** - wrap objects with additional functionality

**Behavioral** - objects' communication

  - **Command** - turns actions into objects (e.g. useful for queues, delays, undo/redo, event sourcing, ...)
  
  - **Observer** - subscription/notification of objects to events

  - **Strategy** - define a family of interchangeable algorithms