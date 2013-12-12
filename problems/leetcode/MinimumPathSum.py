from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class MinimumPathSum(LeetcodeProblem):
    def solve(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        res = [0] * n
        s = 0
        for j in xrange(n):
            s += grid[0][j]
            res[j] = s
        i = 1
        while i < m:
            next = [0] * n
            next[0] = res[0] + grid[i][0]
            for j in xrange(1, n):
                next[j] = min(next[j - 1], res[j]) + grid[i][j]
            res = next
            i += 1

        return res[-1]

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArrayArrays
        return parseIntArrayArrays(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = MinimumPathSum
