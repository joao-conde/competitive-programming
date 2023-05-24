t = int(input())

for _ in range(t):
    a, b, k = [int(x) for x in input().split()]

    if k % 2 == 0:
        print((k // 2) * (a - b))
    else:
        print(((k - 1) // 2) * (a - b) + a)
