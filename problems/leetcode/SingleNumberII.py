from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SingleNumberII(LeetcodeProblem):
    def solve(self, a):
        record = [0] * 32
        sign = 0
        for n in a:
            if n < 0:
                sign += 1
                n = -n
            i = 0
            while n:
                if n & 1:
                    record[i] += 1
                i += 1
                n >>= 1
            for i in xrange(32):
                record[i] %= 3
            sign %= 3

        res = 0
        m = 1
        for b in record:
            res += b * m
            m *= 2
        return -res if sign else res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = SingleNumberII
