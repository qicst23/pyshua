from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class SearchinRotatedSortedArrayII(LeetcodeProblem):
    def solve(self, a, target):
        for n in a:
            if n == target:
                return True
        return False

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseArrayAndInt
        return parseArrayAndInt(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = SearchinRotatedSortedArrayII
