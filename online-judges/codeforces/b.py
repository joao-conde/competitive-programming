t = int(input())

for _ in range(t):
    m, s = [int(x) for x in input().split()]
    found = [int(x) for x in input().split()]

    found.sort()

    i = 0
    prev = 0
    added = 0
    while i < len(found):
        if found[i] != prev + 1:
            added += prev + 1
        else:
            i += 1
        prev += 1

    while added < s:
        prev += 1
        added += prev

    if added == s:
        print("YES")
    else:
        print("NO")
