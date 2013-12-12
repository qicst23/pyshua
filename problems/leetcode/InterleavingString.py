from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class InterleavingString(LeetcodeProblem):
    def solve(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if l != m + n:
            return False

        res = [False] * (n + 1)
        res[0] = True
        for j in xrange(1, n + 1):
            res[j] = res[j - 1] and s2[j - 1] == s3[j - 1]
        i = 1
        while i < m + 1:
            next = [False] * (n + 1)
            next[0] = res[0] and s1[i - 1] == s3[i - 1]
            for j in xrange(1, n + 1):
                next[j] = (
                    next[j - 1] and s2[j - 1] == s3[i + j - 1]
                ) or (
                    res[j] and s1[i - 1] == s3[i + j - 1]
                )
            res = next
            i += 1

        return res[-1]

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseThreeStrings
        return parseThreeStrings(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = InterleavingString
