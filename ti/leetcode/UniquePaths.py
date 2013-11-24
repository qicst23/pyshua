from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class UniquePaths(LeetcodeProblem):
    def solve(self, m, n):
        if m < 1 or n < 1:
            return 0

        lastRow = [1] * n
        i = 1

        while i < m:
            nextRow = [0] * n
            nextRow[0] = 1
            for j in xrange(1, n):
                nextRow[j] = nextRow[j - 1] + lastRow[j]
            lastRow = nextRow
            i += 1
        return lastRow[-1]

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoInt
        return parseTwoInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = UniquePaths
