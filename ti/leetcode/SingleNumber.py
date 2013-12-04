from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class SingleNumber(LeetcodeProblem):
    def solve(self, a):
        res = a[0]
        n = len(a)
        for i in xrange(1, n):
            res ^= a[i]

        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = SingleNumber
