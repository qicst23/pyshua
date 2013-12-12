from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class PlusOne(LeetcodeProblem):
    def solve(self, digits):
        plusOne = 1
        n = len(digits)
        for i in reversed(xrange(n)):
            digits[i] += plusOne
            plusOne = digits[i] / 10
            digits[i] %= 10

        if plusOne:
            digits.insert(0, 1)

        return digits

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = PlusOne
