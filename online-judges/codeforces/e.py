s = input()
modulo = 10**9 + 7

i = 1
ways = 1
while i < len(s) - 1:
    if s[i] == "m" or s[i] == "w":
        ways = 0
        break

    if s[i - 1] == "u" and s[i] == "u":
        ways = 2 * ways

    if s[i - 1] == "n" and s[i] == "n":
        ways = 2 * ways

    ways %= modulo
    i += 1

print(ways)
