from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class MaximalRectangle(LeetcodeProblem):
    def solve(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0

        res = 0
        h = [0] * (n + 1)
        level = 0
        while level < m:
            for i in xrange(n):
                if matrix[level][i] == '0':
                    h[i] = 0
                else:
                    h[i] += 1
            levelMaxArea = self.maxArea(h, n)
            if res < levelMaxArea:
                res = levelMaxArea
            level += 1
        return res

    def maxArea(self, h, n):
        stack = []
        res = 0
        i = 0
        while i < n + 1:
            if not stack or h[i] >= h[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                height = h[stack.pop()]
                width = i - (stack[-1] if stack else -1) - 1
                area = height * width
                if res < area:
                    res = area
        return res

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
