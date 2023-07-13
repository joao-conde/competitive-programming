def bracketsGame(s):
    i = 0
    j = len(s) - 1

    score = 0
    while i < j:
        while s[i] != "(":
            i += 1

        while s[j] != ")":
            j -= 1

        if i >= j:
            break

        score += j - i
        i += 1
        j -= 1

    return score


assert bracketsGame("()()") == 3
assert bracketsGame("(()") == 2
assert bracketsGame("(())") == 4
