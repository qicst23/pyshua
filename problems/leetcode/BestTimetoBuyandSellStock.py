from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class BestTimetoBuyandSellStock(LeetcodeProblem):
    def solve(self, prices):
        if not prices:
            return 0

        n = len(prices)
        m = prices[0]
        res = 0
        for i in xrange(1, n):
            x = prices[i]
            p = x - m
            if res < p:
                res = p
            if x < m:
                m = x
        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = BestTimetoBuyandSellStock
