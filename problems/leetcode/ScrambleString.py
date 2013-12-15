from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ScrambleString(LeetcodeProblem):
    def solve(self, s1, s2):
        m = len(s1)
        n = len(s2)

        if m != n:
            return False

        r = [[[False for i in range(m)] for j in range(m)] for k in range(m)]

        for i in xrange(m):
            for j in xrange(m):
                r[0][i][j] = s1[i] == s2[j]

        # length is k + 1, start from i in s1, from j in s2
        for k in xrange(1, m):
            for i in xrange(m - k):
                for j in xrange(m - k):
                    for l in xrange(1, k + 1):
                        if (
                            r[l - 1][i][j] and r[k - l][i + l][j + l] or
                            r[k - l][i][j + l] and r[l - 1][i + k - l + 1][j]
                        ):
                            r[k][i][j] = True
                            break

        return r[-1][0][0]

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoStrings
        return parseTwoStrings(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = ScrambleString
