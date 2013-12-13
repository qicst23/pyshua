from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class DecodeWays(LeetcodeProblem):
    def solve(self, s):
        if not s:
            return 0
        return self.decode(s, len(s), 0, {})

    def decode(self, s, n, i, cache):
        if i in cache:
            return cache[i]

        res = 0
        if i == n:
            res = 1
        elif i < n:
            c = s[i]
            if c == '0':
                res = 0
            else:
                if i == n - 1:
                    res = 1
                else:
                    res = self.decode(s, n, i + 1, cache)
                    if c == '1' or (c == '2' and ord(s[i + 1]) <= ord('6')):
                        res += self.decode(s, n, i + 2, cache)

        cache[i] = res
        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = DecodeWays
