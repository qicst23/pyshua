from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class Candy(LeetcodeProblem):
    def solve(self, ratings):
        n = len(ratings)
        candys = [0] * n
        for i, x in enumerate(ratings):
            if i > 0 and x > ratings[i - 1]:
                candys[i] = candys[i - 1] + 1
            else:
                candys[i] = 1

        for i in xrange(n - 2, -1, -1):
            x = ratings[i]
            if i < n - 1 and x > ratings[i + 1] and candys[i] <= candys[i + 1]:
                candys[i] = candys[i + 1] + 1

        return sum(candys)

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = Candy
