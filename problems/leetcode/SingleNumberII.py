from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SingleNumberII(LeetcodeProblem):
    def solve(self, a):
        return min(minSum)

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = SingleNumberII
