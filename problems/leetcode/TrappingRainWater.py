from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class TrappingRainWater(LeetcodeProblem):
    def solve(self, a):
        n = len(a)
        if n == 0:
            return 0

        m = 0
        left = [0] * n
        for i in xrange(n):
            if a[i] > m:
                m = a[i]
            left[i] = m

        res = 0
        m = 0
        right = 0
        for i in xrange(n - 1, -1, -1):
            if a[i] > m:
                m = a[i]
            right = m
            res += min(left[i], right) - a[i]

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

problem = TrappingRainWater
