from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class DistinctSubsequences(LeetcodeProblem):
    def solve(self, s, t):
        self.cache = {}
        return self.go(s, len(s), 0, t, len(t), 0)

    def go(self, s, m, i, t, n, j):
        if (i, j) in self.cache:
            return self.cache[(i, j)]

        if m - i < n - j:
            res = 0
        elif j == n:
            res = 1
        else:
            res = sum(
                [
                    self.go(
                        s, m, k + 1, t, n, j + 1
                    ) for k in xrange(i, m) if s[k] == t[j]
                ]
            )

        self.cache[(i, j)] = res
        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoStrings
        return parseTwoStrings(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = DistinctSubsequences
