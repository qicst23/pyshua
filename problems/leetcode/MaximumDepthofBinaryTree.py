from problems.leetcode.LeetcodeProblem import LeetcodeProblem


class MaximumDepthofBinaryTree(LeetcodeProblem):
    def solve(self, root):
        stack = []
        cur = root
        res = 0
        h = 0

        while stack or cur:
            if cur:
                h += 1
                stack.append((cur, h))
                cur = cur.left
                if h > res:
                    res = h
            else:
                cur, h = stack.pop()
                cur = cur.right

        return res

    def verify(self, original_input, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseBinaryTree
        return parseBinaryTree(open(self.inputPath))

    def output(self):
        from Parser import parseOneInt
        for o in parseOneInt(open(self.outputPath)):
            yield o[0]

problem = MaximumDepthofBinaryTree
