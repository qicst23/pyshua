from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class PalindromeNumber(LeetcodeProblem):
    def solve(self, x):
        if x < 0:
            return False

        m = 1
        while x / m >= 10:
            m *= 10

        while x >= 10:
            first = x / m
            last = x % 10
            if first != last:
                return False
            x = (x % m) / 10
            m /= 100

        return True

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = PalindromeNumber
