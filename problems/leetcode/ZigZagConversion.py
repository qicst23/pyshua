from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ZigZagConversion(LeetcodeProblem):
    def solve(self, s, nRows):
        if nRows == 1:
            return s

        n = len(s)
        compoSize = 2 * (nRows - 1)

        res = []

        i = 0
        while i < n:
            res.append(s[i])
            i += compoSize

        for j in xrange(1, nRows - 1):
            i = j
            while i < n:
                res.append(s[i])
                if i + compoSize - 2 * j < n:
                    res.append(s[i + compoSize - 2 * j])
                i += compoSize

        i = nRows - 1
        while i < n:
            res.append(s[i])
            i += compoSize

        return ''.join(map(str, res))

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseStringAndInt
        return parseStringAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseString
        for o in parseString(open(self.outputPath)):
            yield o[0]

problem = ZigZagConversion
