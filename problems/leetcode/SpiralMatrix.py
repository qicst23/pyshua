from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SpiralMatrix(LeetcodeProblem):
    def solve(self, matrix):
        res = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []

        left = 0
        right = n - 1
        top = 0
        down = m - 1
        while left < right and top < down:
            self.fill(matrix, left, right, top, down, res)
            left += 1
            right -= 1
            top += 1
            down -= 1

        if left == right:
            for i in xrange(top, down + 1):
                res.append(matrix[i][left])
        elif top == down:
            for i in xrange(left, right + 1):
                res.append(matrix[top][i])

        return res

    def fill(self, matrix, left, right, top, down, res):
        for i in xrange(left, right):
            res.append(matrix[top][i])
        for i in xrange(top, down):
            res.append(matrix[i][right])
        for i in xrange(right, left, -1):
            res.append(matrix[down][i])
        for i in xrange(down, top, -1):
            res.append(matrix[i][left])

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArrayArrays
        return parseIntArrayArrays(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = SpiralMatrix
