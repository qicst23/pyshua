from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class MaximalRectangle(LeetcodeProblem):
    def solve(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0

        lastZero = -1
        for j in xrange(n):
            if matrix[0][j] == '1':
                matrix[0][j] = j - lastZero
            else:
                matrix[0][j] = j - lastZero - 1
                lastZero = j
        print 20, matrix
        lastZero = -1 if matrix[0][0] == 1 else 0
        for i in xrange(1, m):
            if matrix[i][0] in '1':
                matrix[i][0] = i - lastZero
            else:
                matrix[i][0] = i - lastZero - 1
                lastZero = i
        print 28, matrix
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    matrix[i][j] = min(
                        [
                            matrix[i - 1][j - 1],
                            matrix[i][j - 1],
                            matrix[i - 1][j]
                        ]
                    ) + 1
                else:
                    matrix[i][j] = 0

        return max([max(row) for row in matrix])

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseStringArray
        for o in parseStringArray(open(self.inputPath)):
            yield [list(s) for s in o[0]],

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = MaximalRectangle
