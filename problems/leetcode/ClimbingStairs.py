from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ClimbingStairs(LeetcodeProblem):
    def solve(self, n):
        last = 0
        res = 1
        for i in xrange(n):
            next = res + last
            last = res
            res = next
        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = ClimbingStairs
