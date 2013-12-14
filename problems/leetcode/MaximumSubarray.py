from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class MaximumSubarray(LeetcodeProblem):
    def solve(self, a):
        res = -float('inf')
        s = 0
        for x in a:
            s += x
            if res < s:
                res = s
            if s < 0:
                s = 0

        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = MaximumSubarray
