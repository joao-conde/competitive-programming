# https://www.lintcode.com/problem/659/


class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


# Tests
solver = Solution()

strs = ["3#strlonger", "##hardoneright", "123onlynumbers", "you"]
encoded = solver.encode(strs)
decoded = solver.decode(encoded)
assert isinstance(encoded, str) == True
assert decoded == strs

strs = ["lint", "code", "love", "you"]
encoded = solver.encode(strs)
decoded = solver.decode(encoded)
assert isinstance(encoded, str) == True
assert decoded == strs

strs = ["we", "say", ":", "yes"]
encoded = solver.encode(strs)
decoded = solver.decode(encoded)
assert isinstance(encoded, str) == True
assert decoded == strs

strs = ["we", "sa;y", ";", ";yes", "semi;"]
encoded = solver.encode(strs)
decoded = solver.decode(encoded)
assert isinstance(encoded, str) == True
assert decoded == strs

strs = ["we\;\\;\\\;", "sa;y", ";", ";yes", "semi;"]
encoded = solver.encode(strs)
decoded = solver.decode(encoded)
assert isinstance(encoded, str) == True
assert decoded == strs
