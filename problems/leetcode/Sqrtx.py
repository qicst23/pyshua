from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class Sqrtx(LeetcodeProblem):
    def solve(self, x):
        if x <= 1:
            return x

        low = 1
        high = x
        while low <= high:
            middle = low + (high - low) / 2

            if x / middle >= middle and x / (middle + 1) < (middle + 1):
                return middle
            elif x / middle < middle:
                high = middle - 1
            else:
                low = middle + 1

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = Sqrtx
