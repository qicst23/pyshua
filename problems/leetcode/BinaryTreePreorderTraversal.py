from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class BinaryTreePreorderTraversal(LeetcodeProblem):
    def solve(self, root):
        stack = []
        cur = root
        res = []

        while stack or cur:
            if cur:
                res.append(cur.val)

                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right

        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = BinaryTreePreorderTraversal
