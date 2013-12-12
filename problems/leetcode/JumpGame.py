from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class JumpGame(LeetcodeProblem):
    def solve(self, a):
        r = 0
        for i, x in enumerate(a):
            if i > r:
                return False
            else:
                if r < i + x:
                    r = i + x

        return True

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = JumpGame
