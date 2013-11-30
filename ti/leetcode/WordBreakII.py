from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class WordBreakII(LeetcodeProblem):
    def solve(self, s, dict):
        cache = {}
        res = self.go(s, len(s), 0, dict, cache)
        for solution in res:
            solution.reverse()
        return [' '.join(solution) for solution in res]

    def go(self, s, l, i, dict, cache):
        if i in cache:
            return cache[i]
        else:
            res = []
            if i == l:
                res = [[]]
            else:
                for j in xrange(i, l):
                    word = s[i:j + 1]
                    if word in dict:
                        tailSolutions = self.go(s, l, j + 1, dict, cache)
                        if tailSolutions:
                            newSolutions = [
                                solution + [word] for solution in tailSolutions
                            ]
                            res += newSolutions
            cache[i] = res
            return res

    def verify(self, input, s1, s2):
        s1Set = set([tuple(l) for l in s1])
        if len(s1) != len(s1Set):
            return False
        return s1Set == set([tuple(l) for l in s2])

    def input(self):
        from Parser import parseStringAndStringArray
        return parseStringAndStringArray(open(self.inputPath))

    def output(self):
        from Parser import parseStringArray
        for o in parseStringArray(open(self.outputPath)):
            yield o[0]

problem = WordBreakII
