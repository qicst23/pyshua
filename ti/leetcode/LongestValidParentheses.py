from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class LongestValidParentheses(LeetcodeProblem):
    def solve(self, s):
        res = 0
        left = 0
        count = 0
        accum = 0
        for c in s:
            if c == '(':
                left += 1
                count = 0
            else:
                if left > 0:
                    left -= 1
                    count = 1
                else:
                    if accum > res:
                        res = accum
                    count = 0
                    accum = 0
            accum += count
        if accum > res:
            res = accum
        return res * 2

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseString
        return parseString(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = LongestValidParentheses
