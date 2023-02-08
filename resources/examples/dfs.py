def dfs_rec(root):
    if root == None:
        return
    print(root)
    for child in root.children:
        dfs_rec(child)


def dfs(root):
    stack = [root]
    while len(stack) > 0:
        top = stack.pop()
        print(top)
        for child in reversed(top.children):
            if child == None:
                continue
            stack.append(child)


def has_cycle(root):
    visited = set()
    stack = [root]
    while len(stack) > 0:
        top = stack.pop()

        if top in visited:
            return True

        for child in reversed(top.children):
            if child == None:
                continue
            stack.append(child)

    return False
