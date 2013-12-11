from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class JumpGameII(LeetcodeProblem):
    def solve(self, a):
        r = 0
        m = 0
        res = 0
        for i, x in enumerate(a):
            if i > r:
                r = m
                res += 1
            m = max(m, i + x)
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

problem = JumpGameII
