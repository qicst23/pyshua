from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class BinaryTreeMaximumPathSum(LeetcodeProblem):
    def solve(self, root):
        return self.maxSum(root)[1]

    def maxSum(self, node):
        if not node:
            return 0, 0
        else:
            leftOneSide, left = self.maxSum(node.left)
            rightOndeSide, right = self.maxSum(node.right)
            oneSide = max(
                node.val,
                node.val + leftOneSide,
                node.val + rightOndeSide
            )
            res = max(
                oneSide,
                node.val + leftOneSide + rightOndeSide
            )

            if node.left:
                res = max(res, left)
            if node.right:
                res = max(res, right)

            return oneSide, res

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
