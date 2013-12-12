from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class Powxn(LeetcodeProblem):
    def solve(self, x, n):
        if n < 0:
            return self.solve(1 / x, -n)

        return round(self.pow(1, x, n), 5)

    def pow(self, res, base, n):
        if n == 0:
            return res
        else:
            if n % 2 == 0:
                return self.pow(res, base * base, n / 2)
            else:
                return self.pow(res * base, base, n - 1)

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneFloatAndOneInt
        return parseOneFloatAndOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneFloat
        for o in parseOneFloat(open(self.outputPath)):
            yield o[0]

problem = Powxn
