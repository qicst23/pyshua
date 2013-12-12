from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class PalindromePartitioningII(LeetcodeProblem):
    def solve(self, s):
        n = len(s)
        res = [n - i for i in xrange(n + 1)]

        lastIsP = [True] * n
        for i in xrange(n - 2, -1, -1):
            newIsP = [False] * n
            for j in xrange(i, n):
                if s[i] == s[j] and (j - i < 2 or lastIsP[j - 1]):
                    newIsP[j] = True
                    res[i] = min(res[i], 1 + res[j + 1])
            lastIsP = newIsP

        return res[0] - 1

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = PalindromePartitioningII
