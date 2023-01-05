from collections import deque


def bfs(root):
    queue = deque([root])
    while len(queue) > 0:
        front = queue.popleft()
        print(front)
        for child in front.children:
            if child == None:
                continue
            queue.append(child)