from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class ValidateBinarySearchTree(LeetcodeProblem):
    def solve(self, root):
        return self.isValid(root, -float('inf'), float('inf'))

    def isValid(self, node, low, high):
        if not node:
            return True

        if not low < node.val < high:
            return False

        return self.isValid(
            node.left, low, node.val
        ) and self.isValid(
            node.right, node.val, high
        )

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseBoolean
        for o in parseBoolean(open(self.outputPath)):
            yield o[0]

problem = ValidateBinarySearchTree
