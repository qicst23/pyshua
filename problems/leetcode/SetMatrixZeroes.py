from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SetMatrixZeroes(LeetcodeProblem):
    def solve(self, matrix):
        m = len(matrix)
        if m == 0:
            return None
        n = len(matrix[0])
        if n == 0:
            return None

        firstRowZero = False
        for i in xrange(m):
            if matrix[i][0] == 0:
                firstRowZero = True
                break

        firstColZero = False
        for j in xrange(n):
            if matrix[0][j] == 0:
                firstColZero = True
                break

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstRowZero:
            for i in xrange(m):
                matrix[i][0] = 0

        if firstColZero:
            for j in xrange(n):
                matrix[0][j] = 0

        return matrix

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArrayArrays
        return parseIntArrayArrays(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = SetMatrixZeroes
