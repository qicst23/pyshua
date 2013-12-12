from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class PascalsTriangle(LeetcodeProblem):
    def solve(self, rowIndex):
        res = []
        level = 0

        while level < rowIndex:
            if res:
                last = res[-1]
                n = len(last)
                next = [1] * n
                for i in xrange(n - 1):
                    next[i + 1] = last[i] + last[i + 1]
                next.append(1)
            else:
                next = [1]

            res.append(next)
            level += 1
        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = PascalsTriangle
