from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class RegularExpressionMatching(LeetcodeProblem):
    def solve(self, s, p):
        return self.match(s, len(s), 0, p, len(p), 0)

    def match(self, s, m, i, p, n, j):
        if j == n:
            return i == m

        if j + 1 < n and p[j + 1] == '*':
            if self.match(s, m, i, p, n, j + 2):
                return True
            while i < m:
                if p[j] == s[i] or p[j] == '.':
                    i += 1
                    if self.match(s, m, i, p, n, j + 2):
                        return True
                else:
                    return False

            return False
        else:
            if i < m:
                return (
                    (p[j] == s[i] or p[j] == '.') and
                    (self.match(s, m, i + 1, p, n, j + 1))
                )

            else:
                return False

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoStrings
        return parseTwoStrings(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = RegularExpressionMatching
