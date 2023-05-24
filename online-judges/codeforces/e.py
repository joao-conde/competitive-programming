s = input()
modulo = 10**9 + 7

dp = [1] * len(s)

for i in range(1, len(s)):
    if s[i] == "m" or s[i] == "w":
        dp[-1] = 0
        break
    if s[i] == "u" and s[i - 1] == "u":
        dp[i] = dp[i - 2] + dp[i - 1]
    elif s[i] == "n" and s[i - 1] == "n":
        dp[i] = dp[i - 2] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]

print(dp[-1])
