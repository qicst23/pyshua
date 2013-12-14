from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class NQueens(LeetcodeProblem):
    def solve(self, n):
        self.cols = [-1] * n

        self.y_used = [False] * n
        self.md_used = [False] * (2 * n - 1)
        self.sd_used = [False] * (2 * n - 1)

        self.res = []

        self.go(n, 0)

        return self.constructSolution(n, self.res)

    def go(self, n, i):
        if i == n:
            self.res.append(self.cols[:])
        else:
            for j in xrange(n):
                if (
                    not self.y_used[j] and
                    not self.md_used[i - j + n - 1] and
                    not self.sd_used[i + j]
                ):
                    self.y_used[j] = True
                    self.md_used[i - j + n - 1] = True
                    self.sd_used[i + j] = True
                    self.cols[i] = j

                    self.go(n, i + 1)

                    self.y_used[j] = False
                    self.md_used[i - j + n - 1] = False
                    self.sd_used[i + j] = False
                    self.cols[i] = -1

    def constructSolution(self, n, res):
        boards = []
        for solution in res:
            b = []
            for i in xrange(n):
                b.append('.' * solution[i] + 'Q' + '.' * (n - solution[i] - 1))
            boards.append(b)
        return boards

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseStringArrayArrays
        for o in parseStringArrayArrays(open(self.outputPath)):
            yield o[0]

problem = NQueens
