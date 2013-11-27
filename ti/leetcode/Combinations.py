from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class Combinations(LeetcodeProblem):
    def solve(self, n, k):
        return self.combi(n, 1, k)

    def combi(self, n, i, k):
        if n - i + 1 < k:
            return []
        elif k == 0:
            return [[]]
        else:
            res = []
            for j in xrange(i, n + 1):
                res += [[j] + tail for tail in self.combi(n, j + 1, k - 1)]
            return res

    def verify(self, input, s1, s2):
        s1Set = set([tuple(l) for l in s1])
        if len(s1) != len(s1Set):
            return False
        return s1Set == set([tuple(l) for l in s2])

    def input(self):
        from Parser import parseTwoInt
        return parseTwoInt(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = Combinations
