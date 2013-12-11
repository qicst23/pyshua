from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class RotateImage(LeetcodeProblem):
    def solve(self, matrix):
        n = len(matrix)

        for i in xrange(n / 2):
            self.rotate(matrix, i, n)

        return matrix

    def rotate(self, matrix, i, n):
        for k in xrange(0, n - 2 * i - 1):
            temp = matrix[n - 1 - i - k][i]
            matrix[n - 1 - i - k][i] = matrix[n - 1 - i][n - 1 - i - k]
            matrix[n - 1 - i][n - 1 - i - k] = matrix[i + k][n - 1 - i]
            matrix[i + k][n - 1 - i] = matrix[i][i + k]
            matrix[i][i + k] = temp

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArrayArrays
        return parseIntArrayArrays(open(self.inputPath))

    def output(self):
        from Parser import parseIntArrayArrays
        for o in parseIntArrayArrays(open(self.outputPath)):
            yield o[0]

problem = RotateImage
