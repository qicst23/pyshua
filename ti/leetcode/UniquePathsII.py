from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class UniquePathsII(LeetcodeProblem):
    def solve(self, obstacleGrid):
        m = len(obstacleGrid)
        if m < 1:
            return 0
        n = len(obstacleGrid[0])
        if m < 1:
            return 0

        lastRow = [0] * n
        seen1 = False
        for i, x in enumerate(obstacleGrid[0]):
            seen1 = (seen1 or x == 1)
            if seen1:
                break
            else:
                lastRow[i] = 1
        firstColumnBlocked = obstacleGrid[0][0] == 1
        i = 1

        while i < m:
            nextRow = [0] * n
            if firstColumnBlocked or obstacleGrid[i][0] == 1:
                firstColumnBlocked = True
                nextRow[0] = 0
            else:
                nextRow[0] = 1

            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    nextRow[j] = 0
                else:
                    nextRow[j] = nextRow[j - 1] + lastRow[j]
            lastRow = nextRow
            i += 1
        return lastRow[-1]

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArrayArrays
        return parseIntArrayArrays(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = UniquePathsII
