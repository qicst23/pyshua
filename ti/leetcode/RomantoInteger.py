from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class RomantoInteger(LeetcodeProblem):
    def solve(self, s):
        n = len(s)
        if n == 0:
            return 0

        self.table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        last = self.ctoi(s[0])
        res += last

        for i in xrange(1, n):
            cur = self.ctoi(s[i])
            if last < cur:
                res = res - last + (cur - last)
            else:
                res += cur
            last = cur

        return res

    def ctoi(self, c):
        return self.table[c]

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = RomantoInteger
