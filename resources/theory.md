# Data Structures

Built-in python data structures and relevant notes:

| Structure | Python            | Relevant Notes                                                                             |
| --------- | ----------------- | ------------------------------------------------------------------------------------------ |
| Vector    | list()            | `append`, `pop`, `insert`, `remove`, `extend`, `index`, `clear`                            |
| HashMap   | dict()            | `d[k]=v`, `d.pop(k)`. CPython uses open addressing and random probing to solve collisions. |
| HashSet   | set()             | `add`, `remove`                                                                            |
| Stack     | list()            |                                                                                            |
| Dequeue   | collections.deque | `rotate`, `append`, `appendleft`, `pop`, `popLeft`, `extend`, `extendLeft`                 |

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

### Binary Tree

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

### Binary Search Tree

- a binary tree where left < root < right
- no certainty regarding tree height, hence:
  - O(H) lookup
  - O(H) insert
  - O(H) delete

```python
class Node:
    def __init__(self, val, left = None, right = None):
        if left != None and right != None:
            assert(left < right)
        self.val = val
        self.left = left
        self.right = right
```

### Balanced Binary Search Tree

- a binary search tree where the height difference between subtrees is at most 1
- the height H is balanced, hence with N nodes height is log N, thus:
  - O(log N) lookup
  - O(log N) insert
  - O(log N) delete

- insertions and deletions possibly make the tree unbalanced

#### AVL Trees

- self-balancing tree after insertions & deletions
- balances itself through rotations

### Trie

- trees of characters
- terminal nodes (leafs) represent words
- allows caching of current prefix and current node for efficient search
- given the prefix length of N:
    - O(N) lookup

## Heap (Max)

- balanced binary tree
- root is bigger than children (recursive definition meaning maximum is at the top)
- insertion is done by inserting new element in the last spot and bubbling it up, swapping with parent if needed
- deletion is done by removing element and replacing by the last element added, swapping it down with the max child
- great for sorting or priority queues

## Disjoint Set

- keeps track of multiple sets of elements, disjoint at first
- allows fast check of disjoint sets of elements
- implemented as a simple array that keeps track of set parents
- `find(x)` should return the set `x` belongs to
- `union(x, y)` should set `x` and `y` to the same set


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
- keep edges sorted by weight in a min heap
- pop them one by one, using those that do not connect two already used vertices
- stop when all vertices are connected
TODO: Missing complexities
TODO some pseudocode with comments

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

- greedy algorithm to find the shortest path between two nodes
- no negative weight edges
TODO some pseudocode with comments

## A*

- dijkstra with an extra heuristic added to the cost
- TODO some pseudocode with comments

## Bellman-Ford

- finds the shortest path between two nodes
- relaxes edges V-1 times, quitting early if no distance improves
- works for negative edges
- does not work with negative cycles but detects them

## Floyd-Warshall

- shortest path between all nodes
- O(V³)

## Cycle Detection
TODO: complexities

Detecting cycles in a graph can be done in several ways:

- DFS: check if a node has been visited twice
- Disjoint Set: union nodes for each edge and quit if same set is found
- Bellman-Ford: run an extra cycle and if it improves there is a cycle
- Tortoise & Hare: if both pointers meet, there is a cycle

## Dynamic Programming

- appliable when optimal solution depends on the optimal solution for subproblems
- bottom-up: solve base cases and compound results (e.g. floyd-warshall)
- top-down: memoization, cache results and avoid recomputation, easily applied to recursive solutions

## Bubble Sort

- bubble biggest element to the top each iteration
- each iteration the ith element is sorted, quitting early if nothing is swapped
- O(N²)

## Quick Sort

- recursively sort halves, partitioned by a pivot
- swap left and right elements of the pivot and call quick sort on both halves
- O(N * log N)

## Merge Sort

- recursively sort halves, call merge sort on each
- copy elements in order to a new array
- O(N * log N)

## Heap Sort

- build an heap
- keep popping the min element into a new array
- O(N * log N)

# Object Oriented Programming (OOP)

TODO examples

**Abstraction** - black-box abstractions that hide implementation details

**Encapsulation** - hide private implementation details, expose a public interface

**Inheritance** - parent/child relationship, inherit data and behavior

**Polymorphism** - uniform usage of objects that share a same interface

## SOLID

TODO examples

**Single Responsibility** - classes should do one thing and do it well, having one reason to change

**Open-Closed** - classes should be open for extension and closed for modifications

**Liskov Substition** - classes should be substituted for parent classes or interfaces they implement

**Interface Segregation** - keep interfaces thin, split big ones into smaller contracts, each client implements what is needed

**Dependency Inversion** - entities depend on abstractions and not on concretions

## Design Patterns

TODO examples

Typical solutions for common software OOP design problems.

**Creational** - objects' creation
  - **Factory** - interface for creating objects, hiding details
  - **Builder** - construct complex objects step by step
  - **Singleton** - ensure a single instance of this class

**Structural** - objects' assembly
  - **Adapter** - allow objects with incompatible interfaces to communicate
  - **Decorator** - wrap objects with additional functionality

**Behavioral** - objects' communication
  - **Command** - turns actions into objects (e.g. useful for queues, delays, undo/redo, event sourcing, ...)
  - **Observer** - subscription/notification of objects to events
  - **Strategy** - define a family of interchangeable algorithms