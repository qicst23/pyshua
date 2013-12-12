from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class Triangle(LeetcodeProblem):
    def solve(self, triangle):
        n = len(triangle)
        minSum = [0]
        i = 0
        while i < n:
            row = triangle[i]
            for j in xrange(i + 1):
                if j == 0:
                    row[j] += minSum[j]
                elif j == i:
                    row[j] += minSum[j - 1]
                else:
                    row[j] += min(minSum[j - 1], minSum[j])
            minSum = row
            i += 1
        return min(minSum)

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArrayArrays
        return parseIntArrayArrays(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = Triangle
