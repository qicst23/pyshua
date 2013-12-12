from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ReverseInteger(LeetcodeProblem):
    def solve(self, x):
        if x < 0:
            return -self.solve(-x)

        res = 0
        while x:
            res = res * 10 + x % 10
            x /= 10

        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = ReverseInteger
