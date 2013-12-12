from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class BalancedBinaryTree(LeetcodeProblem):
    def solve(self, root):
        if not root:
            return True
        else:
            return (self.solve(root.left)
                    and self.solve(root.right)
                    and abs(self.height(root.left) -
                            self.height(root.right)) <= 1)

    def height(self, root):
        if not root:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = BalancedBinaryTree
