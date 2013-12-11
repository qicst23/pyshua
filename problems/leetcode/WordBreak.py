from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class WordBreak(LeetcodeProblem):
    def solve(self, s, dict):
        n = len(s)
        self.cache = {}
        return self.find(s, n, 0, dict)

    def find(self, s, n, i, dict):
        if i in self.cache:
            return self.cache[i]

        res = False
        if n == i:
            res = True
        else:
            for j in xrange(i, n):
                if s[i:j + 1] in dict:
                    if self.find(s, n, j + 1, dict):
                        res = True
                        break
        self.cache[i] = res
        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseStringAndStringArray
        return parseStringAndStringArray(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = WordBreak
