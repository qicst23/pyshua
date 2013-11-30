from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class BestTimetoBuyandSellStockIII(LeetcodeProblem):
    def solve(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        first = [0] * n
        m = prices[0]
        p = 0
        for i in xrange(1, n - 1):
            x = prices[i]
            if x - m > p:
                p = x - m
            if x < m:
                m = x
            first[i] = p

        m = prices[n - 1]
        res = 0
        for i in xrange(n - 2, -1, -1):
            x = prices[i]
            if first[i] + (m - x) > res:
                res = first[i] + (m - x)
            if m < x:
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

problem = BestTimetoBuyandSellStockIII
