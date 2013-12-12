from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SpiralMatrixII(LeetcodeProblem):
    def solve(self, n):
        if n == 0:
            return []

        res = [[1] * n for i in xrange(n)]
        i = 1
        left = 0
        right = n - 1
        top = 0
        down = n - 1
        while left < right and top < down:
            i = self.fill(res, left, right, top, down, i)
            left += 1
            right -= 1
            top += 1
            down -= 1

        if left <= right:
            for j in xrange(left, right + 1):
                res[top][j] = i
                i += 1

        return res

    def fill(self, res, left, right, top, down, i):
        for j in xrange(left, right):
            res[top][j] = i
            i += 1
        for j in xrange(top, down):
            res[j][right] = i
            i += 1
        for j in xrange(right, left, -1):
            res[down][j] = i
            i += 1
        for j in xrange(down, top, -1):
            res[j][left] = i
            i += 1
        return i

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = SpiralMatrixII
