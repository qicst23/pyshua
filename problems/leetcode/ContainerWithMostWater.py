from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ContainerWithMostWater(LeetcodeProblem):
    def solve(self, height):
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            if height[i] < height[j]:
                area = height[i] * (j - i)
                i += 1
            else:
                area = height[j] * (j - i)
                j -= 1
            if res < area:
                res = area

        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseIntArray
        return parseIntArray(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = ContainerWithMostWater
