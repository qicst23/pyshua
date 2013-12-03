from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class PascalsTriangleII(LeetcodeProblem):
    def solve(self, rowIndex):
        res = [1]
        level = 0

        while level < rowIndex:
            for i in xrange(len(res) - 1, 0, -1):
                res[i] += res[i - 1]
            res.append(1)
            level += 1

        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = PascalsTriangleII
