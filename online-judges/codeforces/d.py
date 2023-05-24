t = int(input())

for _ in range(t):
    n, h = [int(x) for x in input().split()]
    attacks = [int(x) for x in input().split()]

    lb = 1
    ub = h
    while lb < ub:
        k = lb + (ub - lb) // 2

        last = 0
        damage = 0
        for a in attacks:
            if a > last:
                damage += k
            else:
                damage += k - (last - a + 1)

            last = a + k - 1

        if damage < h:
            lb = k + 1
        elif damage >= h:
            ub = k

    print(ub)
