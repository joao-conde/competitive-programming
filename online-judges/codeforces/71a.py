# https://codeforces.com/problemset/problem/71/A

n = int(input())

for _ in range(n):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word) - 2) + word[-1])
