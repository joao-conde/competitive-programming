def decode(s, i, cache):
    if i >= len(s):
        return 1

    if i in cache:
        return cache[i]

    ways = 1
    for j in range(i, len(s) - 1):
        if s[j] == "u" and s[j + 1] == "u":
            ways += decode(s, j + 2, cache) % (10**9 + 7)
        elif s[j] == "n" and s[j + 1] == "n":
            ways += decode(s, j + 2, cache) % (10**9 + 7)
        elif s[j] == "m" or s[j] == "w" or s[j + 1] == "m" or s[j + 1] == "w":
            return 0

    cache[i] = ways % (10**9 + 7)
    return cache[i]


s = input()
print(decode(s, 0, dict()))
