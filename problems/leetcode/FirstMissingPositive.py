from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class FirstMissingPositive(LeetcodeProblem):
    def solve(self, a):
        n = len(a)

        for i, x in enumerate(a):
            if x <= 0:
                a[i] = n + 2

        for i in xrange(n):
            x = abs(a[i])
            if 0 < x <= n:
                a[x - 1] = -abs(a[x - 1])

        for i, x in enumerate(a):
            if x >= 0:
                return i + 1

        return n + 1

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = FirstMissingPositive
