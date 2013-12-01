from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class BinaryTreeMaximumPathSum(LeetcodeProblem):
    def solve(self, root):
        return 0

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = BinaryTreeMaximumPathSum
