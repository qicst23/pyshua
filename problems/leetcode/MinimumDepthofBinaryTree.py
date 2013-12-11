from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class MinimumDepthofBinaryTree(LeetcodeProblem):
    def solve(self, root):
        if not root:
            return 0
        else:
            if root.left and root.right:
                return 1 + min(
                    self.solve(root.left),
                    self.solve(root.right)
                )
            elif root.left or root.right:
                return 1 + self.solve(root.left or root.right)
            else:
                return 1

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = MinimumDepthofBinaryTree
