from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class PermutationSequence(LeetcodeProblem):
    def solve(self, n, k):
        res = []
        m = 1
        i = 1
        while i < n:
            m *= i
            i += 1

        digits = range(1, n + 1)
        for i in xrange(n):
            l = (k - 1) / m + 1
            d = self.take(digits, l)
            res.append(d)
            digits[d - 1] = '*'
            k -= (l - 1) * m
            if i < n - 1:
                m /= n - 1 - i

        return ''.join(map(str, res))

    def take(self, digits, l):
        i = 0
        for d in digits:
            if d != '*':
                i += 1
            if i == l:
                return d
        return -1

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoInt
        return parseTwoInt(open(self.inputPath))

    def output(self):
        from Parser import parseString
        for o in parseString(open(self.outputPath)):
            yield o[0]

problem = PermutationSequence
