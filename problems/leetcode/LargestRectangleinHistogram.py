from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class LargestRectangleinHistogram(LeetcodeProblem):
    def solve(self, height):
        height.append(0)

        n = len(height)
        res = 0
        stack = []
        i = 0
        while i < n:
            if not stack or height[i] >= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                h = height[stack.pop()]
                w = i - (stack[-1] if stack else -1) - 1
                area = h * w
                if res < area:
                    res = area
        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = LargestRectangleinHistogram
