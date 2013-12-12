from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class EditDistance(LeetcodeProblem):
    def solve(self, word1, word2):
        m = len(word1)
        n = len(word2)
        res = range(n + 1)
        i = 1
        while i < m + 1:
            next = [0] * (n + 1)
            next[0] = i
            for j in xrange(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    next[j] = res[j - 1]
                else:
                    next[j] = min(res[j - 1], res[j], next[j - 1]) + 1
            res = next
            i += 1

        return res[-1]

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseTwoStrings
        return parseTwoStrings(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = EditDistance
