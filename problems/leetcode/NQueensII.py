from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class NQueensII(LeetcodeProblem):
    def solve(self, n):
        self.res = 0

        self.cols = [-1] * n

        self.y_used = [False] * n
        self.md_used = [False] * (2 * n - 1)
        self.sd_used = [False] * (2 * n - 1)

        self.go(n, 0)

        return self.res

    def go(self, n, i):
        if i == n:
            self.res += 1
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

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = NQueensII
