from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class BinaryTreePostorderTraversal(LeetcodeProblem):
    def solve(self, root):
        res = []
        stack = []
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left

        return list(reversed(res))

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = BinaryTreePostorderTraversal
