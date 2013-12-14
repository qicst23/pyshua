from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class WildcardMatching(LeetcodeProblem):
    def solve(self, s, p):
        i = 0
        j = 0
        m = len(s)
        n = len(p)
        i_backup = -1
        j_backup = -1
        while i < m:
            if j < n and p[j] == '*':
                if p[j] == '*':
                    while j < n and p[j] == '*':
                        j += 1
                    if j == n:
                        return True
                    i_backup = i
                    j_backup = j
            elif j < n and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            else:
                if i_backup >= 0:
                    i_backup += 1
                    i = i_backup
                    j = j_backup
                else:
                    return False

        while j < n and p[j] == '*':
            j += 1

        return True if j == n else False

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoStrings
        return parseTwoStrings(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = WildcardMatching
